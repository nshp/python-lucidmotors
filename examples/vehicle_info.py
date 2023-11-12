import sys
import pathlib
import asyncio
import getpass
import json
import rich
import time
import logging

# Allow running straight out of the repo
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

from lucidmotors import LucidAPI, LoginResponse  # noqa: E402

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) < 2:
    print("Please enter your Lucid account credentials.")

    username = input("Username: ")
    password = getpass.getpass()

    async def main():
        async with LucidAPI() as lucid:
            await lucid.login(username, password)
            print("Logged in. User profile:")
            rich.print(lucid.user)

            print("Vehicles:")
            rich.print(lucid.vehicles)

            time.sleep(1)

            print("Waking up vehicle")
            await lucid.wakeup_vehicle(lucid.vehicles[0])

            print("... Sleeping 5s to be nice ...")
            time.sleep(5)

            print("Honking horn")
            await lucid.honk_horn(lucid.vehicles[0])

            print("... Sleeping 5s to be nice ...")
            time.sleep(5)

            print("Flashing lights")
            await lucid.lights_flash(lucid.vehicles[0])

            print("... Sleeping 5s to be nice ...")
            time.sleep(5)

            print("Then refreshing vehicle info")
            await lucid.fetch_vehicles()
            rich.print(lucid.vehicles)

    asyncio.run(main())

else:
    for sample in sys.argv[1:]:
        print(f"Reading sample data file {sample}")

        with open(sample, "r") as fi:
            raw = json.load(fi)
            data = LoginResponse.model_validate(raw)
            print("User profile:")
            rich.print(data.user_profile)
            print("User vehicles:")
            rich.print(data.user_vehicle_data)
