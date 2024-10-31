"""
TBD
"""
import time
from datetime import datetime
from dataclasses import field, fields, dataclass
from functools import wraps
from typing import Dict, Union
from urllib3.util.retry import Retry

import requests
from robot.api import logger
from robot.utils.robottime import timestr_to_secs
from robot.errors import ExecutionFailed
from robot.api.deco import not_keyword, keyword

# import logging
#
# from http.client import HTTPConnection
# HTTPConnection.debuglevel = 1
# # you need to initialize logging, otherwise you will not see anything from requests
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

class RelukkoConflict(Exception):
    """
    TBD
    """


class RelukkoRecoverableException(Exception):
    """
    TBD
    """


class RelukkoNonRecoverableException(Exception):
    """
    TBD
    """


@dataclass
class RetryConfig:
    """
    TBD
    """
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
                        raise ExecutionFailed("Failed to lock resource!") from e
                    msg = _get_retry_msg("Conflict",
                        conf.conflict_tries, remaining_conflict_tries, conf.conflict_delay)
                    rt_logger.info(msg)
                    time.sleep(conf.conflict_delay)
                    conf.conflict_delay = min(
                        conf.conflict_delay*conf.conflict_backoff, conf.conflict_max_delay)
                except requests_exceptions as e:
                    # Relukko down? Maybe restart? Let's try in a moment!
                    remaining_conn_err_tries -= 1
                    if remaining_conn_err_tries < 0:
                        raise e
                    msg = _get_retry_msg(type(e).__name__,
                        conf.conn_err_tries, remaining_conn_err_tries, conf.conn_err_delay)
                    rt_logger.info(msg)
                    time.sleep(conf.conn_err_delay)
                except RelukkoRecoverableException as e:
                    # There is not much hope this will recover! Still let's try
                    remaining_rl_err_tries -= 1
                    if remaining_rl_err_tries < 0:
                        raise e
                    msg = _get_retry_msg("RelukkoRecoverableException",
                        conf.rl_err_tries, remaining_rl_err_tries, conf.rl_err_delay)
                    rt_logger.warn(msg)
                    time.sleep(conf.rl_err_delay)
        return f_retry  # true decorator
    return deco_retry


class Relukko:
    """
    TBD
    """
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(
            self, base_url: str=None, api_key: str=None,
            creator: str=None, cert=None, **kwargs):
        """
        """
        self.base_url: str = base_url
        self.url = f"{base_url}/v1/locks"

        self.api_key: str = api_key
        self.creator: str = creator

        self.session = requests.Session()
        self.session.cert = cert
        self.session.headers = {'X-api-Key': api_key}
        self._handle_session_kwagrs(**kwargs)
        self._setup_http_adapters_retry(**kwargs)

        # Settings for retry decorator
        self.retry_conf = RetryConfig()
        self._handle_retry_config_kwargs(**kwargs)

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
        TODO: use **kwargs? prefix retry_conf?
        TODO: get creator, api-key, base_url from env var
        TODO: move to init, or part of it?
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

    def acquire_relukko(self, lock_name: str, creator: str=None):
        """
        TBD
        """
        payload = {
            "lock_name": lock_name,
            "creator": creator or self.creator,
        }

        self.lock = self._relukko_request_with_retry(
            method="post", url=self.url, payload=payload)

        self.lock_url = f"{self.url}/{self.lock['id']}"
        print("lock created", self.lock)

    def keep_relukko_alive(self):
        """
        TBD
        """
        url = f"{self.lock_url}/keep_alive"

        self.lock = self._relukko_request_with_retry(
            method="get", url=url, payload=None)
        print(self.lock)

    @keyword(name='Keep Relukko Alive For "${seconds}" Seconds', types=[int])
    def keep_relukko_alive_for_x_seconds(self, seconds: int):
        """
        TBD
        """
        url = f"{self.lock_url}/keep_alive"
        payload = {
            "seconds": seconds
        }
        self.lock = self._relukko_request_with_retry(
            method="put", url=url, payload=payload)
        print(self.lock)

    def keep_relukko_alive_for(self, timestr: str):
        """
        Robot Framework's
        [https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format|Time Format]
        """
        self.keep_relukko_alive_for_x_seconds(timestr_to_secs(timestr=timestr))


    def add_to_current_relukko_expire_at(self):
        """
        TBD
        """
        url = f"{self.lock_url}/add_to_expire_at"

        self.lock = self._relukko_request_with_retry(
            method="get", url=url, payload=None)
        print(self.lock)

    @keyword(name='Add To Current Relukko Expire Time "${seconds}" Seconds',
             types=[int])
    def add_to_current_relukko_expire_time_x_seconds(self, seconds: int):
        """
        TBD
        """
        url = f"{self.lock_url}/add_to_expire_at"
        payload = {
            "seconds": seconds
        }
        self.lock = self._relukko_request_with_retry(
            method="put", url=url, payload=payload)
        print(self.lock)

    def add_to_current_relukko_expire(self, timestr: str):
        """
        Robot Framework's
        [https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format|Time Format]
        """
        self.add_to_current_relukko_expire_time_x_seconds(
            timestr_to_secs(timestr=timestr))

    def update_relukko(
            self, creator: str=None, expires_at: Union[str, datetime]=None):
        """
        TBD
        """
        if isinstance(expires_at, datetime):
            expires_at = expires_at.isoformat()
            print("iso:", expires_at)

        payload = {
            "creator": creator,
            "expires_at": expires_at,
        }
        self.lock = self._relukko_request_with_retry(
            method="put", url=self.lock_url, payload=payload)
        print(self.lock)

    def delete_relukko(self):
        """
        TBD
        """
        self.lock = self._relukko_request_with_retry(
            method="delete", url=self.lock_url, payload=None)
        print(self.lock)
