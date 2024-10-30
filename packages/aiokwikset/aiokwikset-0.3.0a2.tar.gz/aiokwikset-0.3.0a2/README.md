# aiokwikset - Python interface for the Kwikset API

Python library for communicating with the [Kwikset Smart Locks](https://www.kwikset.com/products/electronic/electronic-smart-locks) via the Kwikset cloud API.

***WARNING***
* This library only works if you have signed up for and created a home/had a home shared with you from the Kwikset Application.
* [IOS](https://apps.apple.com/us/app/kwikset/id1465996742)
* [Android](https://play.google.com/store/apps/details?id=com.kwikset.blewifi)

NOTE:

* This library is community supported, please submit changes and improvements.
* This is a very basic interface, not well thought out at this point, but works for the use cases that initially prompted spitting this out from.

## Supports

- locking/unlocking
- retrieving basic information

## Installation

```
pip install aiokwikset
```

## Examples

```python
import asyncio

from aiokwikset import API


async def main() -> None:
    """Run!"""
    #initialize the API
    api = API("<EMAIL>")

    #start auth
    #<CODE_TYPE> = [phone, email]
    pre_auth = await api.authenticate('<PASSWORD>','<CODE_TYPE>')

    #MFA verification
    await api.verify_user(pre_auth, input("Code:"))

    # Get user account information:
    user_info = await api.user.get_info()

    # Get the homes
    homes = await api.user.get_homes()

    # Get the devices for the first home
    devices = await api.device.get_devices(homes[0]['homeid'])

    # Get information for a specific device
    device_info = await api.device.get_device_info(devices[0]['deviceid'])

    # Lock the specific device
    lock = await api.device.lock_device(device_info, user_info)

    # Set led status
    led = await api.device.set_ledstatus(device_info, "false")

    # Set audio status
    audio = await api.device.set_audiostatus(device_info, "false")

    # Set secure screen status
    screen = await api.device.set_securescreenstatus(device_info, "false")


asyncio.run(main())
```

## Known Issues

* not all APIs supported
