"""
Keywords, helper classes and helper functions for the Robot Framework Relukko
package.
"""
import time
from datetime import datetime
from dataclasses import field, fields, dataclass
from functools import wraps
from typing import Dict, Union
from urllib3.util.retry import Retry

import requests
from robot.api import logger, SkipExecution
from robot.api.deco import not_keyword, keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.utils.robottime import timestr_to_secs


class RelukkoConflict(Exception):
    """
    Exception thrown when the lock already exists (HTTP: 409).
    """


class RelukkoRecoverableException(Exception):
    """
    Exception thrown when there is chance it might work later again.
    """


class RelukkoNonRecoverableException(Exception):
    """
    Exception thrown when there is no chance it might work later again,
    retry is futile.
    """


@dataclass
class RetryConfig:
    """
    Dataclass to store various parameters of the retry decorator.
    """
    # pylint: disable=too-many-instance-attributes
    conn_err_tries: int = field(default=4)
    conn_err_delay: int = field(default=30)
    rl_err_tries: int = field(default=3)
    rl_err_delay: int = field(default=10)
    conflict_tries: int = field(default=30)
    conflict_delay: int = field(default=10)
    conflict_max_delay: int = field(default=120)
    conflict_backoff: float = field(default=1.1)


def _get_retry_msg(cause: str, tries: int, cur_try: int, delay: float) -> str:
    msg = f'[{cause}]({tries - cur_try}/{tries}): '
    msg += f'Retrying in {delay:.2f} seconds!'
    return msg


