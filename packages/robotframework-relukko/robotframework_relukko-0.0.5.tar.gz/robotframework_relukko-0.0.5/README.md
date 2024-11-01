# Robotframework Relukko

```robot
*** Settings ***
Library    Relukko    creator=Creator Name


*** Test Cases ***
Test Resource Lock
    Set Up Relukko    http://localhost:3000    some-api-key
    Acquire Relukko    LockName
    Sleep    5s
    Keep Relukko Alive
    Sleep    5s
    Keep Relukko Alive For "1200" Seconds
    Sleep    5s
    Keep Relukko Alive For    1h34m12s
    Sleep    5s
    Add To Current Relukko Expire    1m24s
    Sleep    5s
    Add To Current Relukko Expire At
    Sleep    5s
    Add To Current Relukko Expire Time "1800" Seconds
    Sleep    5s
    Update Relukko    creator=Mark
    Sleep    5s
    Update Relukko    expires_at=2025-01-01T12:34:56.123456Z
    Sleep    5s
    Delete Relukko
```