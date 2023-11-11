import sys
import pathlib
import asyncio
import getpass
import json
import rich
import time

# Allow running straight out of the repo
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

from lucidmotors import LucidAPI, LoginResponse

if len(sys.argv) < 2:
    print('Please enter your Lucid account credentials.')

    username = input('Username: ')
    password = getpass.getpass()

    async def main():
        async with LucidAPI() as lucid:
            await lucid.login(username, password)
            print('Logged in. User profile:')
            rich.print(lucid.user)
            print('Vehicles:')
            rich.print(lucid.vehicles)

            print('... Sleeping 5s to be nice ...')
            print('Then refreshing vehicle info')
            time.sleep(5)

            await lucid.fetch_vehicles()
            rich.print(lucid.vehicles)

    asyncio.run(main())

else:
    for sample in sys.argv[1:]:
        print(f'Reading sample data file {sample}')

        with open(sample, 'r') as fi:
            raw = json.load(fi)
            data = LoginResponse.model_validate(raw)
            print('User profile:')
            rich.print(data.user_profile)
            print('User vehicles:')
            rich.print(data.user_vehicle_data)
