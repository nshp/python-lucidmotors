from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetEventsRequest(_message.Message):
    __slots__ = ["vehicle_id", "limit"]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    limit: int
    def __init__(self, vehicle_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class GetEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
