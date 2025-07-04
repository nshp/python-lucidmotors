#!/usr/bin/env python3
"""
Run this by setting LUCID_USERNAME and LUCID_PASSWORD environment variables, then running:
quart --app evcc_plugin run

By default, the plugin will listen on port 5118.

To configure EVCC to use the plugin, go to http://<host>:<port>/evcc-config and
add the generated vehicle config to evcc.yaml's vehicles section.
"""

import os
import sys
import pathlib
import logging
import time
import yaml

from quart import Quart, request, current_app

# Allow running straight out of the repo
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

from lucidmotors import LucidAPI, ChargeState, HvacPower  # noqa: E402

logging.basicConfig(level=logging.DEBUG)

app = Quart(__name__)

username = os.getenv('LUCID_USERNAME')
password = os.getenv('LUCID_PASSWORD')
os.unsetenv('LUCID_PASSWORD')

timeout_ms = 5 * 60 * 1000 - 1000


async def _get_api_client():
    if not hasattr(current_app, "lucid_api"):
        print('do not have an active lucid_api session, creating new one.')
        current_app.lucid_api = LucidAPI()
        await current_app.lucid_api.login(username, password)
    if (current_app.lucid_api.vehicles and
            current_app.lucid_api.vehicles[0].state.last_updated_ms + timeout_ms < time.time() * 1000):
        print('timeout since last update')
        await current_app.lucid_api.authentication_refresh()
        await current_app.lucid_api.fetch_vehicles()
    return current_app.lucid_api


@app.get("/")
async def root():
    lucid = await _get_api_client()
    return list(map(lambda x: (x.vehicle_id, x.config.nickname), lucid.vehicles))


@app.get("/evcc-config")
async def get_evcc_config(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    origin = request.headers['Host']
    return yaml.dump({
        'vehicles': [{
            'name': 'lucid-' + v.vehicle_id,
            'type': 'custom',
            'title': v.config.nickname,
            'icon': 'car',
            'capacity': int(v.state.battery.capacity_kwhr),
            'phases': 3,
            'soc': make_http_source(origin, 'soc'),
            'limitsoc': make_http_source(origin, 'limitsoc'),
            'status': make_http_source(origin, 'status'),
            'range': make_http_source(origin, 'range'),
            'odometer': make_http_source(origin, 'odometer'),
            'climater': make_http_source(origin, 'climater'),
            'getmaxcurrent': make_http_source(origin, 'getmaxcurrent'),
            'chargeenable': {
                'source': 'http',
                'method': 'POST',
                'uri': f'http://{origin}/chargeenable',
                'body': "{{if .chargeenable}}1{{else}}0{{end}}"
            },
            'wakeup': {
                'source': 'http',
                'method': 'POST',
                'uri': f'http://{origin}/wakeup',
                'body': "{{if .wakeup}}1{{else}}0{{end}}"
            }
        }]
    }, sort_keys=False)


#  # Read values
#  soc:
#    source: const
#    value: 80
@app.get("/soc")
async def get_soc(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    return str(int(v.state.battery.charge_percent))


#  limitsoc:
#    source: const
#    value: 100
@app.get("/limitsoc")
async def get_limitsoc(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    return str(int(v.state.charging.charge_limit_percent))


#  status:
#    source: const
#    value: A
@app.get("/status")
async def get_status(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    if v.state.charging.charge_state == ChargeState.CHARGE_STATE_NOT_CONNECTED:
       return "A"
    elif v.state.charging.charge_state == ChargeState.CHARGE_STATE_CABLE_CONNECTED:
       return "B"
    elif v.state.charging.charge_state == ChargeState.CHARGE_STATE_CHARGING:
       return "C"
    elif v.state.charging.charge_state == ChargeState.CHARGE_STATE_CHARGING:
       return "E"
    else:
       return ""


#  range:
#    source: const
#    value: 67
@app.get("/range")
async def get_range(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    return str(int(v.state.battery.remaining_range))


#  odometer:
#    source: const
#    value: 696969
@app.get("/odometer")
async def get_odometer(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    return str(int(v.state.chassis.odometer_km))


#  climater:
#    source: const
#    value: false
@app.get("/climater")
async def get_climater(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    return str(v.state.hvac.power != HvacPower.HVAC_OFF)


#  getmaxcurrent:
#    source: const
#    value: 80
@app.get("/getmaxcurrent")
async def get_maxcurrent(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    return str(int(v.state.charging.charge_limit))

#  # Write values
#  wakeup:
#    source: const
#    value: true
@app.post("/wakeup")
async def post_wakeup(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    async with request.get_data() as request_data:
        if request_data.strip() == '1':
            await lucid.wakeup_vehicle(v)


#  chargeenable:
#    source: const
#    value: false
@app.post("/chargeenable")
async def post_chargeenable(idx=0):
    lucid = await _get_api_client()
    v = lucid.vehicles[idx]
    async with request.get_data() as request_data:
        if request_data.strip() == '1':
            await lucid.start_charging(v)
        elif request_data.strip() == '0':
            await lucid.stop_charging(v)

def make_http_source(origin, suffix):
    return {'source': 'http', 'uri': f'http://{origin}/{suffix}'}


app.run(host='0.0.0.0', port=5118, use_reloader=False, )