def retry(rt_logger, conf: RetryConfig):
    """
    Retry calling the decorated function using an exponential backoff.
    https://www.calazan.com/retry-decorator-for-python-3/

    :param exceptions: The exception(s) to catch, tuple for multiple exeptions.
    :param tries: Number of times to try (not retry) before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Backoff multiplier (e.g. value of 2 will double the delay
     each retry).
    :param max_delay: maximum value for delay
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            remaining_conn_err_tries = conf.conn_err_tries
            remaining_rl_err_tries = conf.rl_err_tries
            remaining_conflict_tries = conf.conflict_tries
            requests_exceptions = (
                requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout,
            )
            while True:
                try:
                    return f(*args, **kwargs)
                except RelukkoConflict as e:
                    remaining_conflict_tries -= 1
                    if remaining_conn_err_tries < 0:
                        raise SkipExecution("Failed to lock resource!") from e
                    msg = _get_retry_msg(
                        "Conflict", conf.conflict_tries,
                        remaining_conflict_tries, conf.conflict_delay)
                    rt_logger.info(msg)
                    time.sleep(conf.conflict_delay)
                    conf.conflict_delay = min(
                        conf.conflict_delay*conf.conflict_backoff,
                        conf.conflict_max_delay)
                except requests_exceptions as e:
                    # Relukko down? Maybe restart? Let's try in a moment!
                    remaining_conn_err_tries -= 1
                    if remaining_conn_err_tries < 0:
                        raise e
                    msg = _get_retry_msg(
                        type(e).__name__, conf.conn_err_tries,
                        remaining_conn_err_tries, conf.conn_err_delay)
                    rt_logger.info(msg)
                    time.sleep(conf.conn_err_delay)
                except RelukkoRecoverableException as e:
                    # There is not much hope this will recover! Still let's try
                    remaining_rl_err_tries -= 1
                    if remaining_rl_err_tries < 0:
                        raise e
                    msg = _get_retry_msg(
                        "RelukkoRecoverableException", conf.rl_err_tries,
                        remaining_rl_err_tries,conf.rl_err_delay)
                    rt_logger.warn(msg)
                    time.sleep(conf.rl_err_delay)
        return f_retry  # true decorator
    return deco_retry


class Relukko:
    """
    Robot Framework keywords to acquire locks from a
    [https://gitlab.com/relukko/relukko|Relukko backend].

    The library can be configured at initializing time or later with the
    keyword `Setup Relukko`.

    Example set up:
    | ***** Settings *****
    | Library    Relukko    creator=Demo Creator
    |
    |
    | ***** Test Cases *****
    | Test Resource Lock
    |     [Tags]    test_case_id:eb3a4185-185b-4ac6-a63d-5d1f20e55134
    |     Set Up Relukko    http://localhost:3000    some-api-key
    |     Acquire Relukko For Test

    DTO of a "Relukko" lock:
    | {
    |   "id": "950daa20-a814-451e-9407-ec496cf9c136",
    |   "lock_name": "eb3a4185-185b-4ac6-a63d-5d1f20e55134",
    |   "creator": "Demo Creator",
    |   "ip": "10.89.0.6",
    |   "expires_at": "2024-10-31T20:14:43.9313Z",
    |   "created_at": "2024-10-31T20:04:43.9313Z",
    |   "updated_at": "2024-10-31T20:04:43.9313Z"
    | }
    """
    # pylint: disable=too-many-instance-attributes
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(
            self, base_url: str=None, api_key: str=None,
            creator: str=None, **kwargs):
        """
        ``base_url`` The URL of the Relukko back end (without ``/v1/locks``).

        ``api_key`` The API Key to do the HTTP REST calls.

        ``creator`` An optinal name of the creator of the lock, only for
                    information.

        ``**kwargs`` The kwargs are passed to ``requests.Session``, the
                     ``RetryConfig`` and the ``http_adapter.max_retries``.
        """
        self.base_url: str = base_url
        self.url = f"{base_url}/v1/locks"

        self.api_key: str = api_key
        self.creator: str = creator

        self.session = requests.Session()
        self.session.headers = {'X-api-Key': api_key}
        self._handle_session_kwagrs(**kwargs)
        self._setup_http_adapters_retry(**kwargs)

        # Settings for retry decorator
        self.retry_conf = RetryConfig()
        self._handle_retry_config_kwargs(**kwargs)

        self.builtin = BuiltIn()

        # Forward declaration will be filled later
        self.lock_name: str = None
        self.lock: str = None
        self.lock_url: str = None

    @not_keyword
    def _handle_session_kwagrs(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.session, key):
                setattr(self.session, key, value)

    @not_keyword
    def _handle_retry_config_kwargs(self, **kwargs):
        for item in fields(self.retry_conf):
            kw_val = kwargs.get(item.name)
            if kw_val:
                setattr(self.retry_conf, item.name, item.type(kw_val))

    @not_keyword
    def _setup_http_adapters_retry(self, **kwargs):
        total = kwargs.get('har_total', None)
        connect = kwargs.get('har_connect', 3)
        read = kwargs.get('har_read', 3)
        redirect = kwargs.get('har_redirect', 3)
        other = kwargs.get('har_other', 3)
        backoff_factor = kwargs.get('har_backoff_factor', 3)
        backoff_jitter = kwargs.get('har_backoff_jitter', 3)

        for _, http_adapter in self.session.adapters.items():
            http_adapter.max_retries = Retry(
                total=total, connect=connect, read=read, redirect=redirect,
                other=other, backoff_factor=backoff_factor,
                backoff_jitter=backoff_jitter)

    @not_keyword
    def _relukko_request_with_retry(
        self,
        method: str,
        url: str,
        payload: Union[Dict, None],
    ):

        @retry(rt_logger=logger, conf=self.retry_conf)
        def _relukko_request(
            session: requests.Session,
            method: str,
            url: str,
            payload: Union[Dict, None],
        ):
            res = session.request(method=method, url=url, json=payload)
            match res.status_code:
                # case 404?
                case 200 | 201:
                    return res.json()
                case 400 | 403:
                    err = res.json()
                    logger.warn(err.get('status'), err.get('message'))
                    raise RelukkoNonRecoverableException()
                case 409:
                    err = res.json()
                    logger.info(err.get('status'), err.get('message'))
                    raise RelukkoConflict()
                case _:
                    logger.warn(res.status_code, res.text)
                    raise RelukkoRecoverableException()

        return _relukko_request(
            session=self.session, method=method, url=url, payload=payload)

    def set_up_relukko(
            self, base_url: str=None, api_key: str=None, creator: str=None,
            cert=None, **kwargs):
        """
        It might not be possible to configure everything already when the
        library is imported. This keyword allows to finish the configuration.

        Arguments given to this keyword take precedence of already configured
        values during import!

        ``base_url`` The URL of the Relukko back end (without
                     ``/v1/locks``).

        ``api_key`` The API Key to do the HTTP REST calls.

        ``creator`` An optinal name of the creator of the lock, only for
                    information.

        ``**kwargs`` The kwargs are passed to ``requests.Session``, the
                     ``RetryConfig`` and the ``http_adapter.max_retries``.
        """
        # Maybe these things have been set already in during __init__
        # if given again use the given values otherwise keep what was
        # initialized earlier.
        self.base_url = base_url or self.base_url
        self.url = f"{base_url or self.base_url}/v1/locks"
        self.api_key = api_key or self.api_key
        self.creator = creator or self.creator

        self.session.cert = cert or self.session.cert
        self.session.headers = {'X-api-Key': api_key or self.api_key}

        self._handle_session_kwagrs(**kwargs)
        self._handle_retry_config_kwargs(**kwargs)

    def acquire_relukko(
            self, lock_name: str, creator: str=None) -> Union[Dict, None]:
        """
        Create (acquire) a lock from the Relukko back end. If the ``lock_name``
        already exists in the Relukko back end, then it block the execution
        until it gets the lock or gives up.

        ``lock_name`` The name of the lock that shall be acquired.

        ``creator`` An optinal name of the creator of the lock, only for
                    information. If omitted the value set during library
                    configuration (see: `Importing` or `Setup Relukko`) is used.

        Returns the created DTO of the lock (dict).
        """
        payload = {
            "lock_name": lock_name,
            "creator": creator or self.creator,
        }

        self.lock = self._relukko_request_with_retry(
            method="post", url=self.url, payload=payload)

        self.lock_url = f"{self.url}/{self.lock['id']}"
        logger.info(f"Relukko created: {self.lock}")
        return self.lock

    def keep_relukko_alive_for_the_next_5_min(self) -> Union[Dict, None]:
        """
        Keeps the current Relukko lock alive by setting the expires at time to
        5 minutes from _now_ into the future.

        Returns the updated DTO of the lock (dict).
        """
        url = f"{self.lock_url}/keep_alive"

        self.lock = self._relukko_request_with_retry(
            method="get", url=url, payload=None)
        logger.info(f"Relukko kept alive: {self.lock}")
        return self.lock

    @keyword(
        name='Keep Relukko Alive For The Next "${seconds}" Seconds',
        types=[int])
    def keep_relukko_alive_for_x_seconds(
        self, seconds: int) -> Union[Dict, None]:
        """
        Keeps the current Relukko lock alive by setting the expires at time to
        the amount of seconds provided from _now_ into the future.

        ``seconds`` The amount of seconds to at to from now.

        Returns the updated DTO of the lock (dict).
        """
        url = f"{self.lock_url}/keep_alive"
        payload = {
            "seconds": seconds
        }
        self.lock = self._relukko_request_with_retry(
            method="put", url=url, payload=payload)
        logger.info(f"Relukko kept alive: {self.lock}")
        return self.lock

    def keep_relukko_alive_for_the_next(self, timestr: str) -> Union[Dict, None]:
        """
        Keeps the current Relukko lock alive by setting the expires at time to
        the amount of time provided in the ``timestr`` from _now_ into the future.

        The ``timestr`` must follow Robot Framework's
        [https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format|Time Format].

        Example:
        | Keep Relukko Alive For The Next    1h34m13s

        ``timestr`` The amount of time to set the expires at time into the
                    future.

        Returns the updated DTO of the lock (dict).
        """
        return self.keep_relukko_alive_for_x_seconds(
            timestr_to_secs(timestr=timestr))


    def add_to_current_relukko_expire_at_time_5_min(self) -> Union[Dict, None]:
        """
        Keeps the current Relukko lock alive by adding 5 minutes to the
        current expires at time.

        Returns the updated DTO of the lock (dict).
        """
        url = f"{self.lock_url}/add_to_expire_at"

        self.lock = self._relukko_request_with_retry(
            method="get", url=url, payload=None)
        logger.info(f"Time added to Relukko expires at: {self.lock}")
        return self.lock

    @keyword(
        name='Add To Current Relukko Expire At Time "${seconds}" Seconds',
        types=[int])
    def add_to_current_relukko_expire_time_x_seconds(
        self, seconds: int) -> Union[Dict, None]:
        """
        Keeps the current Relukko lock alive by adding the provided amount of
        seconds to the current expires at time.

        ``seconds`` The amount of seconds to at to the current expires at time.

        Returns the updated DTO of the lock (dict).
        """
        url = f"{self.lock_url}/add_to_expire_at"
        payload = {
            "seconds": seconds
        }
        self.lock = self._relukko_request_with_retry(
            method="put", url=url, payload=payload)
        logger.info(f"Time added to Relukko expires at: {self.lock}")
        return self.lock

    def add_to_current_relukko_expire_at_time(
            self, timestr: str) -> Union[Dict, None]:
        """
        Keeps the current Relukko lock alive by adding the amount of time
        provided in the ``timestr`` to the current expires at time.

        The ``timestr`` must follow Robot Framework's
        [https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format|Time Format].

        Example:
        | Add To Current Relukko Expire At Time    1h34m13s

        Returns the updated DTO of the lock (dict)
        """
        return self.add_to_current_relukko_expire_time_x_seconds(
            timestr_to_secs(timestr=timestr))

    def update_relukko(
            self,
            creator: str=None,
            expires_at: Union[str, datetime]=None) -> Union[Dict, None]:
        """
        Allows to change the "creator" of the lock and/or the expires at time
        to any time.

        ``creator`` An name to set as the creator of the lock, if omitted the
                    value does not change in the Relukko back end.

        ``expires_at`` The new to set expires at time either as string in the
                       RFC3339 format (``YYYY-MM-DDThh:mm:ss.ssssssZ``) or as
                       datetime object, if omitted the value does not change
                       in the Relukko back end.

        Returns the updated DTO of the lock (dict).
        """
        if isinstance(expires_at, datetime):
            expires_at = expires_at.isoformat()

        payload = {
            "creator": creator,
            "expires_at": expires_at,
        }
        self.lock = self._relukko_request_with_retry(
            method="put", url=self.lock_url, payload=payload)
        logger.info(f"Relukko updated: {self.lock}")
        return self.lock

    def delete_relukko(self) -> Union[Dict, None]:
        """
        Deletes the Relukko lock from the backend.

        Returns the deleted DTO of the lock (dict).
        """
        self.lock = self._relukko_request_with_retry(
            method="delete", url=self.lock_url, payload=None)
        logger.info(f"Relukko deleted: {self.lock}")
        return self.lock

    def get_current_relukko(self, refresh: bool=False) -> Union[Dict, None]:
        """
        If ``refresh`` is ``True`` it fetches an up to date version of the
        Relukko DTO from the back end and returns it. Otherwise by default
        it returns the stored Relukko lock DTO.

        ``refresh`` Shall the Relukko DTO be fetched from the Relukko back end.

        Returns the current DTO of the lock (dict)
        """
        if refresh:
            self.lock = self._relukko_request_with_retry(
                method="get", url=self.lock_url, payload=None)
        logger.info(self.lock)
        return self.lock

    def get_relukko_expires_at_time(self, refresh: bool=False) -> datetime:
        """
        If ``refresh`` is ``True`` it fetches an up to date version of the
        Relukko DTO from the back end. Otherwise by default it returns the
        stored expires at as ``datetime`` object.

        ``refresh`` Shall the Relukko DTO be fetched from the Relukko back end.

        Returns the expires at time as ``datetime``
        """
        if refresh or self.lock is None:
            self.lock = self._relukko_request_with_retry(
                method="get", url=self.lock_url, payload=None)

        expires_at = datetime.fromisoformat(self.lock.get("expires_at"))
        logger.info(expires_at)

    def acquire_relukko_for_test(self) -> Union[Dict, None]:
        """
        Create (acquire) a lock from the Relukko back end. The ``lock_name``
        is derived either from the tag that starts with ``test_case_id:`` or if
        no such tag is found from the suite and test case name. For the
        ``creator`` the configured value is used (see: `Importing` or
        `Setup Relukko`).

        If derived from ``test_case_id`` tag only the part after the `:` (colon)
        is used, from the tag:
        ```test_case_id:81f2c642-ddaf-400d-9f6b-4b1c89ef9732`` the resulting
        lock name will be: ``81f2c642-ddaf-400d-9f6b-4b1c89ef9732``.

        If derived from suite name and test case, the lock name will be:
        ``f"{suite_name}:{test_name}"``

        Returns the created DTO of the lock (dict)
        """
        test_tags = self.builtin.get_variable_value("@{TEST TAGS}")
        test_case_id_tag = [
            x for x in test_tags if x.startswith('test_case_id:')]
        if test_case_id_tag:
            lock_name = test_case_id_tag[0][13:]
        else:
            test_name = self.builtin.get_variable_value("${TEST NAME}")
            suite_name = self.builtin.get_variable_value("${SUITE NAME}")
            lock_name = f"{suite_name}:{test_name}"

        logger.info(f"Derived lock name: {lock_name}")
        return self.acquire_relukko(lock_name=lock_name)
