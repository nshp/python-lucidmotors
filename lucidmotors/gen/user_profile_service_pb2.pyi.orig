from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneNumber(_message.Message):
    __slots__ = ("type", "number")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    type: str
    number: str
    def __init__(self, type: _Optional[str] = ..., number: _Optional[str] = ...) -> None: ...

class UserProfile(_message.Message):
    __slots__ = ("first_name", "last_name", "email", "locale", "photo_url", "address", "city", "state", "postal_code", "country", "phones", "preferred_name")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_NAME_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    locale: str
    photo_url: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    phones: _containers.RepeatedCompositeFieldContainer[PhoneNumber]
    preferred_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., locale: _Optional[str] = ..., photo_url: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., postal_code: _Optional[str] = ..., country: _Optional[str] = ..., phones: _Optional[_Iterable[_Union[PhoneNumber, _Mapping]]] = ..., preferred_name: _Optional[str] = ...) -> None: ...

class GetUserProfileRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserProfileResponse(_message.Message):
    __slots__ = ("profile",)
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    profile: UserProfile
    def __init__(self, profile: _Optional[_Union[UserProfile, _Mapping]] = ...) -> None: ...

class SetUserProfileRequest(_message.Message):
    __slots__ = ("first_name", "last_name")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class SetUserProfileResponse(_message.Message):
    __slots__ = ("profile",)
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    profile: UserProfile
    def __init__(self, profile: _Optional[_Union[UserProfile, _Mapping]] = ...) -> None: ...

class UploadUserProfilePhotoRequest(_message.Message):
    __slots__ = ("photo_bytes",)
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    photo_bytes: str
    def __init__(self, photo_bytes: _Optional[str] = ...) -> None: ...

class UploadUserProfilePhotoResponse(_message.Message):
    __slots__ = ("photo_url",)
    PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    photo_url: str
    def __init__(self, photo_url: _Optional[str] = ...) -> None: ...

class ReferralHistoryApiRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReferralHistoryApiResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
