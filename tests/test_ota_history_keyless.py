"""ota_version_history drops the build name; keyless driving sends the right action."""

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

import lucidmotors
from lucidmotors import OtaVersion
from lucidmotors.gen import vehicle_state_service_pb2 as pb

VIN = "FAKEVIN0000000001"


def _api(**rpcs):
    api = lucidmotors.LucidAPI.__new__(lucidmotors.LucidAPI)
    api._auto_wake = False
    api._vehicle_service = MagicMock(
        **{k: AsyncMock(return_value=v) for k, v in rpcs.items()}
    )
    return api


def _vehicle():
    vehicle = pb.Vehicle(vehicle_id="vehicle-alpha")
    vehicle.config.vin = VIN
    return vehicle


def _reply(*rows):
    reply = pb.GetOtaVersionHistoryResponse()
    for version, name, stamp in rows:
        reply.values.add(version=version, name=name, updateTime=stamp)
    return reply


def test_history_is_parsed_sorted_and_nameless():
    reply = _reply(
        ("3.1.51", "build-FAKEVIN0000000002", "2025-12-19T10:00:00"),
        ("2.0.10", "build-FAKEVIN0000000003", "2025-06-01T08:30:00Z"),
        ("", "no-version", "2025-07-01T00:00:00"),
        ("9.9.9", "bad-time", "not a time"),
    )
    api = _api(GetOtaVersionHistory=reply)
    history = asyncio.run(api.ota_version_history(_vehicle()))
    assert history == [
        OtaVersion("2.0.10", datetime(2025, 6, 1, 8, 30, tzinfo=timezone.utc)),
        OtaVersion("3.1.51", datetime(2025, 12, 19, 10, 0, tzinfo=timezone.utc)),
    ]
    assert not any("build" in repr(entry) for entry in history)
    request = api._vehicle_service.GetOtaVersionHistory.call_args.args[0]
    assert (request.vin, request.offset, request.limit) == (VIN, 0, 100)


def test_keyless_driving_on_and_off():
    api = _api(KeylessDrivingAction=pb.KeylessDrivingActionResponse())
    asyncio.run(api.keyless_driving_on(_vehicle()))
    asyncio.run(api.keyless_driving_off(_vehicle()))
    calls = api._vehicle_service.KeylessDrivingAction.call_args_list
    assert [c.args[0].action for c in calls] == [
        pb.KeylessDrivingState.KEYLESS_DRIVING_ON,
        pb.KeylessDrivingState.KEYLESS_DRIVING_OFF,
    ]
    assert all(c.args[0].vehicle_id == "vehicle-alpha" for c in calls)
