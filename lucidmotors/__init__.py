"""The Lucid Motors mobile app API"""
from __future__ import annotations
from typing import Optional, Any, Callable, TypeVar, Awaitable
from datetime import datetime, timezone, timedelta
from grpc.aio import ClientCallDetails, UnaryUnaryCall

import uuid
import grpc
import grpc.aio
import logging

from .const import MOBILE_API
from .exceptions import APIError

from .gen import (
    login_session_pb2,
    login_session_pb2_grpc,
    trip_service_pb2,
    trip_service_pb2_grpc,
    vehicle_state_service_pb2,
    vehicle_state_service_pb2_grpc,
    charging_service_pb2,
    charging_service_pb2_grpc,
)
from .gen.login_session_pb2 import NotificationChannelType
from .gen.user_profile_service_pb2 import UserProfile
from .gen.vehicle_state_service_pb2 import (
    Vehicle,
    LightAction,
    DoorState,
    DefrostState,
    LockState,
    HvacPower,
)


__version__ = "1.0.0"

_LOGGER = logging.getLogger(__name__)


T = TypeVar('T')


async def _check_for_api_error(coroutine: Awaitable[T]) -> T:
    try:
        return await coroutine
    except grpc.aio.AioRpcError as exc:
        raise APIError(exc.code(), exc.details(), exc.debug_error_string()) from None


class LucidAPIInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    """RPC interceptor adding token-based authentication."""

    # RPC call credentials (includes session token)
    _credentials: Optional[grpc.CallCredentials] = None

    def set_credentials(self, credentials: Optional[grpc.CallCredentials]) -> None:
        """Set (or clear) the gRPC credentials used for this channel."""
        self._credentials = credentials

    async def intercept_unary_unary(
        self,
        continuation: Callable[[ClientCallDetails, None], UnaryUnaryCall],
        client_call_details: ClientCallDetails,
        request: None,
    ) -> UnaryUnaryCall | None:
        """Intercept a unary-unary invocation asynchronously."""

        client_call_details = ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            client_call_details.metadata,
            self._credentials,
            client_call_details.wait_for_ready,
        )

        response = await continuation(client_call_details, request)

        return response


