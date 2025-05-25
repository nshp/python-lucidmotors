from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionSKU(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_SKU_UNKNOWN: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_AD02TRIAL: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_AD02: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_AU01TRIAL: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_AU01: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_AD01: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_DCSCUS: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_DCSCCA: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_DCPUS: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_DCPCA: _ClassVar[SubscriptionSKU]
    SUBSCRIPTION_SKU_LCBP: _ClassVar[SubscriptionSKU]
SUBSCRIPTION_SKU_UNKNOWN: SubscriptionSKU
SUBSCRIPTION_SKU_AD02TRIAL: SubscriptionSKU
SUBSCRIPTION_SKU_AD02: SubscriptionSKU
SUBSCRIPTION_SKU_AU01TRIAL: SubscriptionSKU
SUBSCRIPTION_SKU_AU01: SubscriptionSKU
SUBSCRIPTION_SKU_AD01: SubscriptionSKU
SUBSCRIPTION_SKU_DCSCUS: SubscriptionSKU
SUBSCRIPTION_SKU_DCSCCA: SubscriptionSKU
SUBSCRIPTION_SKU_DCPUS: SubscriptionSKU
SUBSCRIPTION_SKU_DCPCA: SubscriptionSKU
SUBSCRIPTION_SKU_LCBP: SubscriptionSKU

class Feature(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class Description(_message.Message):
    __slots__ = ("text", "features")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    text: str
    features: _containers.RepeatedCompositeFieldContainer[Feature]
    def __init__(self, text: _Optional[str] = ..., features: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ...) -> None: ...

class Entitlement(_message.Message):
    __slots__ = ("should_notify", "billing_type_description", "entitlement_type", "start_date", "end_date", "cancel_status", "renewal_status", "renewal_date", "sku", "restricts_products", "price", "currency", "product_id", "billing_type_frequency", "name", "description")
    SHOULD_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    BILLING_TYPE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_STATUS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_DATE_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    RESTRICTS_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_TYPE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    should_notify: bool
    billing_type_description: str
    entitlement_type: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    cancel_status: str
    renewal_status: str
    renewal_date: _timestamp_pb2.Timestamp
    sku: SubscriptionSKU
    restricts_products: _containers.RepeatedScalarFieldContainer[str]
    price: float
    currency: str
    product_id: str
    billing_type_frequency: str
    name: str
    description: Description
    def __init__(self, should_notify: bool = ..., billing_type_description: _Optional[str] = ..., entitlement_type: _Optional[str] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_status: _Optional[str] = ..., renewal_status: _Optional[str] = ..., renewal_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sku: _Optional[_Union[SubscriptionSKU, str]] = ..., restricts_products: _Optional[_Iterable[str]] = ..., price: _Optional[float] = ..., currency: _Optional[str] = ..., product_id: _Optional[str] = ..., billing_type_frequency: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[Description, _Mapping]] = ...) -> None: ...

class Subscription(_message.Message):
    __slots__ = ("vin", "active_entitlements")
    VIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    vin: str
    active_entitlements: _containers.RepeatedCompositeFieldContainer[Entitlement]
    def __init__(self, vin: _Optional[str] = ..., active_entitlements: _Optional[_Iterable[_Union[Entitlement, _Mapping]]] = ...) -> None: ...

class UserEntitlement(_message.Message):
    __slots__ = ("user_id", "subscriptions")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscriptions: _containers.RepeatedCompositeFieldContainer[Subscription]
    def __init__(self, user_id: _Optional[str] = ..., subscriptions: _Optional[_Iterable[_Union[Subscription, _Mapping]]] = ...) -> None: ...

class GetUserActiveEntitlementsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserActiveEntitlementsResponse(_message.Message):
    __slots__ = ("user_entitlements",)
    USER_ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    user_entitlements: UserEntitlement
    def __init__(self, user_entitlements: _Optional[_Union[UserEntitlement, _Mapping]] = ...) -> None: ...
