from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Concern(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONCERN_UNKNOWN: _ClassVar[Concern]
    CONCERN_TIRE_SERVICE_TIRE_PURCHASE: _ClassVar[Concern]
    CONCERN_TIRE_SERVICE_TIRE_SWAP: _ClassVar[Concern]
    CONCERN_TIRE_SERVICE_TIRE_ROTATION: _ClassVar[Concern]
    CONCERN_TIRE_SERVICE_BALANCE_AND_WHEEL_ALIGNMENT: _ClassVar[Concern]
    CONCERN_TIRE_SERVICE_OTHER_TIRE_SERVICE: _ClassVar[Concern]
    CONCERN_ANNUAL_MAINTENANCE: _ClassVar[Concern]
CONCERN_UNKNOWN: Concern
CONCERN_TIRE_SERVICE_TIRE_PURCHASE: Concern
CONCERN_TIRE_SERVICE_TIRE_SWAP: Concern
CONCERN_TIRE_SERVICE_TIRE_ROTATION: Concern
CONCERN_TIRE_SERVICE_BALANCE_AND_WHEEL_ALIGNMENT: Concern
CONCERN_TIRE_SERVICE_OTHER_TIRE_SERVICE: Concern
CONCERN_ANNUAL_MAINTENANCE: Concern

class ReferralHistory(_message.Message):
    __slots__ = ("referee_email", "referral_status", "referral_points", "referee_first_name", "referee_last_name", "referral_date", "trim")
    REFEREE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    REFEREE_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFEREE_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_DATE_FIELD_NUMBER: _ClassVar[int]
    TRIM_FIELD_NUMBER: _ClassVar[int]
    referee_email: str
    referral_status: str
    referral_points: float
    referee_first_name: str
    referee_last_name: str
    referral_date: str
    trim: str
    def __init__(self, referee_email: _Optional[str] = ..., referral_status: _Optional[str] = ..., referral_points: _Optional[float] = ..., referee_first_name: _Optional[str] = ..., referee_last_name: _Optional[str] = ..., referral_date: _Optional[str] = ..., trim: _Optional[str] = ...) -> None: ...

class MemberAttributes(_message.Message):
    __slots__ = ("value", "name")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    value: str
    name: str
    def __init__(self, value: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ReferralData(_message.Message):
    __slots__ = ("email", "status", "referral_code", "points_balance", "total_referral_count", "referrals", "member_attributes", "valid_state", "valid_age", "country")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_CODE_FIELD_NUMBER: _ClassVar[int]
    POINTS_BALANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REFERRAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFERRALS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VALID_STATE_FIELD_NUMBER: _ClassVar[int]
    VALID_AGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    email: str
    status: str
    referral_code: str
    points_balance: int
    total_referral_count: int
    referrals: _containers.RepeatedCompositeFieldContainer[ReferralHistory]
    member_attributes: _containers.RepeatedCompositeFieldContainer[MemberAttributes]
    valid_state: bool
    valid_age: bool
    country: str
    def __init__(self, email: _Optional[str] = ..., status: _Optional[str] = ..., referral_code: _Optional[str] = ..., points_balance: _Optional[int] = ..., total_referral_count: _Optional[int] = ..., referrals: _Optional[_Iterable[_Union[ReferralHistory, _Mapping]]] = ..., member_attributes: _Optional[_Iterable[_Union[MemberAttributes, _Mapping]]] = ..., valid_state: bool = ..., valid_age: bool = ..., country: _Optional[str] = ...) -> None: ...

class BigCommerceLoginRequest(_message.Message):
    __slots__ = ("email", "first_name", "last_name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    first_name: str
    last_name: str
    def __init__(self, email: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class BigCommerceLoginResponse(_message.Message):
    __slots__ = ("customer", "url")
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    customer: str
    url: str
    def __init__(self, customer: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CreateLoyaltyMemberRequest(_message.Message):
    __slots__ = ("first_name", "last_name", "preferred_language", "email", "referral_code")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_CODE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    preferred_language: str
    email: str
    referral_code: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., preferred_language: _Optional[str] = ..., email: _Optional[str] = ..., referral_code: _Optional[str] = ...) -> None: ...

class CreateLoyaltyMemberResponse(_message.Message):
    __slots__ = ("status_code", "message", "data")
    class Data(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    message: str
    data: CreateLoyaltyMemberResponse.Data
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ..., data: _Optional[_Union[CreateLoyaltyMemberResponse.Data, _Mapping]] = ...) -> None: ...

class ReferralHistoryRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ReferralHistoryResponse(_message.Message):
    __slots__ = ("status_code", "message", "data")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    message: str
    data: ReferralData
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ..., data: _Optional[_Union[ReferralData, _Mapping]] = ...) -> None: ...

class ConcernDetail(_message.Message):
    __slots__ = ("concern", "notes")
    CONCERN_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    concern: Concern
    notes: str
    def __init__(self, concern: _Optional[_Union[Concern, str]] = ..., notes: _Optional[str] = ...) -> None: ...

class CreateServiceAppointmentRequest(_message.Message):
    __slots__ = ("vin", "lucid_customer_id", "location_id", "arrival_time", "concern_details")
    VIN_FIELD_NUMBER: _ClassVar[int]
    LUCID_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    CONCERN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    vin: str
    lucid_customer_id: str
    location_id: str
    arrival_time: str
    concern_details: _containers.RepeatedCompositeFieldContainer[ConcernDetail]
    def __init__(self, vin: _Optional[str] = ..., lucid_customer_id: _Optional[str] = ..., location_id: _Optional[str] = ..., arrival_time: _Optional[str] = ..., concern_details: _Optional[_Iterable[_Union[ConcernDetail, _Mapping]]] = ...) -> None: ...

class CreateServiceAppointmentResponse(_message.Message):
    __slots__ = ("status", "message", "service_appt_number", "service_appt_id", "appointment_status", "estimated_start_time", "estimated_end_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APPT_ID_FIELD_NUMBER: _ClassVar[int]
    APPOINTMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_START_TIME_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_END_TIME_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    service_appt_number: str
    service_appt_id: str
    appointment_status: str
    estimated_start_time: str
    estimated_end_time: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ..., service_appt_number: _Optional[str] = ..., service_appt_id: _Optional[str] = ..., appointment_status: _Optional[str] = ..., estimated_start_time: _Optional[str] = ..., estimated_end_time: _Optional[str] = ...) -> None: ...

class UpdateServiceAppointmentResponse(_message.Message):
    __slots__ = ("status", "message", "service_appt_number", "service_appt_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APPT_ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    service_appt_number: str
    service_appt_id: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ..., service_appt_number: _Optional[str] = ..., service_appt_id: _Optional[str] = ...) -> None: ...

class UpdateServiceAppointmentRequest(_message.Message):
    __slots__ = ("service_appt_id", "arrival_datetime", "concern_details")
    SERVICE_APPT_ID_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_DATETIME_FIELD_NUMBER: _ClassVar[int]
    CONCERN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    service_appt_id: str
    arrival_datetime: str
    concern_details: _containers.RepeatedCompositeFieldContainer[ConcernDetail]
    def __init__(self, service_appt_id: _Optional[str] = ..., arrival_datetime: _Optional[str] = ..., concern_details: _Optional[_Iterable[_Union[ConcernDetail, _Mapping]]] = ...) -> None: ...

class GetServiceAppointmentSlotsRequest(_message.Message):
    __slots__ = ("location_id", "service_date")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATE_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    service_date: str
    def __init__(self, location_id: _Optional[str] = ..., service_date: _Optional[str] = ...) -> None: ...

class GetServiceAppointmentSlotsResponse(_message.Message):
    __slots__ = ("status", "message", "timeslots")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESLOTS_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    timeslots: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ..., timeslots: _Optional[_Iterable[str]] = ...) -> None: ...

class GetServiceAppointmentsV1Request(_message.Message):
    __slots__ = ("customer_id",)
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class ServiceAppointmentsV1Data(_message.Message):
    __slots__ = ("work_order_number", "vin", "time_zone", "appointment_status", "service_type", "location_id", "service_appt_id", "service_appt_number", "technician_name", "advisor_name", "lucid_id", "arrival_time", "created_date", "street", "address", "phone", "concern_details")
    WORK_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    APPOINTMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APPT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TECHNICIAN_NAME_FIELD_NUMBER: _ClassVar[int]
    ADVISOR_NAME_FIELD_NUMBER: _ClassVar[int]
    LUCID_ID_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CONCERN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    work_order_number: str
    vin: str
    time_zone: str
    appointment_status: str
    service_type: str
    location_id: str
    service_appt_id: str
    service_appt_number: str
    technician_name: str
    advisor_name: str
    lucid_id: str
    arrival_time: str
    created_date: str
    street: str
    address: str
    phone: str
    concern_details: _containers.RepeatedCompositeFieldContainer[ConcernDetail]
    def __init__(self, work_order_number: _Optional[str] = ..., vin: _Optional[str] = ..., time_zone: _Optional[str] = ..., appointment_status: _Optional[str] = ..., service_type: _Optional[str] = ..., location_id: _Optional[str] = ..., service_appt_id: _Optional[str] = ..., service_appt_number: _Optional[str] = ..., technician_name: _Optional[str] = ..., advisor_name: _Optional[str] = ..., lucid_id: _Optional[str] = ..., arrival_time: _Optional[str] = ..., created_date: _Optional[str] = ..., street: _Optional[str] = ..., address: _Optional[str] = ..., phone: _Optional[str] = ..., concern_details: _Optional[_Iterable[_Union[ConcernDetail, _Mapping]]] = ...) -> None: ...

class GetServiceAppointmentsV1Response(_message.Message):
    __slots__ = ("status", "data", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    data: _containers.RepeatedCompositeFieldContainer[ServiceAppointmentsV1Data]
    message: str
    def __init__(self, status: _Optional[str] = ..., data: _Optional[_Iterable[_Union[ServiceAppointmentsV1Data, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class CancelServiceAppointmentRequest(_message.Message):
    __slots__ = ("service_appt_id",)
    SERVICE_APPT_ID_FIELD_NUMBER: _ClassVar[int]
    service_appt_id: str
    def __init__(self, service_appt_id: _Optional[str] = ...) -> None: ...

class CancelServiceAppointmentResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
