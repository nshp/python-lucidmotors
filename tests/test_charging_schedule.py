"""get_charging_schedule and set_charging_schedule build the requests the proto defines."""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import grpc
import pytest
from grpc import StatusCode

import lucidmotors
from lucidmotors.gen import vehicle_state_service_pb2 as vss


class _RpcError(grpc.aio.AioRpcError):
    def __init__(self, code):
        super().__init__(
            code,
            grpc.aio.Metadata(),
            grpc.aio.Metadata(),
            details="",
            debug_error_string="",
        )


def _api(awake=True):
    api = lucidmotors.LucidAPI.__new__(lucidmotors.LucidAPI)
    api._auto_wake = True
    api._vehicle_service = MagicMock()
    api._vehicle_service.GetVehicleState = AsyncMock()
    api._vehicle_service.UpdateChargingSchedule = AsyncMock(
        return_value=vss.UpdateChargingScheduleResponse()
    )
    api._vehicle_service.WakeupVehicle = AsyncMock()
    vehicle = vss.Vehicle(vehicle_id="v1")
    vehicle.state.power = (
        vss.PowerState.POWER_STATE_DRIVE if awake else vss.PowerState.POWER_STATE_SLEEP
    )
    return api, vehicle


def test_get_returns_the_schedule_from_the_state_reply():
    api, vehicle = _api()
    api._vehicle_service.GetVehicleState.return_value = vss.GetVehicleStateResponse(
        vehicle_id="v1",
        charging_schedule=vss.ChargingSchedule(
            schedule_on=True,
            start_time="23:00",
            end_time="06:00",
            weekday_on=True,
            charging_available=True,
        ),
    )
    got = asyncio.run(api.get_charging_schedule(vehicle))
    request = api._vehicle_service.GetVehicleState.await_args.args[0]
    assert request.vehicle_id == "v1"
    assert (got.schedule_on, got.start_time, got.end_time) == (True, "23:00", "06:00")
    assert got.weekday_on and got.charging_available


def test_set_sends_every_field():
    api, vehicle = _api()
    asyncio.run(
        api.set_charging_schedule(vehicle, True, "23:00", "06:00", weekday_on=True)
    )
    request = api._vehicle_service.UpdateChargingSchedule.await_args.args[0]
    assert request == vss.UpdateChargingScheduleRequest(
        schedule_on=True,
        start_time="23:00",
        end_time="06:00",
        weekday_on=True,
        vehicle_id="v1",
    )
    api._vehicle_service.WakeupVehicle.assert_not_awaited()


def test_set_defaults_weekday_off():
    api, vehicle = _api()
    asyncio.run(api.set_charging_schedule(vehicle, False, "00:00", "00:00"))
    request = api._vehicle_service.UpdateChargingSchedule.await_args.args[0]
    assert request.weekday_on is False and request.schedule_on is False


def test_set_wakes_a_sleeping_car_first():
    api, vehicle = _api(awake=False)
    asyncio.run(api.set_charging_schedule(vehicle, True, "23:00", "06:00"))
    api._vehicle_service.WakeupVehicle.assert_awaited_once()
    api._vehicle_service.UpdateChargingSchedule.assert_awaited_once()


def test_errors_become_api_errors():
    api, vehicle = _api()
    api._vehicle_service.UpdateChargingSchedule.side_effect = _RpcError(
        StatusCode.UNAVAILABLE
    )
    with pytest.raises(lucidmotors.exceptions.APIError):
        asyncio.run(api.set_charging_schedule(vehicle, True, "23:00", "06:00"))
    api._vehicle_service.GetVehicleState.side_effect = _RpcError(StatusCode.UNAVAILABLE)
    with pytest.raises(lucidmotors.exceptions.APIError):
        asyncio.run(api.get_charging_schedule(vehicle))
