from . import user_profile_service_pb2 as _user_profile_service_pb2
from . import vehicle_state_service_pb2 as _vehicle_state_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CHANNEL_UNKNOWN: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_FIREBASE: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_BAIDU: _ClassVar[NotificationChannelType]

class Os(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OS_UNKNOWN: _ClassVar[Os]
    OS_IOS: _ClassVar[Os]
    OS_ANDROID: _ClassVar[Os]

class NotificationCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CATEGORY_UNKNOWN: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_CHARGE: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_SECURITY: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_SOFTWARE: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_HVAC: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_REQUIRED: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_CDR_EMAIL: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_SUBSCRIPTION: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_REFERRAL_CAMPAIGN: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_RECALL_CAMPAIGN: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_CLOSURE: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_ACCESSORIES: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_USER_PROFILE: _ClassVar[NotificationCategory]
    NOTIFICATION_CATEGORY_TIRE_PRESSURE: _ClassVar[NotificationCategory]

class Encryption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_UNKNOWN: _ClassVar[Encryption]
    ENCRYPTION_SINGLE: _ClassVar[Encryption]
    ENCRYPTION_MUTUAL: _ClassVar[Encryption]

class ResetPinStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESET_PIN_STATUS_UNKNOWN: _ClassVar[ResetPinStatus]
    RESET_PIN_STATUS_PENDING: _ClassVar[ResetPinStatus]
    RESET_PIN_STATUS_APPROVED: _ClassVar[ResetPinStatus]
    RESET_PIN_STATUS_DENIED: _ClassVar[ResetPinStatus]
NOTIFICATION_CHANNEL_UNKNOWN: NotificationChannelType
NOTIFICATION_CHANNEL_FIREBASE: NotificationChannelType
NOTIFICATION_CHANNEL_BAIDU: NotificationChannelType
OS_UNKNOWN: Os
OS_IOS: Os
OS_ANDROID: Os
NOTIFICATION_CATEGORY_UNKNOWN: NotificationCategory
NOTIFICATION_CATEGORY_CHARGE: NotificationCategory
NOTIFICATION_CATEGORY_SECURITY: NotificationCategory
NOTIFICATION_CATEGORY_SOFTWARE: NotificationCategory
NOTIFICATION_CATEGORY_HVAC: NotificationCategory
NOTIFICATION_CATEGORY_REQUIRED: NotificationCategory
NOTIFICATION_CATEGORY_CDR_EMAIL: NotificationCategory
NOTIFICATION_CATEGORY_SUBSCRIPTION: NotificationCategory
NOTIFICATION_CATEGORY_REFERRAL_CAMPAIGN: NotificationCategory
NOTIFICATION_CATEGORY_RECALL_CAMPAIGN: NotificationCategory
NOTIFICATION_CATEGORY_CLOSURE: NotificationCategory
NOTIFICATION_CATEGORY_ACCESSORIES: NotificationCategory
NOTIFICATION_CATEGORY_USER_PROFILE: NotificationCategory
NOTIFICATION_CATEGORY_TIRE_PRESSURE: NotificationCategory
ENCRYPTION_UNKNOWN: Encryption
ENCRYPTION_SINGLE: Encryption
ENCRYPTION_MUTUAL: Encryption
RESET_PIN_STATUS_UNKNOWN: ResetPinStatus
RESET_PIN_STATUS_PENDING: ResetPinStatus
RESET_PIN_STATUS_APPROVED: ResetPinStatus
RESET_PIN_STATUS_DENIED: ResetPinStatus

class LoginRequest(_message.Message):
    __slots__ = ("username", "password", "notification_channel_type", "os", "notification_device_token", "locale", "device_id", "client_name")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    notification_channel_type: NotificationChannelType
    os: Os
    notification_device_token: str
    locale: str
    device_id: str
    client_name: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., notification_channel_type: _Optional[_Union[NotificationChannelType, str]] = ..., os: _Optional[_Union[Os, str]] = ..., notification_device_token: _Optional[str] = ..., locale: _Optional[str] = ..., device_id: _Optional[str] = ..., client_name: _Optional[str] = ...) -> None: ...

