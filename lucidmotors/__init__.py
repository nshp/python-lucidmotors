"""The Lucid Motors mobile app API"""
from __future__ import annotations
from enum import Enum
from typing import Optional, Any
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, Field

import aiohttp
import logging

from .const import MOBILE_API
from .user import User
from .vehicle import Vehicle
from .exceptions import APIError


__version__ = "0.1.1"

_LOGGER = logging.getLogger(__name__)


async def _check_for_api_error(resp: aiohttp.ClientResponse) -> dict[str, Any]:
    """Check if an API response is an error, and if so, raise an exception"""

    reply = await resp.json()

    if resp.status != 200 or "code" in reply:
        # There is also a 'details' list, but I have not seen it populated yet.
        raise APIError(resp.status, reply.get("code", None), reply.get("message", None))

    return reply


class SessionInfo(BaseModel):
    """API login session information"""

    expiry_time: datetime = Field(alias="expiryTimeSec")
    gigya_jwt: str = Field(alias="gigyaJwt")
    id_token: str = Field(alias="idToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponse(BaseModel):
    """Response to the /login API request."""

    uid: str
    session_info: SessionInfo = Field(alias="sessionInfo")
    user_profile: User = Field(alias="userProfile")
    user_vehicle_data: list[Vehicle] = Field(alias="userVehicleData")


class GetNewJWTTokenResponse(BaseModel):
    """Response to the /get_new_jwt_token API request."""

    session_info: SessionInfo = Field(alias="sessionInfo")


class UserVehiclesResponse(BaseModel):
    """Response to the /user_vehicles API request."""

    user_vehicle_data: list[Vehicle] = Field(alias="userVehicleData")


class LightsAction(str, Enum):
    ON = 'LIGHTS_ON'
    OFF = 'LIGHTS_OFF'
    FLASH = 'LIGHTS_FLASH'


class ClosureState(str, Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class LockState(str, Enum):
    LOCKED = 'LOCKED'
    UNLOCKED = 'UNLOCKED'


class DefrostAction(str, Enum):
    ON = 'DEFROST_ON'
    OFF = 'DEFROST_OFF'


class LucidAPI:
    """A wrapper around the API used by the Lucid mobile apps"""

    _session: aiohttp.ClientSession

    # Expiration time of our current authentication token, or None if we do not
    # have a valid one yet (call .login()).
    _token_expiry_time: Optional[datetime]

    # Refresh token for our session
    _refresh_token: str

    # User profile data from most recent login request, or None if not logged
    # in yet.
    _user_profile: Optional[User]

    # List of user vehicles
    _vehicles: list[Vehicle]

    def __init__(self) -> None:
        """Initialize the API client"""

        headers = {
            "user-agent": f"python-lucidmotors/{__version__}",
        }
        self._session = aiohttp.ClientSession(MOBILE_API, headers=headers)
        self._token_expiry_time = None
        self._user_profile = None
        self._vehicles = []

    async def __aenter__(self) -> "LucidAPI":
        await self._session.__aenter__()
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self._session.__aexit__(*exc)

    def _save_session(self, sess):
        self._token_expiry_time = sess.expiry_time
        self._refresh_token = sess.refresh_token

        _LOGGER.debug(
            "API authentication succeeded. Token expires at %s (%s from now)",
            self._token_expiry_time,
            self._token_expiry_time - datetime.now(timezone.utc),
        )

        # Save authentication token in our ClientSession - it is sent as an
        # HTTP header.
        self._session.headers.update({"authorization": f"Bearer {sess.id_token}"})

    @property
    def session_time_remaining(self) -> timedelta:
        """Time remaining before our session would expire without renewal.

        Returns timedelta(0) if not logged in yet.
        """
        if self._token_expiry_time is None:
            return timedelta(0)
        now = datetime.now(timezone.utc)
        if self._token_expiry_time > now:
            return now - self._token_expiry_time
        return timedelta(0)

    async def _login_request(self, username: str, password: str) -> Any:
        """Authenticate to the API, returning the raw result."""

        # The API responds with helpful schema validation messages if these
        # fields are wrong. If the API requirements change in the future, try
        # just looking at the message it returns to see if it says something
        # like "missing required field XYZ," or "invalid value for enumerator
        # type XYZ."
        request = {
            "username": username,
            "password": password,
            # Either 1 or 2 - probably iOS or Android, but no idea which value
            # is which.
            "os": 1,
            # Again no idea what this means, but it is a required enum value. 1
            # and 2 are accepted.
            "notification_channel_type": 1,
            # Required string, not sure what it is used for exactly.
            "notification_device_token": "1234",
            # TODO: Make this configurable, assuming other values are actually
            # accepted by the API.
            "locale": "en_US",
            "device_id": "python-lucidmotors",
        }

        # The login endpoint gives us a bearer token we can use in future
        # requests. It comes with an expiration time, but there is a renewal
        # endpoint to keep the session alive. We don't need to log in again
        # unless we miss a renewal window.
        async with self._session.post("/v1/login", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /login API response: %r", raw_reply)

        return raw_reply

    async def login(self, username: str, password: str) -> None:
        """Authenticate to the API using your Lucid account credentials"""

        raw_reply = await self._login_request(username, password)

        reply = LoginResponse(**raw_reply)
        self._save_session(reply.session_info)

        self._user_profile = reply.user_profile
        self._vehicles = reply.user_vehicle_data

    async def _get_new_jwt_token_request(self, refresh_token: str) -> Any:
        """Get a fresh new token by using the refresh token, return the raw reply."""
        request = {"refresh_token": refresh_token}

        async with self._session.post("/v1/get_new_jwt_token", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /get_new_jwt_token API response: %r", raw_reply)

        return raw_reply

    async def get_new_jwt_token(self) -> None:
        """Get a fresh new token by using the refresh token."""
        raw_reply = await self._get_new_jwt_token_request(self._refresh_token)

        reply = GetNewJWTTokenResponse(**raw_reply)

        self._save_session(reply.session_info)
        assert self._token_expiry_time is not None  # always set by _save_session

        _LOGGER.debug(
            "Session refresh succeeded. New token expires at %s (%s from now)",
            self._token_expiry_time,
            self._token_expiry_time - datetime.now(timezone.utc),
        )

    async def close(self) -> None:
        """
        Close the underlying connector. Must be called to free resources if
        this object is not used as a context manager.
        """
        await self._session.close()

    @property
    def user(self) -> Optional[User]:
        """Return the logged-in user's profile information"""
        return self._user_profile

    @property
    def vehicles(self) -> list[Vehicle]:
        """
        Return a cached list of the logged-in user's Vehicles.
        Note: To get fresh vehicle information, call .fetch_vehicles()
        """
        return self._vehicles

    async def fetch_vehicles(self) -> list[Vehicle]:
        """
        Refresh the list (and status) of vehicles from the API.
        """

        async with self._session.get("/v1/user_vehicles") as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /user_vehicles API response: %r", raw_reply)

        reply = UserVehiclesResponse(**raw_reply)
        self._vehicles = reply.user_vehicle_data

        return self._vehicles

    async def wakeup_vehicle(self, vehicle: Vehicle) -> None:
        """
        Wake up a specific vehicle.
        """

        async with self._session.post(
            "/v1/wakeup", json={"vehicle_id": vehicle.vehicle_id}
        ) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /wakeup API response: %r", raw_reply)

    async def honk_horn(self, vehicle: Vehicle) -> None:
        """
        Honk the horn of a specific vehicle.
        """

        async with self._session.post(
            "/v1/honk_horn", json={"vehicle_id": vehicle.vehicle_id}
        ) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /honk_horn API response: %r", raw_reply)

    async def lights_control(self, vehicle: Vehicle, action: LightsAction) -> None:
        """
        Control the lights of a specific vehicle.
        """

        request = {
            "vehicle_id": vehicle.vehicle_id,
            "action": action,
        }

        async with self._session.post("/v1/lights_control", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /lights_control API response: %r", raw_reply)

    async def lights_on(self, vehicle: Vehicle) -> None:
        """
        Turn on the lights of a specific vehicle.
        """

        await self.lights_control(vehicle, LightsAction.ON)

    async def lights_off(self, vehicle: Vehicle) -> None:
        """
        Turn off the lights of a specific vehicle.
        """

        await self.lights_control(vehicle, LightsAction.OFF)

    async def lights_flash(self, vehicle: Vehicle) -> None:
        """
        Flash the lights of a specific vehicle.
        """

        await self.lights_control(vehicle, LightsAction.FLASH)

    async def charge_port_control(self, vehicle: Vehicle, state: ClosureState) -> None:
        """
        Control the charge port door of a specific vehicle.
        """

        request = {
            "vehicle_id": vehicle.vehicle_id,
            "closure_state": state,
        }

        async with self._session.post("/v1/charge_port_control", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /charge_port_control API response: %r", raw_reply)

    async def charge_port_open(self, vehicle: Vehicle) -> None:
        """
        Open the charge port door of a specific vehicle.
        """

        await self.charge_port_control(vehicle, ClosureState.OPEN)

    async def charge_port_close(self, vehicle: Vehicle) -> None:
        """
        Close the charge port door of a specific vehicle.
        """

        await self.charge_port_control(vehicle, ClosureState.CLOSED)

    async def door_locks_control(
        self, vehicle: Vehicle, state: LockState, doors: list[int] = list(range(1, 5))
    ) -> None:
        """
        Control the charge port door of a specific vehicle.
        """

        request = {
            "vehicle_id": vehicle.vehicle_id,
            "lock_state": state,
            "door_location": doors,
        }

        async with self._session.post("/v1/door_locks_control", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /door_locks_control API response: %r", raw_reply)

    async def doors_unlock(
        self, vehicle: Vehicle, doors: list[int] = list(range(1, 5))
    ) -> None:
        """
        Open the doors of a specific vehicle.
        """

        await self.door_locks_control(vehicle, LockState.UNLOCKED, doors)

    async def doors_lock(
        self, vehicle: Vehicle, doors: list[int] = list(range(1, 5))
    ) -> None:
        """
        Close the doors of a specific vehicle.
        """

        await self.door_locks_control(vehicle, LockState.LOCKED, doors)

    async def frunk_control(self, vehicle: Vehicle, state: ClosureState) -> None:
        """
        Control the charge port door of a specific vehicle.
        """

        request = {
            "vehicle_id": vehicle.vehicle_id,
            "closure_state": state,
        }

        async with self._session.post("/v1/front_cargo_control", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /front_cargo_control API response: %r", raw_reply)

    async def frunk_open(self, vehicle: Vehicle) -> None:
        """
        Open the charge port door of a specific vehicle.
        """

        await self.frunk_control(vehicle, ClosureState.OPEN)

    async def frunk_close(self, vehicle: Vehicle) -> None:
        """
        Close the charge port door of a specific vehicle.
        """

        await self.frunk_control(vehicle, ClosureState.CLOSED)

    async def trunk_control(self, vehicle: Vehicle, state: ClosureState) -> None:
        """
        Control the charge port door of a specific vehicle.
        """

        request = {
            "vehicle_id": vehicle.vehicle_id,
            "closure_state": state,
        }

        async with self._session.post("/v1/rear_cargo_control", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /rear_cargo_control API response: %r", raw_reply)

    async def trunk_open(self, vehicle: Vehicle) -> None:
        """
        Open the charge port door of a specific vehicle.
        """

        await self.trunk_control(vehicle, ClosureState.OPEN)

    async def trunk_close(self, vehicle: Vehicle) -> None:
        """
        Close the charge port door of a specific vehicle.
        """

        await self.trunk_control(vehicle, ClosureState.CLOSED)

    async def defrost_control(self, vehicle: Vehicle, action: DefrostAction) -> None:
        """
        Control the defrost mode of a specific vehicle.
        """

        request = {
            "vehicle_id": vehicle.vehicle_id,
            "hvac_defrost": action,
        }

        async with self._session.post("/v1/defrost_control", json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug("Raw /defrost_control API response: %r", raw_reply)

    async def defrost_on(self, vehicle: Vehicle) -> None:
        """
        Turn on the defrost mode of a specific vehicle.
        """

        await self.defrost_control(vehicle, DefrostAction.ON)

    async def defrost_off(self, vehicle: Vehicle) -> None:
        """
        Turn off the defrost mode of a specific vehicle.
        """

        await self.defrost_control(vehicle, DefrostAction.OFF)
