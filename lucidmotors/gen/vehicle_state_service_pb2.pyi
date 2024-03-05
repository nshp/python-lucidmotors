from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_LEVEL_UNKNOWN: _ClassVar[AccessLevel]
    ACCESS_LEVEL_PREDELIVERY_OWNER: _ClassVar[AccessLevel]
    ACCESS_LEVEL_PRIMARY_OWNER: _ClassVar[AccessLevel]

class Model(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_UNKNOWN: _ClassVar[Model]
    MODEL_AIR: _ClassVar[Model]
    MODEL_GRAVITY: _ClassVar[Model]

class ModelVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_VARIANT_UNKNOWN: _ClassVar[ModelVariant]
    MODEL_VARIANT_DREAM_EDITION: _ClassVar[ModelVariant]
    MODEL_VARIANT_GRAND_TOURING: _ClassVar[ModelVariant]
    MODEL_VARIANT_TOURING: _ClassVar[ModelVariant]
    MODEL_VARIANT_PURE: _ClassVar[ModelVariant]

class PaintColor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAINT_COLOR_UNKNOWN: _ClassVar[PaintColor]
    PAINT_COLOR_EUREKA_GOLD: _ClassVar[PaintColor]
    PAINT_COLOR_STELLAR_WHITE: _ClassVar[PaintColor]
    PAINT_COLOR_INFINITE_BLACK: _ClassVar[PaintColor]
    PAINT_COLOR_COSMOS_SILVER: _ClassVar[PaintColor]
    PAINT_COLOR_QUANTUM_GREY: _ClassVar[PaintColor]
    PAINT_COLOR_ZENITH_RED: _ClassVar[PaintColor]
    PAINT_COLOR_FATHOM_BLUE: _ClassVar[PaintColor]

class Look(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOK_UNKNOWN: _ClassVar[Look]
    LOOK_PLATINUM: _ClassVar[Look]
    LOOK_STEALTH: _ClassVar[Look]

class Wheels(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WHEELS_UNKNOWN: _ClassVar[Wheels]
    WHEELS_DREAM: _ClassVar[Wheels]
    WHEELS_BLADE: _ClassVar[Wheels]
    WHEELS_LITE: _ClassVar[Wheels]
    WHEELS_RANGE: _ClassVar[Wheels]
    WHEELS_LITE_STEALTH: _ClassVar[Wheels]

class SubscriptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_STATUS_UNKNOWN: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_CURRENT: _ClassVar[SubscriptionStatus]

class ChargingAccountStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHARGING_ACCOUNT_STATUS_UNKNOWN: _ClassVar[ChargingAccountStatus]
    CHARGING_ACCOUNT_STATUS_ENROLLED: _ClassVar[ChargingAccountStatus]

class ChargingVendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHARGING_VENDOR_UNKNOWN: _ClassVar[ChargingVendor]
    CHARGING_VENDOR_ELECTRIFY_AMERICA: _ClassVar[ChargingVendor]
    CHARGING_VENDOR_BOSCH: _ClassVar[ChargingVendor]

class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDITION_UNKNOWN: _ClassVar[Edition]
    EDITION_PERFORMANCE: _ClassVar[Edition]
    EDITION_RANGE: _ClassVar[Edition]
    EDITION_STANDARD: _ClassVar[Edition]

class BatteryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTERY_TYPE_UNKNOWN: _ClassVar[BatteryType]
    BATTERY_TYPE_01: _ClassVar[BatteryType]
    BATTERY_TYPE_02: _ClassVar[BatteryType]
    BATTERY_TYPE_03: _ClassVar[BatteryType]
    BATTERY_TYPE_04: _ClassVar[BatteryType]
    BATTERY_TYPE_05: _ClassVar[BatteryType]
    BATTERY_TYPE_06: _ClassVar[BatteryType]
    BATTERY_TYPE_07: _ClassVar[BatteryType]
    BATTERY_TYPE_08: _ClassVar[BatteryType]
    BATTERY_TYPE_09: _ClassVar[BatteryType]

class Interior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERIOR_UNKNOWN: _ClassVar[Interior]
    INTERIOR_SANTA_CRUZ: _ClassVar[Interior]
    INTERIOR_TAHOE: _ClassVar[Interior]
    INTERIOR_MOJAVE: _ClassVar[Interior]
    INTERIOR_SANTA_MONICA: _ClassVar[Interior]

class StrutType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRUT_TYPE_UNKNOWN: _ClassVar[StrutType]
    STRUT_TYPE_GAS: _ClassVar[StrutType]
    STRUT_TYPE_POWER: _ClassVar[StrutType]

class RoofType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROOF_TYPE_UNKNOWN: _ClassVar[RoofType]
    ROOF_TYPE_GLASS_CANOPY: _ClassVar[RoofType]
    ROOF_TYPE_METAL: _ClassVar[RoofType]

class WarningState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WARNING_UNKNOWN: _ClassVar[WarningState]
    WARNING_OFF: _ClassVar[WarningState]
    WARNING_ON: _ClassVar[WarningState]

class BatteryPreconStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTERY_PRECON_UNKNOWN: _ClassVar[BatteryPreconStatus]
    BATTERY_PRECON_OFF: _ClassVar[BatteryPreconStatus]
    BATTERY_PRECON_ON: _ClassVar[BatteryPreconStatus]
    BATTERY_PRECON_UNAVAILABLE: _ClassVar[BatteryPreconStatus]

class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POWER_STATE_UNKNOWN: _ClassVar[PowerState]
    POWER_STATE_SLEEP: _ClassVar[PowerState]
    POWER_STATE_WINK: _ClassVar[PowerState]
    POWER_STATE_ACCESSORY: _ClassVar[PowerState]
    POWER_STATE_DRIVE: _ClassVar[PowerState]
    POWER_STATE_LIVE_CHARGE: _ClassVar[PowerState]
    POWER_STATE_SLEEP_CHARGE: _ClassVar[PowerState]
    POWER_STATE_LIVE_UPDATE: _ClassVar[PowerState]
    POWER_STATE_CLOUD_2: _ClassVar[PowerState]
    POWER_STATE_MONITOR: _ClassVar[PowerState]

class LockState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK_STATE_UNKNOWN: _ClassVar[LockState]
    LOCK_STATE_UNLOCKED: _ClassVar[LockState]
    LOCK_STATE_LOCKED: _ClassVar[LockState]

class DoorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOOR_STATE_UNKNOWN: _ClassVar[DoorState]
    DOOR_STATE_OPEN: _ClassVar[DoorState]
    DOOR_STATE_CLOSED: _ClassVar[DoorState]
    DOOR_STATE_AJAR: _ClassVar[DoorState]

class WalkawayState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WALKAWAY_UNKNOWN: _ClassVar[WalkawayState]
    WALKAWAY_ACTIVE: _ClassVar[WalkawayState]
    WALKAWAY_DISABLE: _ClassVar[WalkawayState]

class AccessRequest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_REQUEST_UNKNOWN: _ClassVar[AccessRequest]
    ACCESS_REQUEST_ACTIVE: _ClassVar[AccessRequest]
    ACCESS_REQUEST_PASSIVE: _ClassVar[AccessRequest]

class LightState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIGHT_STATE_REALLY_UNKNOWN: _ClassVar[LightState]
    LIGHT_STATE_OFF: _ClassVar[LightState]
    LIGHT_STATE_ON: _ClassVar[LightState]
    LIGHT_STATE_UNKNOWN: _ClassVar[LightState]

class LightAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIGHT_ACTION_UNKNOWN: _ClassVar[LightAction]
    LIGHT_ACTION_FLASH: _ClassVar[LightAction]
    LIGHT_ACTION_ON: _ClassVar[LightAction]
    LIGHT_ACTION_OFF: _ClassVar[LightAction]

class ChargeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHARGE_STATE_UNKNOWN: _ClassVar[ChargeState]
    CHARGE_STATE_NOT_CONNECTED: _ClassVar[ChargeState]
    CHARGE_STATE_CABLE_CONNECTED: _ClassVar[ChargeState]
    CHARGE_STATE_CHARGING: _ClassVar[ChargeState]
    CHARGE_STATE_CHARGING_END_OK: _ClassVar[ChargeState]
    CHARGE_STATE_DISCHARGING: _ClassVar[ChargeState]

class ScheduledChargeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULED_CHARGE_STATE_UNKNOWN: _ClassVar[ScheduledChargeState]
    SCHEDULED_CHARGE_STATE_IDLE: _ClassVar[ScheduledChargeState]
    SCHEDULED_CHARGE_STATE_SCHEDULED_TO_CHARGE: _ClassVar[ScheduledChargeState]
    SCHEDULED_CHARGE_STATE_REQUEST_TO_CHARGE: _ClassVar[ScheduledChargeState]

class ScheduledChargeUnavailableState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULED_CHARGE_UNAVAILABLE_UNKNOWN: _ClassVar[ScheduledChargeUnavailableState]
    SCHEDULED_CHARGE_UNAVAILABLE_NO_REQUEST: _ClassVar[ScheduledChargeUnavailableState]

class EnergyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_TYPE_UNKNOWN: _ClassVar[EnergyType]
    ENERGY_TYPE_AC: _ClassVar[EnergyType]
    ENERGY_TYPE_DC: _ClassVar[EnergyType]
    ENERGY_TYPE_V2V: _ClassVar[EnergyType]

class UpdateState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_STATE_UNKNOWN: _ClassVar[UpdateState]
    UPDATE_STATE_IN_PROGRESS: _ClassVar[UpdateState]
    UPDATE_STATE_SUCCESS: _ClassVar[UpdateState]
    UPDATE_STATE_FAILED: _ClassVar[UpdateState]
    UPDATE_FAILED_DRIVE_ALLOWED: _ClassVar[UpdateState]
    UPDATE_SUCCESS_WITH_WARNINGS: _ClassVar[UpdateState]

class UpdateAvailability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_AVAILABILITY_UNKNOWN: _ClassVar[UpdateAvailability]
    UPDATE_AVAILABLE: _ClassVar[UpdateAvailability]

class AlarmStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALARM_STATUS_UNKNOWN: _ClassVar[AlarmStatus]
    ALARM_STATUS_DISARMED: _ClassVar[AlarmStatus]
    ALARM_STATUS_ARMED: _ClassVar[AlarmStatus]

class AlarmMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALARM_MODE_UNKNOWN: _ClassVar[AlarmMode]
    ALARM_MODE_OFF: _ClassVar[AlarmMode]
    ALARM_MODE_ON: _ClassVar[AlarmMode]
    ALARM_MODE_SILENT: _ClassVar[AlarmMode]

class CloudConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_CONNECTION_UNKNOWN: _ClassVar[CloudConnectionState]
    CLOUD_CONNECTION_CONNECTED: _ClassVar[CloudConnectionState]
    CLOUD_CONNECTION_DISCONNECTED: _ClassVar[CloudConnectionState]

class KeylessDrivingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEYLESS_DRIVING_UNKNOWN: _ClassVar[KeylessDrivingState]
    KEYLESS_DRIVING_ON: _ClassVar[KeylessDrivingState]
    KEYLESS_DRIVING_OFF: _ClassVar[KeylessDrivingState]

class HvacPower(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HVAC_POWER_UNKNOWN: _ClassVar[HvacPower]
    HVAC_ON: _ClassVar[HvacPower]
    HVAC_OFF: _ClassVar[HvacPower]
    HVAC_PRECONDITION: _ClassVar[HvacPower]
    HVAC_KEEP_TEMP: _ClassVar[HvacPower]

class DefrostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFROST_STATE_UNKNOWN: _ClassVar[DefrostState]
    DEFROST_ON: _ClassVar[DefrostState]
    DEFROST_OFF: _ClassVar[DefrostState]

class HvacPreconditionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HVAC_PRECONDITION_STATUS_UNKNOWN: _ClassVar[HvacPreconditionStatus]
    HVAC_PRECONDITION_STATUS_STILL_ACTIVE: _ClassVar[HvacPreconditionStatus]
    HVAC_PRECONDITION_STATUS_USER_INPUT: _ClassVar[HvacPreconditionStatus]

class KeepClimateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEEP_CLIMATE_STATUS_UNKNOWN: _ClassVar[KeepClimateStatus]
    KEEP_CLIMATE_STATUS_INACTIVE: _ClassVar[KeepClimateStatus]
    KEEP_CLIMATE_STATUS_ENABLED: _ClassVar[KeepClimateStatus]
    KEEP_CLIMATE_STATUS_CANCELED: _ClassVar[KeepClimateStatus]
    KEEP_CLIMATE_STATUS_PET_MODE_ON: _ClassVar[KeepClimateStatus]

class KeepClimateCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEEP_CLIMATE_CONDITION_UNKNOWN: _ClassVar[KeepClimateCondition]

class DriveMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DRIVE_MODE_UNKNOWN: _ClassVar[DriveMode]
    DRIVE_MODE_COMFORT: _ClassVar[DriveMode]
    DRIVE_MODE_SWIFT: _ClassVar[DriveMode]
    DRIVE_MODE_SPORT_PLUS: _ClassVar[DriveMode]
    DRIVE_MODE_SERVICE: _ClassVar[DriveMode]

class PrivacyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVACY_MODE_UNKNOWN: _ClassVar[PrivacyMode]
    PRIVACY_MODE_CONNECTIVITY_ENABLED: _ClassVar[PrivacyMode]
    PRIVACY_MODE_CONNECTIVITY_DISABLED: _ClassVar[PrivacyMode]

class GearPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GEAR_UNKNOWN: _ClassVar[GearPosition]
    GEAR_PARK: _ClassVar[GearPosition]
    GEAR_REVERSE: _ClassVar[GearPosition]
    GEAR_NEUTRAL: _ClassVar[GearPosition]
    GEAR_DRIVE: _ClassVar[GearPosition]

class SharedTripState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARED_TRIP_UNKNOWN: _ClassVar[SharedTripState]
    SHARED_TRIP_AVAILABLE: _ClassVar[SharedTripState]

class TcuState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TCU_UNKNOWN: _ClassVar[TcuState]
    TCU_SLEEP: _ClassVar[TcuState]
    TCU_DROWSY: _ClassVar[TcuState]
    TCU_FULL: _ClassVar[TcuState]
    TCU_FACTORY: _ClassVar[TcuState]

class LteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LTE_TYPE_UNKNOWN: _ClassVar[LteType]
    LTE_TYPE_3G: _ClassVar[LteType]
    LTE_TYPE_4G: _ClassVar[LteType]

class InternetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERNET_STATUS_UNKNOWN: _ClassVar[InternetStatus]
    INTERNET_DISCONNECTED: _ClassVar[InternetStatus]
    INTERNET_CONNECTED: _ClassVar[InternetStatus]

class ChargeAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHARGE_ACTION_UNKNOWN: _ClassVar[ChargeAction]
    CHARGE_ACTION_START: _ClassVar[ChargeAction]
    CHARGE_ACTION_STOP: _ClassVar[ChargeAction]

class DocumentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOCUMENT_TYPE_UNKNOWN: _ClassVar[DocumentType]
    DOCUMENT_TYPE_RELEASE_NOTES_PRE: _ClassVar[DocumentType]
    DOCUMENT_TYPE_RELEASE_NOTES_POST: _ClassVar[DocumentType]
    DOCUMENT_TYPE_OWNERS_MANUAL: _ClassVar[DocumentType]
ACCESS_LEVEL_UNKNOWN: AccessLevel
ACCESS_LEVEL_PREDELIVERY_OWNER: AccessLevel
ACCESS_LEVEL_PRIMARY_OWNER: AccessLevel
MODEL_UNKNOWN: Model
MODEL_AIR: Model
MODEL_GRAVITY: Model
MODEL_VARIANT_UNKNOWN: ModelVariant
MODEL_VARIANT_DREAM_EDITION: ModelVariant
MODEL_VARIANT_GRAND_TOURING: ModelVariant
MODEL_VARIANT_TOURING: ModelVariant
MODEL_VARIANT_PURE: ModelVariant
PAINT_COLOR_UNKNOWN: PaintColor
PAINT_COLOR_EUREKA_GOLD: PaintColor
PAINT_COLOR_STELLAR_WHITE: PaintColor
PAINT_COLOR_INFINITE_BLACK: PaintColor
PAINT_COLOR_COSMOS_SILVER: PaintColor
PAINT_COLOR_QUANTUM_GREY: PaintColor
PAINT_COLOR_ZENITH_RED: PaintColor
PAINT_COLOR_FATHOM_BLUE: PaintColor
LOOK_UNKNOWN: Look
LOOK_PLATINUM: Look
LOOK_STEALTH: Look
WHEELS_UNKNOWN: Wheels
WHEELS_DREAM: Wheels
WHEELS_BLADE: Wheels
WHEELS_LITE: Wheels
WHEELS_RANGE: Wheels
WHEELS_LITE_STEALTH: Wheels
SUBSCRIPTION_STATUS_UNKNOWN: SubscriptionStatus
SUBSCRIPTION_STATUS_CURRENT: SubscriptionStatus
CHARGING_ACCOUNT_STATUS_UNKNOWN: ChargingAccountStatus
CHARGING_ACCOUNT_STATUS_ENROLLED: ChargingAccountStatus
CHARGING_VENDOR_UNKNOWN: ChargingVendor
CHARGING_VENDOR_ELECTRIFY_AMERICA: ChargingVendor
CHARGING_VENDOR_BOSCH: ChargingVendor
EDITION_UNKNOWN: Edition
EDITION_PERFORMANCE: Edition
EDITION_RANGE: Edition
EDITION_STANDARD: Edition
BATTERY_TYPE_UNKNOWN: BatteryType
BATTERY_TYPE_01: BatteryType
BATTERY_TYPE_02: BatteryType
BATTERY_TYPE_03: BatteryType
BATTERY_TYPE_04: BatteryType
BATTERY_TYPE_05: BatteryType
BATTERY_TYPE_06: BatteryType
BATTERY_TYPE_07: BatteryType
BATTERY_TYPE_08: BatteryType
BATTERY_TYPE_09: BatteryType
INTERIOR_UNKNOWN: Interior
INTERIOR_SANTA_CRUZ: Interior
INTERIOR_TAHOE: Interior
INTERIOR_MOJAVE: Interior
INTERIOR_SANTA_MONICA: Interior
STRUT_TYPE_UNKNOWN: StrutType
STRUT_TYPE_GAS: StrutType
STRUT_TYPE_POWER: StrutType
ROOF_TYPE_UNKNOWN: RoofType
ROOF_TYPE_GLASS_CANOPY: RoofType
ROOF_TYPE_METAL: RoofType
WARNING_UNKNOWN: WarningState
WARNING_OFF: WarningState
WARNING_ON: WarningState
BATTERY_PRECON_UNKNOWN: BatteryPreconStatus
BATTERY_PRECON_OFF: BatteryPreconStatus
BATTERY_PRECON_ON: BatteryPreconStatus
BATTERY_PRECON_UNAVAILABLE: BatteryPreconStatus
POWER_STATE_UNKNOWN: PowerState
POWER_STATE_SLEEP: PowerState
POWER_STATE_WINK: PowerState
POWER_STATE_ACCESSORY: PowerState
POWER_STATE_DRIVE: PowerState
POWER_STATE_LIVE_CHARGE: PowerState
POWER_STATE_SLEEP_CHARGE: PowerState
POWER_STATE_LIVE_UPDATE: PowerState
POWER_STATE_CLOUD_2: PowerState
POWER_STATE_MONITOR: PowerState
LOCK_STATE_UNKNOWN: LockState
LOCK_STATE_UNLOCKED: LockState
LOCK_STATE_LOCKED: LockState
DOOR_STATE_UNKNOWN: DoorState
DOOR_STATE_OPEN: DoorState
DOOR_STATE_CLOSED: DoorState
DOOR_STATE_AJAR: DoorState
WALKAWAY_UNKNOWN: WalkawayState
WALKAWAY_ACTIVE: WalkawayState
WALKAWAY_DISABLE: WalkawayState
ACCESS_REQUEST_UNKNOWN: AccessRequest
ACCESS_REQUEST_ACTIVE: AccessRequest
ACCESS_REQUEST_PASSIVE: AccessRequest
LIGHT_STATE_REALLY_UNKNOWN: LightState
LIGHT_STATE_OFF: LightState
LIGHT_STATE_ON: LightState
LIGHT_STATE_UNKNOWN: LightState
LIGHT_ACTION_UNKNOWN: LightAction
LIGHT_ACTION_FLASH: LightAction
LIGHT_ACTION_ON: LightAction
LIGHT_ACTION_OFF: LightAction
CHARGE_STATE_UNKNOWN: ChargeState
CHARGE_STATE_NOT_CONNECTED: ChargeState
CHARGE_STATE_CABLE_CONNECTED: ChargeState
CHARGE_STATE_CHARGING: ChargeState
CHARGE_STATE_CHARGING_END_OK: ChargeState
CHARGE_STATE_DISCHARGING: ChargeState
SCHEDULED_CHARGE_STATE_UNKNOWN: ScheduledChargeState
SCHEDULED_CHARGE_STATE_IDLE: ScheduledChargeState
SCHEDULED_CHARGE_STATE_SCHEDULED_TO_CHARGE: ScheduledChargeState
SCHEDULED_CHARGE_STATE_REQUEST_TO_CHARGE: ScheduledChargeState
SCHEDULED_CHARGE_UNAVAILABLE_UNKNOWN: ScheduledChargeUnavailableState
SCHEDULED_CHARGE_UNAVAILABLE_NO_REQUEST: ScheduledChargeUnavailableState
ENERGY_TYPE_UNKNOWN: EnergyType
ENERGY_TYPE_AC: EnergyType
ENERGY_TYPE_DC: EnergyType
ENERGY_TYPE_V2V: EnergyType
UPDATE_STATE_UNKNOWN: UpdateState
UPDATE_STATE_IN_PROGRESS: UpdateState
UPDATE_STATE_SUCCESS: UpdateState
UPDATE_STATE_FAILED: UpdateState
UPDATE_FAILED_DRIVE_ALLOWED: UpdateState
UPDATE_SUCCESS_WITH_WARNINGS: UpdateState
UPDATE_AVAILABILITY_UNKNOWN: UpdateAvailability
UPDATE_AVAILABLE: UpdateAvailability
ALARM_STATUS_UNKNOWN: AlarmStatus
ALARM_STATUS_DISARMED: AlarmStatus
ALARM_STATUS_ARMED: AlarmStatus
ALARM_MODE_UNKNOWN: AlarmMode
ALARM_MODE_OFF: AlarmMode
ALARM_MODE_ON: AlarmMode
ALARM_MODE_SILENT: AlarmMode
CLOUD_CONNECTION_UNKNOWN: CloudConnectionState
CLOUD_CONNECTION_CONNECTED: CloudConnectionState
CLOUD_CONNECTION_DISCONNECTED: CloudConnectionState
KEYLESS_DRIVING_UNKNOWN: KeylessDrivingState
KEYLESS_DRIVING_ON: KeylessDrivingState
KEYLESS_DRIVING_OFF: KeylessDrivingState
HVAC_POWER_UNKNOWN: HvacPower
HVAC_ON: HvacPower
HVAC_OFF: HvacPower
HVAC_PRECONDITION: HvacPower
HVAC_KEEP_TEMP: HvacPower
DEFROST_STATE_UNKNOWN: DefrostState
DEFROST_ON: DefrostState
DEFROST_OFF: DefrostState
HVAC_PRECONDITION_STATUS_UNKNOWN: HvacPreconditionStatus
HVAC_PRECONDITION_STATUS_STILL_ACTIVE: HvacPreconditionStatus
HVAC_PRECONDITION_STATUS_USER_INPUT: HvacPreconditionStatus
KEEP_CLIMATE_STATUS_UNKNOWN: KeepClimateStatus
KEEP_CLIMATE_STATUS_INACTIVE: KeepClimateStatus
KEEP_CLIMATE_STATUS_ENABLED: KeepClimateStatus
KEEP_CLIMATE_STATUS_CANCELED: KeepClimateStatus
KEEP_CLIMATE_STATUS_PET_MODE_ON: KeepClimateStatus
KEEP_CLIMATE_CONDITION_UNKNOWN: KeepClimateCondition
DRIVE_MODE_UNKNOWN: DriveMode
DRIVE_MODE_COMFORT: DriveMode
DRIVE_MODE_SWIFT: DriveMode
DRIVE_MODE_SPORT_PLUS: DriveMode
DRIVE_MODE_SERVICE: DriveMode
PRIVACY_MODE_UNKNOWN: PrivacyMode
PRIVACY_MODE_CONNECTIVITY_ENABLED: PrivacyMode
PRIVACY_MODE_CONNECTIVITY_DISABLED: PrivacyMode
GEAR_UNKNOWN: GearPosition
GEAR_PARK: GearPosition
GEAR_REVERSE: GearPosition
GEAR_NEUTRAL: GearPosition
GEAR_DRIVE: GearPosition
SHARED_TRIP_UNKNOWN: SharedTripState
SHARED_TRIP_AVAILABLE: SharedTripState
TCU_UNKNOWN: TcuState
TCU_SLEEP: TcuState
TCU_DROWSY: TcuState
TCU_FULL: TcuState
TCU_FACTORY: TcuState
LTE_TYPE_UNKNOWN: LteType
LTE_TYPE_3G: LteType
LTE_TYPE_4G: LteType
INTERNET_STATUS_UNKNOWN: InternetStatus
INTERNET_DISCONNECTED: InternetStatus
INTERNET_CONNECTED: InternetStatus
CHARGE_ACTION_UNKNOWN: ChargeAction
CHARGE_ACTION_START: ChargeAction
CHARGE_ACTION_STOP: ChargeAction
DOCUMENT_TYPE_UNKNOWN: DocumentType
DOCUMENT_TYPE_RELEASE_NOTES_PRE: DocumentType
DOCUMENT_TYPE_RELEASE_NOTES_POST: DocumentType
DOCUMENT_TYPE_OWNERS_MANUAL: DocumentType

class ChargingSubscription(_message.Message):
    __slots__ = ("name", "expiration_date", "start_date", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    expiration_date: int
    start_date: int
    status: SubscriptionStatus
    def __init__(self, name: _Optional[str] = ..., expiration_date: _Optional[int] = ..., start_date: _Optional[int] = ..., status: _Optional[_Union[SubscriptionStatus, str]] = ...) -> None: ...

class ChargingAccount(_message.Message):
    __slots__ = ("ema_id", "vehicle_id", "status", "created_at_epoch_sec", "expiry_on_epoch_sec", "vendor_name")
    EMA_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_EPOCH_SEC_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_ON_EPOCH_SEC_FIELD_NUMBER: _ClassVar[int]
    VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
    ema_id: str
    vehicle_id: str
    status: ChargingAccountStatus
    created_at_epoch_sec: int
    expiry_on_epoch_sec: int
    vendor_name: ChargingVendor
    def __init__(self, ema_id: _Optional[str] = ..., vehicle_id: _Optional[str] = ..., status: _Optional[_Union[ChargingAccountStatus, str]] = ..., created_at_epoch_sec: _Optional[int] = ..., expiry_on_epoch_sec: _Optional[int] = ..., vendor_name: _Optional[_Union[ChargingVendor, str]] = ...) -> None: ...

class SpecialIdentifiers(_message.Message):
    __slots__ = ("door_plate",)
    DOOR_PLATE_FIELD_NUMBER: _ClassVar[int]
    door_plate: str
    def __init__(self, door_plate: _Optional[str] = ...) -> None: ...

class Reservation(_message.Message):
    __slots__ = ("date",)
    DATE_FIELD_NUMBER: _ClassVar[int]
    date: int
    def __init__(self, date: _Optional[int] = ...) -> None: ...

class VehicleConfig(_message.Message):
    __slots__ = ("vin", "model", "variant", "nickname", "paint_color", "ema_id", "wheels", "ea_subscription", "charging_accounts", "country_code", "region_code", "edition", "battery", "interior", "special_identifiers", "look", "exterior_color_code", "interior_color_code", "frunk_strut", "reservation", "roof")
    VIN_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PAINT_COLOR_FIELD_NUMBER: _ClassVar[int]
    EMA_ID_FIELD_NUMBER: _ClassVar[int]
    WHEELS_FIELD_NUMBER: _ClassVar[int]
    EA_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    LOOK_FIELD_NUMBER: _ClassVar[int]
    EXTERIOR_COLOR_CODE_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_COLOR_CODE_FIELD_NUMBER: _ClassVar[int]
    FRUNK_STRUT_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    ROOF_FIELD_NUMBER: _ClassVar[int]
    vin: str
    model: Model
    variant: ModelVariant
    nickname: str
    paint_color: PaintColor
    ema_id: str
    wheels: Wheels
    ea_subscription: ChargingSubscription
    charging_accounts: _containers.RepeatedCompositeFieldContainer[ChargingAccount]
    country_code: str
    region_code: str
    edition: Edition
    battery: BatteryType
    interior: Interior
    special_identifiers: SpecialIdentifiers
    look: Look
    exterior_color_code: str
    interior_color_code: str
    frunk_strut: StrutType
    reservation: Reservation
    roof: RoofType
    def __init__(self, vin: _Optional[str] = ..., model: _Optional[_Union[Model, str]] = ..., variant: _Optional[_Union[ModelVariant, str]] = ..., nickname: _Optional[str] = ..., paint_color: _Optional[_Union[PaintColor, str]] = ..., ema_id: _Optional[str] = ..., wheels: _Optional[_Union[Wheels, str]] = ..., ea_subscription: _Optional[_Union[ChargingSubscription, _Mapping]] = ..., charging_accounts: _Optional[_Iterable[_Union[ChargingAccount, _Mapping]]] = ..., country_code: _Optional[str] = ..., region_code: _Optional[str] = ..., edition: _Optional[_Union[Edition, str]] = ..., battery: _Optional[_Union[BatteryType, str]] = ..., interior: _Optional[_Union[Interior, str]] = ..., special_identifiers: _Optional[_Union[SpecialIdentifiers, _Mapping]] = ..., look: _Optional[_Union[Look, str]] = ..., exterior_color_code: _Optional[str] = ..., interior_color_code: _Optional[str] = ..., frunk_strut: _Optional[_Union[StrutType, str]] = ..., reservation: _Optional[_Union[Reservation, _Mapping]] = ..., roof: _Optional[_Union[RoofType, str]] = ...) -> None: ...

class BatteryState(_message.Message):
    __slots__ = ("remaining_range", "charge_percent", "kwhr", "capacity_kwhr", "battery_health", "low_charge_level", "critical_charge_level", "unavailable_range", "preconditioning_status", "preconditioning_time_remaining")
    REMAINING_RANGE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    KWHR_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_KWHR_FIELD_NUMBER: _ClassVar[int]
    BATTERY_HEALTH_FIELD_NUMBER: _ClassVar[int]
    LOW_CHARGE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_CHARGE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_RANGE_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    remaining_range: float
    charge_percent: float
    kwhr: float
    capacity_kwhr: float
    battery_health: WarningState
    low_charge_level: WarningState
    critical_charge_level: WarningState
    unavailable_range: float
    preconditioning_status: BatteryPreconStatus
    preconditioning_time_remaining: int
    def __init__(self, remaining_range: _Optional[float] = ..., charge_percent: _Optional[float] = ..., kwhr: _Optional[float] = ..., capacity_kwhr: _Optional[float] = ..., battery_health: _Optional[_Union[WarningState, str]] = ..., low_charge_level: _Optional[_Union[WarningState, str]] = ..., critical_charge_level: _Optional[_Union[WarningState, str]] = ..., unavailable_range: _Optional[float] = ..., preconditioning_status: _Optional[_Union[BatteryPreconStatus, str]] = ..., preconditioning_time_remaining: _Optional[int] = ...) -> None: ...

class CabinState(_message.Message):
    __slots__ = ("interior_temp", "exterior_temp")
    INTERIOR_TEMP_FIELD_NUMBER: _ClassVar[int]
    EXTERIOR_TEMP_FIELD_NUMBER: _ClassVar[int]
    interior_temp: float
    exterior_temp: float
    def __init__(self, interior_temp: _Optional[float] = ..., exterior_temp: _Optional[float] = ...) -> None: ...

class BodyState(_message.Message):
    __slots__ = ("door_locks", "front_cargo", "rear_cargo", "front_left_door", "front_right_door", "rear_left_door", "rear_right_door", "charge_port", "walkaway_lock", "access_type_status")
    DOOR_LOCKS_FIELD_NUMBER: _ClassVar[int]
    FRONT_CARGO_FIELD_NUMBER: _ClassVar[int]
    REAR_CARGO_FIELD_NUMBER: _ClassVar[int]
    FRONT_LEFT_DOOR_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_DOOR_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_DOOR_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_DOOR_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_FIELD_NUMBER: _ClassVar[int]
    WALKAWAY_LOCK_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_STATUS_FIELD_NUMBER: _ClassVar[int]
    door_locks: LockState
    front_cargo: DoorState
    rear_cargo: DoorState
    front_left_door: DoorState
    front_right_door: DoorState
    rear_left_door: DoorState
    rear_right_door: DoorState
    charge_port: DoorState
    walkaway_lock: WalkawayState
    access_type_status: AccessRequest
    def __init__(self, door_locks: _Optional[_Union[LockState, str]] = ..., front_cargo: _Optional[_Union[DoorState, str]] = ..., rear_cargo: _Optional[_Union[DoorState, str]] = ..., front_left_door: _Optional[_Union[DoorState, str]] = ..., front_right_door: _Optional[_Union[DoorState, str]] = ..., rear_left_door: _Optional[_Union[DoorState, str]] = ..., rear_right_door: _Optional[_Union[DoorState, str]] = ..., charge_port: _Optional[_Union[DoorState, str]] = ..., walkaway_lock: _Optional[_Union[WalkawayState, str]] = ..., access_type_status: _Optional[_Union[AccessRequest, str]] = ...) -> None: ...

class ChassisState(_message.Message):
    __slots__ = ("odometer_km", "front_left_tire_pressure_bar", "front_right_tire_pressure_bar", "rear_left_tire_pressure_bar", "rear_right_tire_pressure_bar", "headlights", "hard_warn_left_front", "hard_warn_left_rear", "hard_warn_right_front", "hard_warn_right_rear", "soft_warn_left_front", "soft_warn_left_rear", "soft_warn_right_front", "soft_warn_right_rear", "software_version")
    ODOMETER_KM_FIELD_NUMBER: _ClassVar[int]
    FRONT_LEFT_TIRE_PRESSURE_BAR_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_TIRE_PRESSURE_BAR_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_TIRE_PRESSURE_BAR_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_TIRE_PRESSURE_BAR_FIELD_NUMBER: _ClassVar[int]
    HEADLIGHTS_FIELD_NUMBER: _ClassVar[int]
    HARD_WARN_LEFT_FRONT_FIELD_NUMBER: _ClassVar[int]
    HARD_WARN_LEFT_REAR_FIELD_NUMBER: _ClassVar[int]
    HARD_WARN_RIGHT_FRONT_FIELD_NUMBER: _ClassVar[int]
    HARD_WARN_RIGHT_REAR_FIELD_NUMBER: _ClassVar[int]
    SOFT_WARN_LEFT_FRONT_FIELD_NUMBER: _ClassVar[int]
    SOFT_WARN_LEFT_REAR_FIELD_NUMBER: _ClassVar[int]
    SOFT_WARN_RIGHT_FRONT_FIELD_NUMBER: _ClassVar[int]
    SOFT_WARN_RIGHT_REAR_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    odometer_km: float
    front_left_tire_pressure_bar: float
    front_right_tire_pressure_bar: float
    rear_left_tire_pressure_bar: float
    rear_right_tire_pressure_bar: float
    headlights: LightState
    hard_warn_left_front: WarningState
    hard_warn_left_rear: WarningState
    hard_warn_right_front: WarningState
    hard_warn_right_rear: WarningState
    soft_warn_left_front: WarningState
    soft_warn_left_rear: WarningState
    soft_warn_right_front: WarningState
    soft_warn_right_rear: WarningState
    software_version: str
    def __init__(self, odometer_km: _Optional[float] = ..., front_left_tire_pressure_bar: _Optional[float] = ..., front_right_tire_pressure_bar: _Optional[float] = ..., rear_left_tire_pressure_bar: _Optional[float] = ..., rear_right_tire_pressure_bar: _Optional[float] = ..., headlights: _Optional[_Union[LightState, str]] = ..., hard_warn_left_front: _Optional[_Union[WarningState, str]] = ..., hard_warn_left_rear: _Optional[_Union[WarningState, str]] = ..., hard_warn_right_front: _Optional[_Union[WarningState, str]] = ..., hard_warn_right_rear: _Optional[_Union[WarningState, str]] = ..., soft_warn_left_front: _Optional[_Union[WarningState, str]] = ..., soft_warn_left_rear: _Optional[_Union[WarningState, str]] = ..., soft_warn_right_front: _Optional[_Union[WarningState, str]] = ..., soft_warn_right_rear: _Optional[_Union[WarningState, str]] = ..., software_version: _Optional[str] = ...) -> None: ...

class ChargingState(_message.Message):
    __slots__ = ("charge_state", "energy_type", "charge_session_mi", "charge_session_kwh", "session_minutes_remaining", "charge_limit", "cable_lock", "charge_rate_kwh_precise", "charge_rate_mph_precise", "charge_rate_miles_min_precise", "charge_limit_percent", "charge_scheduled_time", "scheduled_charge", "scheduled_charge_unavailable")
    CHARGE_STATE_FIELD_NUMBER: _ClassVar[int]
    ENERGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SESSION_MI_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SESSION_KWH_FIELD_NUMBER: _ClassVar[int]
    SESSION_MINUTES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CABLE_LOCK_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_KWH_PRECISE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_MPH_PRECISE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_MILES_MIN_PRECISE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGE_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    charge_state: ChargeState
    energy_type: EnergyType
    charge_session_mi: float
    charge_session_kwh: float
    session_minutes_remaining: int
    charge_limit: int
    cable_lock: LockState
    charge_rate_kwh_precise: float
    charge_rate_mph_precise: float
    charge_rate_miles_min_precise: float
    charge_limit_percent: float
    charge_scheduled_time: int
    scheduled_charge: ScheduledChargeState
    scheduled_charge_unavailable: ScheduledChargeUnavailableState
    def __init__(self, charge_state: _Optional[_Union[ChargeState, str]] = ..., energy_type: _Optional[_Union[EnergyType, str]] = ..., charge_session_mi: _Optional[float] = ..., charge_session_kwh: _Optional[float] = ..., session_minutes_remaining: _Optional[int] = ..., charge_limit: _Optional[int] = ..., cable_lock: _Optional[_Union[LockState, str]] = ..., charge_rate_kwh_precise: _Optional[float] = ..., charge_rate_mph_precise: _Optional[float] = ..., charge_rate_miles_min_precise: _Optional[float] = ..., charge_limit_percent: _Optional[float] = ..., charge_scheduled_time: _Optional[int] = ..., scheduled_charge: _Optional[_Union[ScheduledChargeState, str]] = ..., scheduled_charge_unavailable: _Optional[_Union[ScheduledChargeUnavailableState, str]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Gps(_message.Message):
    __slots__ = ("location", "elevation", "position_time", "heading_precise")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    POSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    HEADING_PRECISE_FIELD_NUMBER: _ClassVar[int]
    location: Location
    elevation: int
    position_time: int
    heading_precise: float
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., elevation: _Optional[int] = ..., position_time: _Optional[int] = ..., heading_precise: _Optional[float] = ...) -> None: ...

class SoftwareUpdate(_message.Message):
    __slots__ = ("version_available", "install_duration_minutes", "percent_complete", "state", "version_available_raw", "update_available", "scheduled_start_time_sec")
    VERSION_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    INSTALL_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_AVAILABLE_RAW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_START_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    version_available: str
    install_duration_minutes: int
    percent_complete: int
    state: UpdateState
    version_available_raw: int
    update_available: UpdateAvailability
    scheduled_start_time_sec: int
    def __init__(self, version_available: _Optional[str] = ..., install_duration_minutes: _Optional[int] = ..., percent_complete: _Optional[int] = ..., state: _Optional[_Union[UpdateState, str]] = ..., version_available_raw: _Optional[int] = ..., update_available: _Optional[_Union[UpdateAvailability, str]] = ..., scheduled_start_time_sec: _Optional[int] = ...) -> None: ...

class AlarmState(_message.Message):
    __slots__ = ("status", "mode")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    status: AlarmStatus
    mode: AlarmMode
    def __init__(self, status: _Optional[_Union[AlarmStatus, str]] = ..., mode: _Optional[_Union[AlarmMode, str]] = ...) -> None: ...

class HvacState(_message.Message):
    __slots__ = ("power", "defrost", "precondition_status", "keep_climate_status")
    POWER_FIELD_NUMBER: _ClassVar[int]
    DEFROST_FIELD_NUMBER: _ClassVar[int]
    PRECONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    KEEP_CLIMATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    power: HvacPower
    defrost: DefrostState
    precondition_status: HvacPreconditionStatus
    keep_climate_status: KeepClimateStatus
    def __init__(self, power: _Optional[_Union[HvacPower, str]] = ..., defrost: _Optional[_Union[DefrostState, str]] = ..., precondition_status: _Optional[_Union[HvacPreconditionStatus, str]] = ..., keep_climate_status: _Optional[_Union[KeepClimateStatus, str]] = ...) -> None: ...

class MobileAppReqState(_message.Message):
    __slots__ = ("alarm_set_request", "charge_port_request", "frunk_cargo_request", "hvac_defrost", "hvac_precondition", "light_request", "shared_trip_request", "trunk_cargo_request", "vehicle_unlock_request")
    ALARM_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FRUNK_CARGO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HVAC_DEFROST_FIELD_NUMBER: _ClassVar[int]
    HVAC_PRECONDITION_FIELD_NUMBER: _ClassVar[int]
    LIGHT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SHARED_TRIP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRUNK_CARGO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_UNLOCK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    alarm_set_request: AlarmMode
    charge_port_request: DoorState
    frunk_cargo_request: DoorState
    hvac_defrost: DefrostState
    hvac_precondition: HvacPower
    light_request: LightAction
    shared_trip_request: SharedTripState
    trunk_cargo_request: DoorState
    vehicle_unlock_request: LockState
    def __init__(self, alarm_set_request: _Optional[_Union[AlarmMode, str]] = ..., charge_port_request: _Optional[_Union[DoorState, str]] = ..., frunk_cargo_request: _Optional[_Union[DoorState, str]] = ..., hvac_defrost: _Optional[_Union[DefrostState, str]] = ..., hvac_precondition: _Optional[_Union[HvacPower, str]] = ..., light_request: _Optional[_Union[LightAction, str]] = ..., shared_trip_request: _Optional[_Union[SharedTripState, str]] = ..., trunk_cargo_request: _Optional[_Union[DoorState, str]] = ..., vehicle_unlock_request: _Optional[_Union[LockState, str]] = ...) -> None: ...

class TcuInternetState(_message.Message):
    __slots__ = ("lte_type", "lte_status", "wifi_status", "lte_rssi", "wifi_rssi")
    LTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LTE_STATUS_FIELD_NUMBER: _ClassVar[int]
    WIFI_STATUS_FIELD_NUMBER: _ClassVar[int]
    LTE_RSSI_FIELD_NUMBER: _ClassVar[int]
    WIFI_RSSI_FIELD_NUMBER: _ClassVar[int]
    lte_type: LteType
    lte_status: InternetStatus
    wifi_status: InternetStatus
    lte_rssi: int
    wifi_rssi: int
    def __init__(self, lte_type: _Optional[_Union[LteType, str]] = ..., lte_status: _Optional[_Union[InternetStatus, str]] = ..., wifi_status: _Optional[_Union[InternetStatus, str]] = ..., lte_rssi: _Optional[int] = ..., wifi_rssi: _Optional[int] = ...) -> None: ...

class VehicleState(_message.Message):
    __slots__ = ("battery", "power", "cabin", "body", "last_updated_ms", "chassis", "charging", "gps", "software_update", "alarm", "cloud_connection", "keyless_driving", "hvac", "drive_mode", "privacy_mode", "gear_position", "mobile_app_request", "tcu", "tcu_internet")
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    CABIN_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_MS_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_FIELD_NUMBER: _ClassVar[int]
    CHARGING_FIELD_NUMBER: _ClassVar[int]
    GPS_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ALARM_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    KEYLESS_DRIVING_FIELD_NUMBER: _ClassVar[int]
    HVAC_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MODE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_MODE_FIELD_NUMBER: _ClassVar[int]
    GEAR_POSITION_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TCU_FIELD_NUMBER: _ClassVar[int]
    TCU_INTERNET_FIELD_NUMBER: _ClassVar[int]
    battery: BatteryState
    power: PowerState
    cabin: CabinState
    body: BodyState
    last_updated_ms: int
    chassis: ChassisState
    charging: ChargingState
    gps: Gps
    software_update: SoftwareUpdate
    alarm: AlarmState
    cloud_connection: CloudConnectionState
    keyless_driving: KeylessDrivingState
    hvac: HvacState
    drive_mode: DriveMode
    privacy_mode: PrivacyMode
    gear_position: GearPosition
    mobile_app_request: MobileAppReqState
    tcu: TcuState
    tcu_internet: TcuInternetState
    def __init__(self, battery: _Optional[_Union[BatteryState, _Mapping]] = ..., power: _Optional[_Union[PowerState, str]] = ..., cabin: _Optional[_Union[CabinState, _Mapping]] = ..., body: _Optional[_Union[BodyState, _Mapping]] = ..., last_updated_ms: _Optional[int] = ..., chassis: _Optional[_Union[ChassisState, _Mapping]] = ..., charging: _Optional[_Union[ChargingState, _Mapping]] = ..., gps: _Optional[_Union[Gps, _Mapping]] = ..., software_update: _Optional[_Union[SoftwareUpdate, _Mapping]] = ..., alarm: _Optional[_Union[AlarmState, _Mapping]] = ..., cloud_connection: _Optional[_Union[CloudConnectionState, str]] = ..., keyless_driving: _Optional[_Union[KeylessDrivingState, str]] = ..., hvac: _Optional[_Union[HvacState, _Mapping]] = ..., drive_mode: _Optional[_Union[DriveMode, str]] = ..., privacy_mode: _Optional[_Union[PrivacyMode, str]] = ..., gear_position: _Optional[_Union[GearPosition, str]] = ..., mobile_app_request: _Optional[_Union[MobileAppReqState, _Mapping]] = ..., tcu: _Optional[_Union[TcuState, str]] = ..., tcu_internet: _Optional[_Union[TcuInternetState, _Mapping]] = ...) -> None: ...

class Vehicle(_message.Message):
    __slots__ = ("vehicle_id", "access_level", "config", "state")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    access_level: AccessLevel
    config: VehicleConfig
    state: VehicleState
    def __init__(self, vehicle_id: _Optional[str] = ..., access_level: _Optional[_Union[AccessLevel, str]] = ..., config: _Optional[_Union[VehicleConfig, _Mapping]] = ..., state: _Optional[_Union[VehicleState, _Mapping]] = ...) -> None: ...

class ApplySoftwareUpdateRequest(_message.Message):
    __slots__ = ("vehicle_id",)
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    def __init__(self, vehicle_id: _Optional[str] = ...) -> None: ...

class ApplySoftwareUpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelScheduledUpdateRequest(_message.Message):
    __slots__ = ("vehicle_id",)
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    def __init__(self, vehicle_id: _Optional[str] = ...) -> None: ...

class CancelScheduledUpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargeControlRequest(_message.Message):
    __slots__ = ("action", "vehicle_id")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    action: ChargeAction
    vehicle_id: str
    def __init__(self, action: _Optional[_Union[ChargeAction, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class ChargeControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ControlChargePortRequest(_message.Message):
    __slots__ = ("closure_state", "vehicle_id")
    CLOSURE_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    closure_state: DoorState
    vehicle_id: str
    def __init__(self, closure_state: _Optional[_Union[DoorState, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class ControlChargePortResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DoorLocksControlRequest(_message.Message):
    __slots__ = ("door_location", "lock_state", "vehicle_id")
    DOOR_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    door_location: _containers.RepeatedScalarFieldContainer[int]
    lock_state: LockState
    vehicle_id: str
    def __init__(self, door_location: _Optional[_Iterable[int]] = ..., lock_state: _Optional[_Union[LockState, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class DoorLocksControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FrontCargoControlRequest(_message.Message):
    __slots__ = ("closure_state", "vehicle_id")
    CLOSURE_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    closure_state: DoorState
    vehicle_id: str
    def __init__(self, closure_state: _Optional[_Union[DoorState, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class FrontCargoControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DocumentInfoUnknown(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class DocumentInfo(_message.Message):
    __slots__ = ("type", "version", "description", "unknown")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    type: DocumentType
    version: str
    description: str
    unknown: DocumentInfoUnknown
    def __init__(self, type: _Optional[_Union[DocumentType, str]] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., unknown: _Optional[_Union[DocumentInfoUnknown, _Mapping]] = ...) -> None: ...

class GetDocumentInfoRequest(_message.Message):
    __slots__ = ("version", "document_type")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    version: str
    document_type: DocumentType
    def __init__(self, version: _Optional[str] = ..., document_type: _Optional[_Union[DocumentType, str]] = ...) -> None: ...

class GetDocumentInfoResponse(_message.Message):
    __slots__ = ("url", "info")
    URL_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    url: str
    info: DocumentInfo
    def __init__(self, url: _Optional[str] = ..., info: _Optional[_Union[DocumentInfo, _Mapping]] = ...) -> None: ...

class GetVehicleStateRequest(_message.Message):
    __slots__ = ("vehicle_id",)
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    def __init__(self, vehicle_id: _Optional[str] = ...) -> None: ...

class GetVehicleStateResponse(_message.Message):
    __slots__ = ("vehicle_id", "state")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    state: VehicleState
    def __init__(self, vehicle_id: _Optional[str] = ..., state: _Optional[_Union[VehicleState, _Mapping]] = ...) -> None: ...

class HonkHornRequest(_message.Message):
    __slots__ = ("vehicle_id",)
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    def __init__(self, vehicle_id: _Optional[str] = ...) -> None: ...

class HonkHornResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HvacDefrostControlRequest(_message.Message):
    __slots__ = ("vehicle_id", "hvac_defrost")
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    HVAC_DEFROST_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    hvac_defrost: DefrostState
    def __init__(self, vehicle_id: _Optional[str] = ..., hvac_defrost: _Optional[_Union[DefrostState, str]] = ...) -> None: ...

class HvacDefrostControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LightsControlRequest(_message.Message):
    __slots__ = ("action", "vehicle_id")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    action: LightAction
    vehicle_id: str
    def __init__(self, action: _Optional[_Union[LightAction, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class LightsControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RearCargoControlRequest(_message.Message):
    __slots__ = ("closure_state", "vehicle_id")
    CLOSURE_STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    closure_state: DoorState
    vehicle_id: str
    def __init__(self, closure_state: _Optional[_Union[DoorState, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class RearCargoControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SecurityAlarmControlRequest(_message.Message):
    __slots__ = ("mode", "vehicle_id")
    MODE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    mode: AlarmMode
    vehicle_id: str
    def __init__(self, mode: _Optional[_Union[AlarmMode, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class SecurityAlarmControlResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCabinTemperatureRequest(_message.Message):
    __slots__ = ("temperature", "state", "vehicle_id")
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    temperature: float
    state: HvacPower
    vehicle_id: str
    def __init__(self, temperature: _Optional[float] = ..., state: _Optional[_Union[HvacPower, str]] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class SetCabinTemperatureResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetChargeLimitRequest(_message.Message):
    __slots__ = ("limit_percent", "vehicle_id")
    LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    limit_percent: int
    vehicle_id: str
    def __init__(self, limit_percent: _Optional[int] = ..., vehicle_id: _Optional[str] = ...) -> None: ...

class SetChargeLimitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WakeupVehicleRequest(_message.Message):
    __slots__ = ("vehicle_id",)
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    vehicle_id: str
    def __init__(self, vehicle_id: _Optional[str] = ...) -> None: ...

class WakeupVehicleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
