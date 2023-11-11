"""The Lucid Motors mobile app API"""
from __future__ import annotations
from enum import Enum, auto
from typing import Optional, Any, TypeVar
from dataclasses import dataclass
from datetime import datetime
from aiohttp import ClientConnectionError
from pydantic import BaseModel, Field

import asyncio
import aiohttp
import logging
import importlib.metadata

from .const import MOBILE_API
from .user import User
from .vehicle import Vehicle
from .exceptions import APIError


__version__ = '0.1.0'

_LOGGER = logging.getLogger(__name__)

async def _check_for_api_error(resp: aiohttp.ClientResponse) -> dict[str, Any]:
    """Check if an API response is an error, and if so, raise an exception"""

    reply = await resp.json()

    if resp.status != 200 or 'code' in reply:
        # There is also a 'details' list, but I have not seen it populated yet.
        raise APIError(resp.status,
                       reply.get('code', None),
                       reply.get('message', None))

    return reply


class SessionInfo(BaseModel):
    """API login session information"""

    expiry_time_sec: int = Field(alias='expiryTimeSec')
    gigya_jwt: str = Field(alias='gigyaJwt')
    id_token: str = Field(alias='idToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginResponse(BaseModel):
    """Response to the /login API request."""

    uid: str
    session_info: SessionInfo = Field(alias='sessionInfo')
    user_profile: User = Field(alias='userProfile')
    user_vehicle_data: list[Vehicle] = Field(alias='userVehicleData')


class UserVehiclesResponse(BaseModel):
    """Response to the /user_vehicles API request."""

    user_vehicle_data: list[Vehicle] = Field(alias='userVehicleData')


class LucidAPI:
    """A wrapper around the API used by the Lucid mobile apps"""

    _session: aiohttp.ClientSession

    # Expiration time of our current authentication token, or None if we do not
    # have a valid one yet (call .login()).
    # NOTE: I am not sure what timezone this is bound to - we don't tell the
    # API and it doesn't tell us. Is it bound to the timezone where the vehicle
    # was last located or something? This might actually matter if time jumps
    # around as the vehicle drives between timezones?
    _token_expiry_time: Optional[datetime]

    # User profile data from most recent login request, or None if not logged
    # in yet.
    _user_profile: Optional[User]

    # List of user vehicles
    _vehicles: list[Vehicle]

    def __init__(self) -> None:
        """Initialize the API client"""

        headers = {
            'user-agent': f'python-lucidmotors/{__version__}',
        }
        self._session = aiohttp.ClientSession(MOBILE_API, headers=headers)
        self._token_expiry_time = None
        self._user_profile = None
        self._vehicles = []


    async def __aenter__(self) -> 'LucidAPI':
        await self._session.__aenter__()
        return self


    async def __aexit__(self, *exc: Any) -> None:
        await self._session.__aexit__(*exc)


    async def login(self, username: str, password: str) -> None:
        """Authenticate to the API using your Lucid account credentials"""

        # The API responds with helpful schema validation messages if these
        # fields are wrong. If the API requirements change in the future, try
        # just looking at the message it returns to see if it says something
        # like "missing required field XYZ," or "invalid value for enumerator
        # type XYZ."
        request = {
            'username': username,
            'password': password,
            # This is some sort of enum - probably iOS or Android, but no idea
            # which value is which.
            'os': 1,
            # Again no idea what this means, but it is a required enum value
            # and cannot be 0.
            'notification_channel_type': 1,
            # Ditto. Required string, not sure what it is used for exactly.
            'notification_device_token': '1234',
            # TODO: Make this configurable, assuming other values are actually
            # accepted by the API.
            'locale': 'en_US',
        }

        # The login endpoint gives us a bearer token we can use in future
        # requests. It comes with an expiration time, but there is a renewal
        # endpoint to keep the session alive. We don't need to log in again
        # unless we miss a renewal window.
        async with self._session.post('/v1/login', json=request) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug('Raw /login API response: %r', raw_reply)

        reply = LoginResponse.model_validate(raw_reply)
        sess = reply.session_info

        self._token_expiry_time = datetime.fromtimestamp(sess.expiry_time_sec)

        _LOGGER.debug('API authentication succeeded. Token expires at %s',
                      self._token_expiry_time)

        # Save authentication token in our ClientSession - it is sent as an HTTP header.
        self._session.headers.update({'authorization': f'Bearer {sess.id_token}'})

        self._user_profile = reply.user_profile
        self._vehicles = reply.user_vehicle_data


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

        async with self._session.get('/v1/user_vehicles') as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug('Raw /user_vehicles API response: %r', raw_reply)

        reply = UserVehiclesResponse.model_validate(raw_reply)
        self._vehicles = reply.user_vehicle_data

        return self._vehicles


    async def wakeup_vehicle(self, vehicle: Vehicle) -> None:
        """
        Wake up a specific vehicle.
        """

        async with self._session.post('/v1/wakeup', json={'vehicle_id': vehicle.vehicle_id}) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug('Raw /wakeup API response: %r', raw_reply)


    async def honk_horn(self, vehicle: Vehicle) -> None:
        """
        Honk the horn of a specific vehicle.
        """

        async with self._session.post('/v1/honk_horn', json={'vehicle_id': vehicle.vehicle_id}) as resp:
            raw_reply = await _check_for_api_error(resp)

        _LOGGER.debug('Raw /honk_horn API response: %r', raw_reply)