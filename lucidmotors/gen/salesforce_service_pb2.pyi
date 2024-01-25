from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAppointment(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSalesForceServiceAppointmentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSalesForceServiceAppointmentsResponse(_message.Message):
    __slots__ = ["status", "appointments", "comment"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPOINTMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    status: str
    appointments: _containers.RepeatedCompositeFieldContainer[ServiceAppointment]
    comment: str
    def __init__(self, status: _Optional[str] = ..., appointments: _Optional[_Iterable[_Union[ServiceAppointment, _Mapping]]] = ..., comment: _Optional[str] = ...) -> None: ...
