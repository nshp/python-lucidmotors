from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_TYPE_UNDEFINED: _ClassVar[EventType]
    EVENT_TYPE_COLLISION: _ClassVar[EventType]
    EVENT_TYPE_BREAKIN: _ClassVar[EventType]
    EVENT_TYPE_TOWING: _ClassVar[EventType]

class EventThreatLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_THREAT_LEVEL_UNDEFINED: _ClassVar[EventThreatLevel]
    EVENT_THREAT_LEVEL_1: _ClassVar[EventThreatLevel]
    EVENT_THREAT_LEVEL_2: _ClassVar[EventThreatLevel]
    EVENT_THREAT_LEVEL_3: _ClassVar[EventThreatLevel]

class MediaFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_FORMAT_UNDEFINED: _ClassVar[MediaFormat]
    MEDIA_FORMAT_JPEG: _ClassVar[MediaFormat]

class MediaSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_SOURCE_UNDEFINED: _ClassVar[MediaSource]
    MEDIA_SOURCE_FRONT_LEFT_CAMERA: _ClassVar[MediaSource]
    MEDIA_SOURCE_FRONT_RIGHT_CAMERA: _ClassVar[MediaSource]
    MEDIA_SOURCE_REAR_LEFT_CAMERA: _ClassVar[MediaSource]
    MEDIA_SOURCE_REAR_RIGHT_CAMERA: _ClassVar[MediaSource]
    MEDIA_SOURCE_INTERIOR_CAMERA: _ClassVar[MediaSource]

class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TYPE_UNDEFINED: _ClassVar[MediaType]
    MEDIA_TYPE_IMAGE: _ClassVar[MediaType]

class SentryModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SENTRY_MODE_STATE_UNKNOWN: _ClassVar[SentryModeState]
    SENTRY_MODE_ENABLED: _ClassVar[SentryModeState]
    SENTRY_MODE_DISABLED: _ClassVar[SentryModeState]
EVENT_TYPE_UNDEFINED: EventType
EVENT_TYPE_COLLISION: EventType
EVENT_TYPE_BREAKIN: EventType
EVENT_TYPE_TOWING: EventType
EVENT_THREAT_LEVEL_UNDEFINED: EventThreatLevel
EVENT_THREAT_LEVEL_1: EventThreatLevel
EVENT_THREAT_LEVEL_2: EventThreatLevel
EVENT_THREAT_LEVEL_3: EventThreatLevel
MEDIA_FORMAT_UNDEFINED: MediaFormat
MEDIA_FORMAT_JPEG: MediaFormat
MEDIA_SOURCE_UNDEFINED: MediaSource
MEDIA_SOURCE_FRONT_LEFT_CAMERA: MediaSource
MEDIA_SOURCE_FRONT_RIGHT_CAMERA: MediaSource
MEDIA_SOURCE_REAR_LEFT_CAMERA: MediaSource
MEDIA_SOURCE_REAR_RIGHT_CAMERA: MediaSource
MEDIA_SOURCE_INTERIOR_CAMERA: MediaSource
MEDIA_TYPE_UNDEFINED: MediaType
MEDIA_TYPE_IMAGE: MediaType
SENTRY_MODE_STATE_UNKNOWN: SentryModeState
SENTRY_MODE_ENABLED: SentryModeState
SENTRY_MODE_DISABLED: SentryModeState

class EventGeoLocation(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class MediaInfo(_message.Message):
    __slots__ = ("name", "media_size", "media_format", "media_source", "md5_checksum")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEDIA_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MD5_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    name: str
    media_size: int
    media_format: MediaFormat
    media_source: MediaSource
    md5_checksum: str
    def __init__(self, name: _Optional[str] = ..., media_size: _Optional[int] = ..., media_format: _Optional[_Union[MediaFormat, str]] = ..., media_source: _Optional[_Union[MediaSource, str]] = ..., md5_checksum: _Optional[str] = ...) -> None: ...

class Media(_message.Message):
    __slots__ = ("media_info", "media_type", "media_download_url")
    MEDIA_INFO_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    media_info: MediaInfo
    media_type: MediaType
    media_download_url: str
    def __init__(self, media_info: _Optional[_Union[MediaInfo, _Mapping]] = ..., media_type: _Optional[_Union[MediaType, str]] = ..., media_download_url: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("event_id", "vehicle_id", "hmi_event_id", "primary_user_id", "event_geo_location", "event_threat_level", "event_type", "recorded_at", "media_list")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    HMI_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_GEO_LOCATION_FIELD_NUMBER: _ClassVar[int]
    EVENT_THREAT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_LIST_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    vehicle_id: str
    hmi_event_id: str
    primary_user_id: str
    event_geo_location: EventGeoLocation
    event_threat_level: EventThreatLevel
    event_type: EventType
    recorded_at: _timestamp_pb2.Timestamp
    media_list: _containers.RepeatedCompositeFieldContainer[Media]
    def __init__(self, event_id: _Optional[str] = ..., vehicle_id: _Optional[str] = ..., hmi_event_id: _Optional[str] = ..., primary_user_id: _Optional[str] = ..., event_geo_location: _Optional[_Union[EventGeoLocation, _Mapping]] = ..., event_threat_level: _Optional[_Union[EventThreatLevel, str]] = ..., event_type: _Optional[_Union[EventType, str]] = ..., recorded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., media_list: _Optional[_Iterable[_Union[Media, _Mapping]]] = ...) -> None: ...

class GetEventRequest(_message.Message):
    __slots__ = ("event_id",)
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    def __init__(self, event_id: _Optional[str] = ...) -> None: ...

class GetEventResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: Event
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class GetEventsRequest(_message.Message):
    __slots__ = ("vehicle_id", "offset", "limit", "start_time_utc", "end_time_utc")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_UTC_FIELD_NUMBER: _ClassVar[int]
    END_TIME_UTC_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    offset: int
    limit: int
    start_time_utc: _timestamp_pb2.Timestamp
    end_time_utc: _timestamp_pb2.Timestamp
    def __init__(self, vehicle_id: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., start_time_utc: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time_utc: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetEventsResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class SetSentryModeRequest(_message.Message):
    __slots__ = ("vehicle_id", "state")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    state: SentryModeState
    def __init__(self, vehicle_id: _Optional[str] = ..., state: _Optional[_Union[SentryModeState, str]] = ...) -> None: ...

class SetSentryModeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetEnhancedDeterrenceRequest(_message.Message):
    __slots__ = ("vehicle_id", "state")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    state: SentryModeState
    def __init__(self, vehicle_id: _Optional[str] = ..., state: _Optional[_Union[SentryModeState, str]] = ...) -> None: ...

class SetEnhancedDeterrenceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetSentryModeAtHomeRequest(_message.Message):
    __slots__ = ("vehicle_id", "state")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    state: SentryModeState
    def __init__(self, vehicle_id: _Optional[str] = ..., state: _Optional[_Union[SentryModeState, str]] = ...) -> None: ...

class SetSentryModeAtHomeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetSentryModeAtWorkRequest(_message.Message):
    __slots__ = ("vehicle_id", "state")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    state: SentryModeState
    def __init__(self, vehicle_id: _Optional[str] = ..., state: _Optional[_Union[SentryModeState, str]] = ...) -> None: ...

class SetSentryModeAtWorkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TurnOffSentryAlarmRequest(_message.Message):
    __slots__ = ("vehicle_id",)
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    def __init__(self, vehicle_id: _Optional[str] = ...) -> None: ...

class TurnOffSentryAlarmResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