class SessionInfo(_message.Message):
    __slots__ = ("id_token", "expiry_time_sec", "refresh_token", "gigya_jwt")
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GIGYA_JWT_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    expiry_time_sec: int
    refresh_token: str
    gigya_jwt: str
    def __init__(self, id_token: _Optional[str] = ..., expiry_time_sec: _Optional[int] = ..., refresh_token: _Optional[str] = ..., gigya_jwt: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("uid", "session_info", "user_profile", "user_vehicle_data", "subscriptions", "encryption")
    UID_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    USER_VEHICLE_DATA_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    uid: str
    session_info: SessionInfo
    user_profile: _user_profile_service_pb2.UserProfile
    user_vehicle_data: _containers.RepeatedCompositeFieldContainer[_vehicle_state_service_pb2.Vehicle]
    subscriptions: _containers.RepeatedScalarFieldContainer[NotificationCategory]
    encryption: Encryption
    def __init__(self, uid: _Optional[str] = ..., session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., user_profile: _Optional[_Union[_user_profile_service_pb2.UserProfile, _Mapping]] = ..., user_vehicle_data: _Optional[_Iterable[_Union[_vehicle_state_service_pb2.Vehicle, _Mapping]]] = ..., subscriptions: _Optional[_Iterable[_Union[NotificationCategory, str]]] = ..., encryption: _Optional[_Union[Encryption, str]] = ...) -> None: ...

class GetNewJWTTokenRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class GetNewJWTTokenResponse(_message.Message):
    __slots__ = ("session_info", "encryption")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    encryption: Encryption
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., encryption: _Optional[_Union[Encryption, str]] = ...) -> None: ...

class RefreshTokenRequest(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RefreshTokenResponse(_message.Message):
    __slots__ = ("jwt_token", "expiry_time_sec", "gigya_jwt")
    JWT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    GIGYA_JWT_FIELD_NUMBER: _ClassVar[int]
    jwt_token: str
    expiry_time_sec: int
    gigya_jwt: str
    def __init__(self, jwt_token: _Optional[str] = ..., expiry_time_sec: _Optional[int] = ..., gigya_jwt: _Optional[str] = ...) -> None: ...

class ConfirmResetPinRequest(_message.Message):
    __slots__ = ("reset_pin_id", "status")
    RESET_PIN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    reset_pin_id: str
    status: ResetPinStatus
    def __init__(self, reset_pin_id: _Optional[str] = ..., status: _Optional[_Union[ResetPinStatus, str]] = ...) -> None: ...

class ConfirmResetPinResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSubscriptionResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedScalarFieldContainer[NotificationCategory]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[NotificationCategory, str]]] = ...) -> None: ...

class UpdateSubscriptionRequest(_message.Message):
    __slots__ = ("enable", "disable")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    enable: _containers.RepeatedScalarFieldContainer[NotificationCategory]
    disable: _containers.RepeatedScalarFieldContainer[NotificationCategory]
    def __init__(self, enable: _Optional[_Iterable[_Union[NotificationCategory, str]]] = ..., disable: _Optional[_Iterable[_Union[NotificationCategory, str]]] = ...) -> None: ...

class UpdateSubscriptionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserVehiclesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserVehiclesResponse(_message.Message):
    __slots__ = ("user_vehicle_data",)
    USER_VEHICLE_DATA_FIELD_NUMBER: _ClassVar[int]
    user_vehicle_data: _containers.RepeatedCompositeFieldContainer[_vehicle_state_service_pb2.Vehicle]
    def __init__(self, user_vehicle_data: _Optional[_Iterable[_Union[_vehicle_state_service_pb2.Vehicle, _Mapping]]] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("notification_device_token",)
    NOTIFICATION_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notification_device_token: str
    def __init__(self, notification_device_token: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshNotificationTokenRequest(_message.Message):
    __slots__ = ("notification_channel_type", "os", "old_device_token", "new_device_token", "locale")
    NOTIFICATION_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OLD_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEW_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    notification_channel_type: NotificationChannelType
    os: Os
    old_device_token: str
    new_device_token: str
    locale: str
    def __init__(self, notification_channel_type: _Optional[_Union[NotificationChannelType, str]] = ..., os: _Optional[_Union[Os, str]] = ..., old_device_token: _Optional[str] = ..., new_device_token: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class RefreshNotificationTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetNickNameRequest(_message.Message):
    __slots__ = ("vehicle_id", "nickname")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    nickname: str
    def __init__(self, vehicle_id: _Optional[str] = ..., nickname: _Optional[str] = ...) -> None: ...

class SetNickNameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ActivateDeviceRequest(_message.Message):
    __slots__ = ("activation_pin",)
    ACTIVATION_PIN_FIELD_NUMBER: _ClassVar[int]
    activation_pin: str
    def __init__(self, activation_pin: _Optional[str] = ...) -> None: ...

class ActivateDeviceResponse(_message.Message):
    __slots__ = ("session_info", "user_vehicle_data")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_VEHICLE_DATA_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    user_vehicle_data: _containers.RepeatedCompositeFieldContainer[_vehicle_state_service_pb2.Vehicle]
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., user_vehicle_data: _Optional[_Iterable[_Union[_vehicle_state_service_pb2.Vehicle, _Mapping]]] = ...) -> None: ...

class DeviceEnrollRequest(_message.Message):
    __slots__ = ("certificate_request",)
    CERTIFICATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    certificate_request: str
    def __init__(self, certificate_request: _Optional[str] = ...) -> None: ...

class DeviceEnrollResponse(_message.Message):
    __slots__ = ("certificate",)
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    certificate: str
    def __init__(self, certificate: _Optional[str] = ...) -> None: ...