class LucidAPI:
    """A wrapper around the API used by the Lucid mobile apps"""

    # API RPC channel
    _channel: grpc.aio.Channel

    # Expiration time of our current authentication token, or None if we do not
    # have a valid one yet (call .login()).
    _token_expiry_time: Optional[datetime]

    # Refresh token for our session
    _refresh_token: Optional[str]

    # User profile data from most recent login request, or None if not logged
    # in yet.
    _user_profile: Optional[UserProfile]

    # List of user vehicles
    _vehicles: list[Vehicle]

    # RPC call interceptor
    _interceptor: LucidAPIInterceptor

    # Service stubs generated from the gRPC Service definitions
    _login_service: login_session_pb2_grpc.LoginSessionStub
    _trip_service: trip_service_pb2_grpc.TripServiceStub
    _vehicle_service: vehicle_state_service_pb2_grpc.VehicleStateServiceStub
    _charging_service: charging_service_pb2_grpc.ChargingServiceStub

    def __init__(self) -> None:
        """Initialize the API client"""

        # We start with a channel secured with "SSL credentials," i.e. normal
        # SSL/TLS certificate verification. Once we log in we can upgrade to
        # "token" credentials to keep an authenticated session.
        ssl_creds = grpc.ssl_channel_credentials()
        self._interceptor = LucidAPIInterceptor()
        # Typing ignored due to "_PartialStubMustCastOrIgnore" insanity in
        # grpc-stubs package.
        self._channel = grpc.aio.secure_channel(
            MOBILE_API,
            credentials=ssl_creds,
            interceptors=[self._interceptor],  # type: ignore
        )
        self._login_service = login_session_pb2_grpc.LoginSessionStub(self._channel)
        self._trip_service = trip_service_pb2_grpc.TripServiceStub(self._channel)
        self._vehicle_service = vehicle_state_service_pb2_grpc.VehicleStateServiceStub(
            self._channel
        )
        self._charging_service = charging_service_pb2_grpc.ChargingServiceStub(
            self._channel
        )
        self._refresh_token = None
        self._token_expiry_time = None
        self._user_profile = None
        self._vehicles = []

    async def __aenter__(self) -> "LucidAPI":
        await self._channel.__aenter__()
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self._channel.__aexit__(*exc)

    def _save_session(self, sess: login_session_pb2.SessionInfo) -> None:
        self._token_expiry_time = datetime.fromtimestamp(
            sess.expiry_time_sec, timezone.utc
        )
        self._refresh_token = sess.refresh_token

        _LOGGER.debug(
            "API authentication succeeded. Token expires at %s (%s from now)",
            self._token_expiry_time,
            self._token_expiry_time - datetime.now(timezone.utc),
        )

        creds = grpc.access_token_call_credentials(sess.id_token)
        self._interceptor.set_credentials(creds)

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

    async def login(self, username: str, password: str) -> None:
        """Authenticate to the API using your Lucid account credentials"""

        # Lucid wants some sort of unique device ID. UUID provides a
        # cross-platform way of getting a relatively unique device ID.
        device_id = f'{uuid.getnode():x}'

        # The API responds with helpful schema validation messages if these
        # fields are wrong. If the API requirements change in the future, try
        # just looking at the message it returns to see if it says something
        # like "missing required field XYZ," or "invalid value for enumerator
        # type XYZ."
        request = login_session_pb2.LoginRequest(
            username=username,
            password=password,
            notification_channel_type=NotificationChannelType.NOTIFICATION_CHANNEL_ONE,
            notification_device_token=device_id,
            os=login_session_pb2.Os.OS_IOS,
            locale='en_US',
            client_name=f'python-lucidmotors/{__version__}',
            device_id=device_id,
        )

        # The login endpoint gives us a bearer token we can use in future
        # requests. It comes with an expiration time, but there is a renewal
        # endpoint to keep the session alive. We don't need to log in again
        # unless we miss a renewal window.
        reply = await _check_for_api_error(self._login_service.Login(request))

        self._save_session(reply.session_info)

        self._user_profile = reply.user_profile
        self._vehicles = reply.user_vehicle_data

    async def get_new_jwt_token(self) -> None:
        """Get a fresh new token by using the refresh token."""
        request = login_session_pb2.GetNewJWTTokenRequest(
            refresh_token=self._refresh_token
        )
        reply = await _check_for_api_error(self._login_service.GetNewJWTToken(request))

        self._save_session(reply.session_info)
        assert self._token_expiry_time is not None  # always set by _save_session

        _LOGGER.debug(
            "Session refresh succeeded. New token expires at %s (%s from now)",
            self._token_expiry_time,
            self._token_expiry_time - datetime.now(timezone.utc),
        )

    async def close(self) -> None:
        """
        Close the underlying channel. Must be called to free resources if
        this object is not used as a context manager.
        """
        await self._channel.close(None)

    @property
    def user(self) -> Optional[UserProfile]:
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

        request = login_session_pb2.GetUserVehiclesRequest()
        reply = await _check_for_api_error(self._login_service.GetUserVehicles(request))
        self._vehicles = reply.user_vehicle_data

        return self._vehicles

    async def wakeup_vehicle(self, vehicle: Vehicle) -> None:
        """
        Wake up a specific vehicle.
        """

        request = vehicle_state_service_pb2.WakeupVehicleRequest(
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.WakeupVehicle(request))

    async def honk_horn(self, vehicle: Vehicle) -> None:
        """
        Honk the horn of a specific vehicle.
        """

        request = vehicle_state_service_pb2.HonkHornRequest(
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.HonkHorn(request))

    async def lights_control(self, vehicle: Vehicle, action: LightAction) -> None:
        """
        Control the lights of a specific vehicle.
        """

        request = vehicle_state_service_pb2.HonkHornRequest(
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.HonkHorn(request))

    async def lights_on(self, vehicle: Vehicle) -> None:
        """
        Turn on the lights of a specific vehicle.
        """

        await self.lights_control(vehicle, LightAction.LIGHT_ACTION_ON)

    async def lights_off(self, vehicle: Vehicle) -> None:
        """
        Turn off the lights of a specific vehicle.
        """

        await self.lights_control(vehicle, LightAction.LIGHT_ACTION_OFF)

    async def lights_flash(self, vehicle: Vehicle) -> None:
        """
        Flash the lights of a specific vehicle.
        """

        await self.lights_control(vehicle, LightAction.LIGHT_ACTION_FLASH)

    async def charge_port_control(self, vehicle: Vehicle, state: DoorState) -> None:
        """
        Control the charge port door of a specific vehicle.
        """

        request = vehicle_state_service_pb2.ControlChargePortRequest(
            closure_state=state,
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.ControlChargePort(request))

    async def charge_port_open(self, vehicle: Vehicle) -> None:
        """
        Open the charge port door of a specific vehicle.
        """

        await self.charge_port_control(vehicle, DoorState.DOOR_STATE_OPEN)

    async def charge_port_close(self, vehicle: Vehicle) -> None:
        """
        Close the charge port door of a specific vehicle.
        """

        await self.charge_port_control(vehicle, DoorState.DOOR_STATE_CLOSED)

    async def door_locks_control(
        self, vehicle: Vehicle, state: LockState, doors: list[int] = list(range(1, 5))
    ) -> None:
        """
        Control the doors of a specific vehicle.
        """

        request = vehicle_state_service_pb2.DoorLocksControlRequest(
            door_location=doors,
            lock_state=state,
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.DoorLocksControl(request))

    async def doors_unlock(
        self, vehicle: Vehicle, doors: list[int] = list(range(1, 5))
    ) -> None:
        """
        Open the doors of a specific vehicle.
        """

        await self.door_locks_control(vehicle, LockState.LOCK_STATE_UNLOCKED, doors)

    async def doors_lock(
        self, vehicle: Vehicle, doors: list[int] = list(range(1, 5))
    ) -> None:
        """
        Close the doors of a specific vehicle.
        """

        await self.door_locks_control(vehicle, LockState.LOCK_STATE_LOCKED, doors)

    async def frunk_control(self, vehicle: Vehicle, state: DoorState) -> None:
        """
        Control the frunk door of a specific vehicle.
        """

        request = vehicle_state_service_pb2.FrontCargoControlRequest(
            closure_state=state,
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.FrontCargoControl(request))

    async def frunk_open(self, vehicle: Vehicle) -> None:
        """
        Open the frunk door of a specific vehicle.
        """

        await self.frunk_control(vehicle, DoorState.DOOR_STATE_OPEN)

    async def frunk_close(self, vehicle: Vehicle) -> None:
        """
        Close the frunk door of a specific vehicle.
        """

        await self.frunk_control(vehicle, DoorState.DOOR_STATE_CLOSED)

    async def trunk_control(self, vehicle: Vehicle, state: DoorState) -> None:
        """
        Control the trunk door of a specific vehicle.
        """

        request = vehicle_state_service_pb2.RearCargoControlRequest(
            closure_state=state,
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.RearCargoControl(request))

    async def trunk_open(self, vehicle: Vehicle) -> None:
        """
        Open the trunk door of a specific vehicle.
        """

        await self.trunk_control(vehicle, DoorState.DOOR_STATE_OPEN)

    async def trunk_close(self, vehicle: Vehicle) -> None:
        """
        Close the trunk door of a specific vehicle.
        """

        await self.trunk_control(vehicle, DoorState.DOOR_STATE_CLOSED)

    async def defrost_control(self, vehicle: Vehicle, action: DefrostState) -> None:
        """
        Control the defrost mode of a specific vehicle.
        """

        request = vehicle_state_service_pb2.HvacDefrostControlRequest(
            hvac_defrost=action,
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.HvacDefrostControl(request))

    async def defrost_on(self, vehicle: Vehicle) -> None:
        """
        Turn on the defrost mode of a specific vehicle.
        """

        await self.defrost_control(vehicle, DefrostState.DEFROST_ON)

    async def defrost_off(self, vehicle: Vehicle) -> None:
        """
        Turn off the defrost mode of a specific vehicle.
        """

        await self.defrost_control(vehicle, DefrostState.DEFROST_OFF)

    async def set_cabin_temperature(
        self, vehicle: Vehicle, temperature: Optional[float]
    ) -> None:
        """
        Set cabin temperature (in celcius) for preconditioning.
        Disables preconditioning if temperature is None.
        """

        if temperature is None:
            power = HvacPower.HVAC_OFF
            temperature = 0.0
        else:
            power = HvacPower.HVAC_PRECONDITION

        request = vehicle_state_service_pb2.SetCabinTemperatureRequest(
            temperature=temperature,
            state=power,
            vehicle_id=vehicle.vehicle_id,
        )
        await _check_for_api_error(self._vehicle_service.SetCabinTemperature(request))
