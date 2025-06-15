from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WaypointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WAYPOINT_TYPE_UNKNOWN: _ClassVar[WaypointType]
    WAYPOINT_TYPE_WAYPOINT: _ClassVar[WaypointType]
    WAYPOINT_TYPE_EV_CHARGER: _ClassVar[WaypointType]
WAYPOINT_TYPE_UNKNOWN: WaypointType
WAYPOINT_TYPE_WAYPOINT: WaypointType
WAYPOINT_TYPE_EV_CHARGER: WaypointType

class Waypoint(_message.Message):
    __slots__ = ("latitude", "longitude", "address", "waypoint_name", "waypoint_type", "arrival_charge_percent", "departure_charge_percent", "charge_duration_secs")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_CHARGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_CHARGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CHARGE_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    address: str
    waypoint_name: str
    waypoint_type: WaypointType
    arrival_charge_percent: float
    departure_charge_percent: float
    charge_duration_secs: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., address: _Optional[str] = ..., waypoint_name: _Optional[str] = ..., waypoint_type: _Optional[_Union[WaypointType, str]] = ..., arrival_charge_percent: _Optional[float] = ..., departure_charge_percent: _Optional[float] = ..., charge_duration_secs: _Optional[int] = ...) -> None: ...

class Trip(_message.Message):
    __slots__ = ("trip_id", "destination_name", "distance_meters", "elapsed_time_sec", "charging_stops", "created_time_ms", "waypoints", "sender")
    TRIP_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    CHARGING_STOPS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    trip_id: str
    destination_name: str
    distance_meters: int
    elapsed_time_sec: int
    charging_stops: int
    created_time_ms: int
    waypoints: _containers.RepeatedCompositeFieldContainer[Waypoint]
    sender: str
    def __init__(self, trip_id: _Optional[str] = ..., destination_name: _Optional[str] = ..., distance_meters: _Optional[int] = ..., elapsed_time_sec: _Optional[int] = ..., charging_stops: _Optional[int] = ..., created_time_ms: _Optional[int] = ..., waypoints: _Optional[_Iterable[_Union[Waypoint, _Mapping]]] = ..., sender: _Optional[str] = ...) -> None: ...

class ShareTripRequest(_message.Message):
    __slots__ = ("trip", "vehicle_id")
    TRIP_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    trip: Trip
    vehicle_id: str
    def __init__(self, trip: _Optional[_Union[Trip, _Mapping]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class ShareTripResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
