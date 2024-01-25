import sys
import pathlib
import asyncio
import getpass
import rich
import logging

# Allow running straight out of the repo
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

from lucidmotors import LucidAPI  # noqa: E402

logging.basicConfig(level=logging.DEBUG)

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

        print("... Sleeping 1s to be nice ...")
        await asyncio.sleep(1)

        print("Then refreshing vehicle info")
        await lucid.fetch_vehicles()
        rich.print(lucid.vehicles)


asyncio.run(main())
