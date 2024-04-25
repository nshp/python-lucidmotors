# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicle_state_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bvehicle_state_service.proto\x12\x14mobilegateway.protos\"\x8b\x01\n\x14\x43hargingSubscription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x65xpiration_date\x18\x02 \x01(\x04\x12\x12\n\nstart_date\x18\x03 \x01(\x04\x12\x38\n\x06status\x18\x04 \x01(\x0e\x32(.mobilegateway.protos.SubscriptionStatus\"\xe8\x01\n\x0f\x43hargingAccount\x12\x0e\n\x06\x65ma_id\x18\x01 \x01(\t\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\x12;\n\x06status\x18\x03 \x01(\x0e\x32+.mobilegateway.protos.ChargingAccountStatus\x12\x1c\n\x14\x63reated_at_epoch_sec\x18\x04 \x01(\x04\x12\x1b\n\x13\x65xpiry_on_epoch_sec\x18\x05 \x01(\x04\x12\x39\n\x0bvendor_name\x18\x06 \x01(\x0e\x32$.mobilegateway.protos.ChargingVendor\"(\n\x12SpecialIdentifiers\x12\x12\n\ndoor_plate\x18\x01 \x01(\t\"\x1b\n\x0bReservation\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\x04\"\x93\x07\n\rVehicleConfig\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12*\n\x05model\x18\x02 \x01(\x0e\x32\x1b.mobilegateway.protos.Model\x12\x33\n\x07variant\x18\x03 \x01(\x0e\x32\".mobilegateway.protos.ModelVariant\x12\x10\n\x08nickname\x18\x05 \x01(\t\x12\x35\n\x0bpaint_color\x18\x06 \x01(\x0e\x32 .mobilegateway.protos.PaintColor\x12\x0e\n\x06\x65ma_id\x18\x07 \x01(\t\x12,\n\x06wheels\x18\x08 \x01(\x0e\x32\x1c.mobilegateway.protos.Wheels\x12\x43\n\x0f\x65\x61_subscription\x18\t \x01(\x0b\x32*.mobilegateway.protos.ChargingSubscription\x12@\n\x11\x63harging_accounts\x18\n \x03(\x0b\x32%.mobilegateway.protos.ChargingAccount\x12\x14\n\x0c\x63ountry_code\x18\x0b \x01(\t\x12\x13\n\x0bregion_code\x18\x0c \x01(\t\x12.\n\x07\x65\x64ition\x18\r \x01(\x0e\x32\x1d.mobilegateway.protos.Edition\x12\x32\n\x07\x62\x61ttery\x18\x0e \x01(\x0e\x32!.mobilegateway.protos.BatteryType\x12\x30\n\x08interior\x18\x0f \x01(\x0e\x32\x1e.mobilegateway.protos.Interior\x12\x45\n\x13special_identifiers\x18\x10 \x01(\x0b\x32(.mobilegateway.protos.SpecialIdentifiers\x12(\n\x04look\x18\x11 \x01(\x0e\x32\x1a.mobilegateway.protos.Look\x12\x1b\n\x13\x65xterior_color_code\x18\x12 \x01(\t\x12\x1b\n\x13interior_color_code\x18\x13 \x01(\t\x12\x34\n\x0b\x66runk_strut\x18\x14 \x01(\x0e\x32\x1f.mobilegateway.protos.StrutType\x12\x36\n\x0breservation\x18\x15 \x01(\x0b\x32!.mobilegateway.protos.Reservation\x12,\n\x04roof\x18\x16 \x01(\x0e\x32\x1e.mobilegateway.protos.RoofType\"\xaf\x03\n\x0c\x42\x61tteryState\x12\x17\n\x0fremaining_range\x18\x01 \x01(\x01\x12\x16\n\x0e\x63harge_percent\x18\x02 \x01(\x01\x12\x0c\n\x04kwhr\x18\x03 \x01(\x01\x12\x15\n\rcapacity_kwhr\x18\x04 \x01(\x01\x12:\n\x0e\x62\x61ttery_health\x18\x05 \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12<\n\x10low_charge_level\x18\x06 \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12\x41\n\x15\x63ritical_charge_level\x18\x07 \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12\x19\n\x11unavailable_range\x18\x08 \x01(\x01\x12I\n\x16preconditioning_status\x18\t \x01(\x0e\x32).mobilegateway.protos.BatteryPreconStatus\x12&\n\x1epreconditioning_time_remaining\x18\n \x01(\r\":\n\nCabinState\x12\x15\n\rinterior_temp\x18\x01 \x01(\x01\x12\x15\n\rexterior_temp\x18\x02 \x01(\x01\"\xc6\x04\n\tBodyState\x12\x33\n\ndoor_locks\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.LockState\x12\x34\n\x0b\x66ront_cargo\x18\x02 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x33\n\nrear_cargo\x18\x03 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x38\n\x0f\x66ront_left_door\x18\x04 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x39\n\x10\x66ront_right_door\x18\x05 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x37\n\x0erear_left_door\x18\x06 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x38\n\x0frear_right_door\x18\x07 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x34\n\x0b\x63harge_port\x18\x08 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12:\n\rwalkaway_lock\x18\t \x01(\x0e\x32#.mobilegateway.protos.WalkawayState\x12?\n\x12\x61\x63\x63\x65ss_type_status\x18\n \x01(\x0e\x32#.mobilegateway.protos.AccessRequest\"\x9b\x06\n\x0c\x43hassisState\x12\x13\n\x0bodometer_km\x18\x01 \x01(\x01\x12$\n\x1c\x66ront_left_tire_pressure_bar\x18\x02 \x01(\x01\x12%\n\x1d\x66ront_right_tire_pressure_bar\x18\x03 \x01(\x01\x12#\n\x1brear_left_tire_pressure_bar\x18\x04 \x01(\x01\x12$\n\x1crear_right_tire_pressure_bar\x18\x05 \x01(\x01\x12\x34\n\nheadlights\x18\x06 \x01(\x0e\x32 .mobilegateway.protos.LightState\x12@\n\x14hard_warn_left_front\x18\x08 \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12?\n\x13hard_warn_left_rear\x18\t \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12\x41\n\x15hard_warn_right_front\x18\n \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12@\n\x14hard_warn_right_rear\x18\x0b \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12@\n\x14soft_warn_left_front\x18\x0c \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12?\n\x13soft_warn_left_rear\x18\r \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12\x41\n\x15soft_warn_right_front\x18\x0e \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12@\n\x14soft_warn_right_rear\x18\x0f \x01(\x0e\x32\".mobilegateway.protos.WarningState\x12\x18\n\x10software_version\x18\x10 \x01(\t\"\xed\x04\n\rChargingState\x12\x37\n\x0c\x63harge_state\x18\x01 \x01(\x0e\x32!.mobilegateway.protos.ChargeState\x12\x35\n\x0b\x65nergy_type\x18\x02 \x01(\x0e\x32 .mobilegateway.protos.EnergyType\x12\x19\n\x11\x63harge_session_mi\x18\x05 \x01(\x01\x12\x1a\n\x12\x63harge_session_kwh\x18\x06 \x01(\x01\x12!\n\x19session_minutes_remaining\x18\x07 \x01(\r\x12\x14\n\x0c\x63harge_limit\x18\x08 \x01(\r\x12\x33\n\ncable_lock\x18\n \x01(\x0e\x32\x1f.mobilegateway.protos.LockState\x12\x1f\n\x17\x63harge_rate_kwh_precise\x18\x0b \x01(\x01\x12\x1f\n\x17\x63harge_rate_mph_precise\x18\x0c \x01(\x01\x12%\n\x1d\x63harge_rate_miles_min_precise\x18\r \x01(\x01\x12\x1c\n\x14\x63harge_limit_percent\x18\x0e \x01(\x01\x12\x1d\n\x15\x63harge_scheduled_time\x18\x10 \x01(\r\x12\x44\n\x10scheduled_charge\x18\x11 \x01(\x0e\x32*.mobilegateway.protos.ScheduledChargeState\x12[\n\x1cscheduled_charge_unavailable\x18\x12 \x01(\x0e\x32\x35.mobilegateway.protos.ScheduledChargeUnavailableState\"/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\"z\n\x03Gps\x12\x30\n\x08location\x18\x01 \x01(\x0b\x32\x1e.mobilegateway.protos.Location\x12\x11\n\televation\x18\x02 \x01(\x05\x12\x15\n\rposition_time\x18\x04 \x01(\x04\x12\x17\n\x0fheading_precise\x18\x05 \x01(\x01\"\x9e\x02\n\x0eSoftwareUpdate\x12\x19\n\x11version_available\x18\x01 \x01(\t\x12 \n\x18install_duration_minutes\x18\x02 \x01(\r\x12\x18\n\x10percent_complete\x18\x04 \x01(\r\x12\x30\n\x05state\x18\x05 \x01(\x0e\x32!.mobilegateway.protos.UpdateState\x12\x1d\n\x15version_available_raw\x18\x08 \x01(\r\x12\x42\n\x10update_available\x18\t \x01(\x0e\x32(.mobilegateway.protos.UpdateAvailability\x12 \n\x18scheduled_start_time_sec\x18\n \x01(\x04\"n\n\nAlarmState\x12\x31\n\x06status\x18\x01 \x01(\x0e\x32!.mobilegateway.protos.AlarmStatus\x12-\n\x04mode\x18\x02 \x01(\x0e\x32\x1f.mobilegateway.protos.AlarmMode\"\x81\x02\n\tHvacState\x12.\n\x05power\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.HvacPower\x12\x33\n\x07\x64\x65\x66rost\x18\x02 \x01(\x0e\x32\".mobilegateway.protos.DefrostState\x12I\n\x13precondition_status\x18\x03 \x01(\x0e\x32,.mobilegateway.protos.HvacPreconditionStatus\x12\x44\n\x13keep_climate_status\x18\x05 \x01(\x0e\x32\'.mobilegateway.protos.KeepClimateStatus\"\xf7\x04\n\x11MobileAppReqState\x12:\n\x11\x61larm_set_request\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.AlarmMode\x12<\n\x13\x63harge_port_request\x18\x02 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12<\n\x13\x66runk_cargo_request\x18\t \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x38\n\x0chvac_defrost\x18\x0b \x01(\x0e\x32\".mobilegateway.protos.DefrostState\x12:\n\x11hvac_precondition\x18\x0c \x01(\x0e\x32\x1f.mobilegateway.protos.HvacPower\x12\x38\n\rlight_request\x18\r \x01(\x0e\x32!.mobilegateway.protos.LightAction\x12\x37\n\rpanic_request\x18\x0e \x01(\x0e\x32 .mobilegateway.protos.PanicState\x12\x42\n\x13shared_trip_request\x18\x0f \x01(\x0e\x32%.mobilegateway.protos.SharedTripState\x12<\n\x13trunk_cargo_request\x18\x10 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12?\n\x16vehicle_unlock_request\x18\x11 \x01(\x0e\x32\x1f.mobilegateway.protos.LockState\"\x82\x02\n\x10TcuInternetState\x12/\n\x08lte_type\x18\x01 \x01(\x0e\x32\x1d.mobilegateway.protos.LteType\x12\x38\n\nlte_status\x18\x02 \x01(\x0e\x32$.mobilegateway.protos.InternetStatus\x12\x39\n\x0bwifi_status\x18\x03 \x01(\x0e\x32$.mobilegateway.protos.InternetStatus\x12\x15\n\x08lte_rssi\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\twifi_rssi\x18\x05 \x01(\x05H\x01\x88\x01\x01\x42\x0b\n\t_lte_rssiB\x0c\n\n_wifi_rssi\"\x83\x08\n\x0cVehicleState\x12\x33\n\x07\x62\x61ttery\x18\x01 \x01(\x0b\x32\".mobilegateway.protos.BatteryState\x12/\n\x05power\x18\x02 \x01(\x0e\x32 .mobilegateway.protos.PowerState\x12/\n\x05\x63\x61\x62in\x18\x03 \x01(\x0b\x32 .mobilegateway.protos.CabinState\x12-\n\x04\x62ody\x18\x04 \x01(\x0b\x32\x1f.mobilegateway.protos.BodyState\x12\x17\n\x0flast_updated_ms\x18\x05 \x01(\x04\x12\x33\n\x07\x63hassis\x18\x06 \x01(\x0b\x32\".mobilegateway.protos.ChassisState\x12\x35\n\x08\x63harging\x18\x08 \x01(\x0b\x32#.mobilegateway.protos.ChargingState\x12&\n\x03gps\x18\x0b \x01(\x0b\x32\x19.mobilegateway.protos.Gps\x12=\n\x0fsoftware_update\x18\x0c \x01(\x0b\x32$.mobilegateway.protos.SoftwareUpdate\x12/\n\x05\x61larm\x18\r \x01(\x0b\x32 .mobilegateway.protos.AlarmState\x12\x44\n\x10\x63loud_connection\x18\x0f \x01(\x0e\x32*.mobilegateway.protos.CloudConnectionState\x12\x42\n\x0fkeyless_driving\x18\x10 \x01(\x0e\x32).mobilegateway.protos.KeylessDrivingState\x12-\n\x04hvac\x18\x11 \x01(\x0b\x32\x1f.mobilegateway.protos.HvacState\x12\x33\n\ndrive_mode\x18\x12 \x01(\x0e\x32\x1f.mobilegateway.protos.DriveMode\x12\x37\n\x0cprivacy_mode\x18\x13 \x01(\x0e\x32!.mobilegateway.protos.PrivacyMode\x12\x39\n\rgear_position\x18\x14 \x01(\x0e\x32\".mobilegateway.protos.GearPosition\x12\x43\n\x12mobile_app_request\x18\x15 \x01(\x0b\x32\'.mobilegateway.protos.MobileAppReqState\x12+\n\x03tcu\x18\x16 \x01(\x0e\x32\x1e.mobilegateway.protos.TcuState\x12<\n\x0ctcu_internet\x18\x17 \x01(\x0b\x32&.mobilegateway.protos.TcuInternetState\"\xbe\x01\n\x07Vehicle\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x37\n\x0c\x61\x63\x63\x65ss_level\x18\x02 \x01(\x0e\x32!.mobilegateway.protos.AccessLevel\x12\x33\n\x06\x63onfig\x18\x03 \x01(\x0b\x32#.mobilegateway.protos.VehicleConfig\x12\x31\n\x05state\x18\x04 \x01(\x0b\x32\".mobilegateway.protos.VehicleState\"0\n\x1a\x41pplySoftwareUpdateRequest\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\"\x1d\n\x1b\x41pplySoftwareUpdateResponse\"2\n\x1c\x43\x61ncelScheduledUpdateRequest\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\"\x1f\n\x1d\x43\x61ncelScheduledUpdateResponse\"^\n\x14\x43hargeControlRequest\x12\x32\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\".mobilegateway.protos.ChargeAction\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x17\n\x15\x43hargeControlResponse\"f\n\x18\x43ontrolChargePortRequest\x12\x36\n\rclosure_state\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x1b\n\x19\x43ontrolChargePortResponse\"y\n\x17\x44oorLocksControlRequest\x12\x15\n\rdoor_location\x18\x01 \x03(\x05\x12\x33\n\nlock_state\x18\x02 \x01(\x0e\x32\x1f.mobilegateway.protos.LockState\x12\x12\n\nvehicle_id\x18\x03 \x01(\t\"\x1a\n\x18\x44oorLocksControlResponse\"f\n\x18\x46rontCargoControlRequest\x12\x36\n\rclosure_state\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x1b\n\x19\x46rontCargoControlResponse\"(\n\x13\x44ocumentInfoUnknown\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\"\xa2\x01\n\x0c\x44ocumentInfo\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".mobilegateway.protos.DocumentType\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12:\n\x07unknown\x18\x05 \x01(\x0b\x32).mobilegateway.protos.DocumentInfoUnknown\"d\n\x16GetDocumentInfoRequest\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x39\n\rdocument_type\x18\x04 \x01(\x0e\x32\".mobilegateway.protos.DocumentType\"X\n\x17GetDocumentInfoResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x30\n\x04info\x18\x02 \x01(\x0b\x32\".mobilegateway.protos.DocumentInfo\",\n\x16GetVehicleStateRequest\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\"`\n\x17GetVehicleStateResponse\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x31\n\x05state\x18\x02 \x01(\x0b\x32\".mobilegateway.protos.VehicleState\"%\n\x0fHonkHornRequest\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\"\x12\n\x10HonkHornResponse\"i\n\x19HvacDefrostControlRequest\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x38\n\x0chvac_defrost\x18\x02 \x01(\x0e\x32\".mobilegateway.protos.DefrostState\"\x1c\n\x1aHvacDefrostControlResponse\"]\n\x14LightsControlRequest\x12\x31\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32!.mobilegateway.protos.LightAction\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x17\n\x15LightsControlResponse\"e\n\x17RearCargoControlRequest\x12\x36\n\rclosure_state\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.DoorState\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x1a\n\x18RearCargoControlResponse\"`\n\x1bSecurityAlarmControlRequest\x12-\n\x04mode\x18\x01 \x01(\x0e\x32\x1f.mobilegateway.protos.AlarmMode\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x1e\n\x1cSecurityAlarmControlResponse\"u\n\x1aSetCabinTemperatureRequest\x12\x13\n\x0btemperature\x18\x01 \x01(\x01\x12.\n\x05state\x18\x02 \x01(\x0e\x32\x1f.mobilegateway.protos.HvacPower\x12\x12\n\nvehicle_id\x18\x03 \x01(\t\"\x1d\n\x1bSetCabinTemperatureResponse\"B\n\x15SetChargeLimitRequest\x12\x15\n\rlimit_percent\x18\x01 \x01(\r\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\"\x18\n\x16SetChargeLimitResponse\"*\n\x14WakeupVehicleRequest\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\"\x17\n\x15WakeupVehicleResponse*k\n\x0b\x41\x63\x63\x65ssLevel\x12\x18\n\x14\x41\x43\x43\x45SS_LEVEL_UNKNOWN\x10\x00\x12\"\n\x1e\x41\x43\x43\x45SS_LEVEL_PREDELIVERY_OWNER\x10\x01\x12\x1e\n\x1a\x41\x43\x43\x45SS_LEVEL_PRIMARY_OWNER\x10\x02*<\n\x05Model\x12\x11\n\rMODEL_UNKNOWN\x10\x00\x12\r\n\tMODEL_AIR\x10\x01\x12\x11\n\rMODEL_GRAVITY\x10\x02*\x9e\x01\n\x0cModelVariant\x12\x19\n\x15MODEL_VARIANT_UNKNOWN\x10\x00\x12\x1f\n\x1bMODEL_VARIANT_DREAM_EDITION\x10\x01\x12\x1f\n\x1bMODEL_VARIANT_GRAND_TOURING\x10\x02\x12\x19\n\x15MODEL_VARIANT_TOURING\x10\x03\x12\x16\n\x12MODEL_VARIANT_PURE\x10\x04*\xf7\x01\n\nPaintColor\x12\x17\n\x13PAINT_COLOR_UNKNOWN\x10\x00\x12\x1b\n\x17PAINT_COLOR_EUREKA_GOLD\x10\x01\x12\x1d\n\x19PAINT_COLOR_STELLAR_WHITE\x10\x02\x12\x1e\n\x1aPAINT_COLOR_INFINITE_BLACK\x10\x03\x12\x1d\n\x19PAINT_COLOR_COSMOS_SILVER\x10\x04\x12\x1c\n\x18PAINT_COLOR_QUANTUM_GREY\x10\x05\x12\x1a\n\x16PAINT_COLOR_ZENITH_RED\x10\x06\x12\x1b\n\x17PAINT_COLOR_FATHOM_BLUE\x10\x07*=\n\x04Look\x12\x10\n\x0cLOOK_UNKNOWN\x10\x00\x12\x11\n\rLOOK_PLATINUM\x10\x01\x12\x10\n\x0cLOOK_STEALTH\x10\x02*|\n\x06Wheels\x12\x12\n\x0eWHEELS_UNKNOWN\x10\x00\x12\x10\n\x0cWHEELS_DREAM\x10\x01\x12\x10\n\x0cWHEELS_BLADE\x10\x02\x12\x0f\n\x0bWHEELS_LITE\x10\x03\x12\x10\n\x0cWHEELS_RANGE\x10\x04\x12\x17\n\x13WHEELS_LITE_STEALTH\x10\x08*V\n\x12SubscriptionStatus\x12\x1f\n\x1bSUBSCRIPTION_STATUS_UNKNOWN\x10\x00\x12\x1f\n\x1bSUBSCRIPTION_STATUS_CURRENT\x10\x01*b\n\x15\x43hargingAccountStatus\x12#\n\x1f\x43HARGING_ACCOUNT_STATUS_UNKNOWN\x10\x00\x12$\n CHARGING_ACCOUNT_STATUS_ENROLLED\x10\x02*o\n\x0e\x43hargingVendor\x12\x1b\n\x17\x43HARGING_VENDOR_UNKNOWN\x10\x00\x12%\n!CHARGING_VENDOR_ELECTRIFY_AMERICA\x10\x01\x12\x19\n\x15\x43HARGING_VENDOR_BOSCH\x10\x03*`\n\x07\x45\x64ition\x12\x13\n\x0f\x45\x44ITION_UNKNOWN\x10\x00\x12\x17\n\x13\x45\x44ITION_PERFORMANCE\x10\x01\x12\x11\n\rEDITION_RANGE\x10\x02\x12\x14\n\x10\x45\x44ITION_STANDARD\x10\x03*\xe4\x01\n\x0b\x42\x61tteryType\x12\x18\n\x14\x42\x41TTERY_TYPE_UNKNOWN\x10\x00\x12\x13\n\x0f\x42\x41TTERY_TYPE_01\x10\x01\x12\x13\n\x0f\x42\x41TTERY_TYPE_02\x10\x02\x12\x13\n\x0f\x42\x41TTERY_TYPE_03\x10\x03\x12\x13\n\x0f\x42\x41TTERY_TYPE_04\x10\x04\x12\x13\n\x0f\x42\x41TTERY_TYPE_05\x10\x05\x12\x13\n\x0f\x42\x41TTERY_TYPE_06\x10\x06\x12\x13\n\x0f\x42\x41TTERY_TYPE_07\x10\x07\x12\x13\n\x0f\x42\x41TTERY_TYPE_08\x10\x08\x12\x13\n\x0f\x42\x41TTERY_TYPE_09\x10\t*}\n\x08Interior\x12\x14\n\x10INTERIOR_UNKNOWN\x10\x00\x12\x17\n\x13INTERIOR_SANTA_CRUZ\x10\x01\x12\x12\n\x0eINTERIOR_TAHOE\x10\x02\x12\x13\n\x0fINTERIOR_MOJAVE\x10\x03\x12\x19\n\x15INTERIOR_SANTA_MONICA\x10\x05*M\n\tStrutType\x12\x16\n\x12STRUT_TYPE_UNKNOWN\x10\x00\x12\x12\n\x0eSTRUT_TYPE_GAS\x10\x01\x12\x14\n\x10STRUT_TYPE_POWER\x10\x02*R\n\x08RoofType\x12\x15\n\x11ROOF_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16ROOF_TYPE_GLASS_CANOPY\x10\x01\x12\x13\n\x0fROOF_TYPE_METAL\x10\x02*D\n\x0cWarningState\x12\x13\n\x0fWARNING_UNKNOWN\x10\x00\x12\x0f\n\x0bWARNING_OFF\x10\x01\x12\x0e\n\nWARNING_ON\x10\x02*\x80\x01\n\x13\x42\x61tteryPreconStatus\x12\x1a\n\x16\x42\x41TTERY_PRECON_UNKNOWN\x10\x00\x12\x16\n\x12\x42\x41TTERY_PRECON_OFF\x10\x01\x12\x15\n\x11\x42\x41TTERY_PRECON_ON\x10\x02\x12\x1e\n\x1a\x42\x41TTERY_PRECON_UNAVAILABLE\x10\x03*\x8e\x02\n\nPowerState\x12\x17\n\x13POWER_STATE_UNKNOWN\x10\x00\x12\x15\n\x11POWER_STATE_SLEEP\x10\x01\x12\x14\n\x10POWER_STATE_WINK\x10\x02\x12\x19\n\x15POWER_STATE_ACCESSORY\x10\x03\x12\x15\n\x11POWER_STATE_DRIVE\x10\x04\x12\x1b\n\x17POWER_STATE_LIVE_CHARGE\x10\x05\x12\x1c\n\x18POWER_STATE_SLEEP_CHARGE\x10\x06\x12\x1b\n\x17POWER_STATE_LIVE_UPDATE\x10\x07\x12\x17\n\x13POWER_STATE_CLOUD_2\x10\n\x12\x17\n\x13POWER_STATE_MONITOR\x10\x0b*S\n\tLockState\x12\x16\n\x12LOCK_STATE_UNKNOWN\x10\x00\x12\x17\n\x13LOCK_STATE_UNLOCKED\x10\x01\x12\x15\n\x11LOCK_STATE_LOCKED\x10\x02*d\n\tDoorState\x12\x16\n\x12\x44OOR_STATE_UNKNOWN\x10\x00\x12\x13\n\x0f\x44OOR_STATE_OPEN\x10\x01\x12\x15\n\x11\x44OOR_STATE_CLOSED\x10\x02\x12\x13\n\x0f\x44OOR_STATE_AJAR\x10\x03*P\n\rWalkawayState\x12\x14\n\x10WALKAWAY_UNKNOWN\x10\x00\x12\x13\n\x0fWALKAWAY_ACTIVE\x10\x02\x12\x14\n\x10WALKAWAY_DISABLE\x10\x03*b\n\rAccessRequest\x12\x1a\n\x16\x41\x43\x43\x45SS_REQUEST_UNKNOWN\x10\x00\x12\x19\n\x15\x41\x43\x43\x45SS_REQUEST_ACTIVE\x10\x01\x12\x1a\n\x16\x41\x43\x43\x45SS_REQUEST_PASSIVE\x10\x02*n\n\nLightState\x12\x1e\n\x1aLIGHT_STATE_REALLY_UNKNOWN\x10\x00\x12\x13\n\x0fLIGHT_STATE_OFF\x10\x01\x12\x12\n\x0eLIGHT_STATE_ON\x10\x02\x12\x17\n\x13LIGHT_STATE_UNKNOWN\x10\x03*j\n\x0bLightAction\x12\x18\n\x14LIGHT_ACTION_UNKNOWN\x10\x00\x12\x16\n\x12LIGHT_ACTION_FLASH\x10\x01\x12\x13\n\x0fLIGHT_ACTION_ON\x10\x02\x12\x14\n\x10LIGHT_ACTION_OFF\x10\x03*\xc4\x01\n\x0b\x43hargeState\x12\x18\n\x14\x43HARGE_STATE_UNKNOWN\x10\x00\x12\x1e\n\x1a\x43HARGE_STATE_NOT_CONNECTED\x10\x01\x12 \n\x1c\x43HARGE_STATE_CABLE_CONNECTED\x10\x02\x12\x19\n\x15\x43HARGE_STATE_CHARGING\x10\x08\x12 \n\x1c\x43HARGE_STATE_CHARGING_END_OK\x10\t\x12\x1c\n\x18\x43HARGE_STATE_DISCHARGING\x10\x13*\xb9\x01\n\x14ScheduledChargeState\x12\"\n\x1eSCHEDULED_CHARGE_STATE_UNKNOWN\x10\x00\x12\x1f\n\x1bSCHEDULED_CHARGE_STATE_IDLE\x10\x01\x12.\n*SCHEDULED_CHARGE_STATE_SCHEDULED_TO_CHARGE\x10\x02\x12,\n(SCHEDULED_CHARGE_STATE_REQUEST_TO_CHARGE\x10\x03*x\n\x1fScheduledChargeUnavailableState\x12(\n$SCHEDULED_CHARGE_UNAVAILABLE_UNKNOWN\x10\x00\x12+\n\'SCHEDULED_CHARGE_UNAVAILABLE_NO_REQUEST\x10\x01*b\n\nEnergyType\x12\x17\n\x13\x45NERGY_TYPE_UNKNOWN\x10\x00\x12\x12\n\x0e\x45NERGY_TYPE_AC\x10\x01\x12\x12\n\x0e\x45NERGY_TYPE_DC\x10\x02\x12\x13\n\x0f\x45NERGY_TYPE_V2V\x10\x04*\xbb\x01\n\x0bUpdateState\x12\x18\n\x14UPDATE_STATE_UNKNOWN\x10\x00\x12\x1c\n\x18UPDATE_STATE_IN_PROGRESS\x10\x01\x12\x18\n\x14UPDATE_STATE_SUCCESS\x10\x02\x12\x17\n\x13UPDATE_STATE_FAILED\x10\x03\x12\x1f\n\x1bUPDATE_FAILED_DRIVE_ALLOWED\x10\x05\x12 \n\x1cUPDATE_SUCCESS_WITH_WARNINGS\x10\x07*K\n\x12UpdateAvailability\x12\x1f\n\x1bUPDATE_AVAILABILITY_UNKNOWN\x10\x00\x12\x14\n\x10UPDATE_AVAILABLE\x10\x01*Z\n\x0b\x41larmStatus\x12\x18\n\x14\x41LARM_STATUS_UNKNOWN\x10\x00\x12\x19\n\x15\x41LARM_STATUS_DISARMED\x10\x01\x12\x16\n\x12\x41LARM_STATUS_ARMED\x10\x02*a\n\tAlarmMode\x12\x16\n\x12\x41LARM_MODE_UNKNOWN\x10\x00\x12\x12\n\x0e\x41LARM_MODE_OFF\x10\x01\x12\x11\n\rALARM_MODE_ON\x10\x02\x12\x15\n\x11\x41LARM_MODE_SILENT\x10\x03*w\n\x14\x43loudConnectionState\x12\x1c\n\x18\x43LOUD_CONNECTION_UNKNOWN\x10\x00\x12\x1e\n\x1a\x43LOUD_CONNECTION_CONNECTED\x10\x01\x12!\n\x1d\x43LOUD_CONNECTION_DISCONNECTED\x10\x02*c\n\x13KeylessDrivingState\x12\x1b\n\x17KEYLESS_DRIVING_UNKNOWN\x10\x00\x12\x16\n\x12KEYLESS_DRIVING_ON\x10\x01\x12\x17\n\x13KEYLESS_DRIVING_OFF\x10\x02*i\n\tHvacPower\x12\x16\n\x12HVAC_POWER_UNKNOWN\x10\x00\x12\x0b\n\x07HVAC_ON\x10\x01\x12\x0c\n\x08HVAC_OFF\x10\x02\x12\x15\n\x11HVAC_PRECONDITION\x10\x03\x12\x12\n\x0eHVAC_KEEP_TEMP\x10\x06*J\n\x0c\x44\x65\x66rostState\x12\x19\n\x15\x44\x45\x46ROST_STATE_UNKNOWN\x10\x00\x12\x0e\n\nDEFROST_ON\x10\x01\x12\x0f\n\x0b\x44\x45\x46ROST_OFF\x10\x02*\x92\x01\n\x16HvacPreconditionStatus\x12$\n HVAC_PRECONDITION_STATUS_UNKNOWN\x10\x00\x12)\n%HVAC_PRECONDITION_STATUS_STILL_ACTIVE\x10\x01\x12\'\n#HVAC_PRECONDITION_STATUS_USER_INPUT\x10\x04*\xbe\x01\n\x11KeepClimateStatus\x12\x1f\n\x1bKEEP_CLIMATE_STATUS_UNKNOWN\x10\x00\x12 \n\x1cKEEP_CLIMATE_STATUS_INACTIVE\x10\x01\x12\x1f\n\x1bKEEP_CLIMATE_STATUS_ENABLED\x10\x02\x12 \n\x1cKEEP_CLIMATE_STATUS_CANCELED\x10\x03\x12#\n\x1fKEEP_CLIMATE_STATUS_PET_MODE_ON\x10\x04*:\n\x14KeepClimateCondition\x12\"\n\x1eKEEP_CLIMATE_CONDITION_UNKNOWN\x10\x00*\x84\x01\n\tDriveMode\x12\x16\n\x12\x44RIVE_MODE_UNKNOWN\x10\x00\x12\x16\n\x12\x44RIVE_MODE_COMFORT\x10\x01\x12\x14\n\x10\x44RIVE_MODE_SWIFT\x10\x02\x12\x19\n\x15\x44RIVE_MODE_SPORT_PLUS\x10\x05\x12\x16\n\x12\x44RIVE_MODE_SERVICE\x10\x08*v\n\x0bPrivacyMode\x12\x18\n\x14PRIVACY_MODE_UNKNOWN\x10\x00\x12%\n!PRIVACY_MODE_CONNECTIVITY_ENABLED\x10\x01\x12&\n\"PRIVACY_MODE_CONNECTIVITY_DISABLED\x10\x02*c\n\x0cGearPosition\x12\x10\n\x0cGEAR_UNKNOWN\x10\x00\x12\r\n\tGEAR_PARK\x10\x01\x12\x10\n\x0cGEAR_REVERSE\x10\x02\x12\x10\n\x0cGEAR_NEUTRAL\x10\x03\x12\x0e\n\nGEAR_DRIVE\x10\x04*E\n\x0fSharedTripState\x12\x17\n\x13SHARED_TRIP_UNKNOWN\x10\x00\x12\x19\n\x15SHARED_TRIP_AVAILABLE\x10\x01*9\n\nPanicState\x12\x17\n\x13PANIC_ALARM_UNKNOWN\x10\x00\x12\x12\n\x0ePANIC_ALARM_ON\x10\x01*Y\n\x08TcuState\x12\x0f\n\x0bTCU_UNKNOWN\x10\x00\x12\r\n\tTCU_SLEEP\x10\x01\x12\x0e\n\nTCU_DROWSY\x10\x02\x12\x0c\n\x08TCU_FULL\x10\x04\x12\x0f\n\x0bTCU_FACTORY\x10\x05*A\n\x07LteType\x12\x14\n\x10LTE_TYPE_UNKNOWN\x10\x00\x12\x0f\n\x0bLTE_TYPE_3G\x10\x01\x12\x0f\n\x0bLTE_TYPE_4G\x10\x02*`\n\x0eInternetStatus\x12\x1b\n\x17INTERNET_STATUS_UNKNOWN\x10\x00\x12\x19\n\x15INTERNET_DISCONNECTED\x10\x01\x12\x16\n\x12INTERNET_CONNECTED\x10\x02*Z\n\x0c\x43hargeAction\x12\x19\n\x15\x43HARGE_ACTION_UNKNOWN\x10\x00\x12\x17\n\x13\x43HARGE_ACTION_START\x10\x01\x12\x16\n\x12\x43HARGE_ACTION_STOP\x10\x02*\x95\x01\n\x0c\x44ocumentType\x12\x19\n\x15\x44OCUMENT_TYPE_UNKNOWN\x10\x00\x12#\n\x1f\x44OCUMENT_TYPE_RELEASE_NOTES_PRE\x10\x01\x12$\n DOCUMENT_TYPE_RELEASE_NOTES_POST\x10\x02\x12\x1f\n\x1b\x44OCUMENT_TYPE_OWNERS_MANUAL\x10\x03\x32\xe0\x0e\n\x13VehicleStateService\x12|\n\x13\x41pplySoftwareUpdate\x12\x30.mobilegateway.protos.ApplySoftwareUpdateRequest\x1a\x31.mobilegateway.protos.ApplySoftwareUpdateResponse\"\x00\x12\x82\x01\n\x15\x43\x61ncelScheduledUpdate\x12\x32.mobilegateway.protos.CancelScheduledUpdateRequest\x1a\x33.mobilegateway.protos.CancelScheduledUpdateResponse\"\x00\x12j\n\rChargeControl\x12*.mobilegateway.protos.ChargeControlRequest\x1a+.mobilegateway.protos.ChargeControlResponse\"\x00\x12v\n\x11\x43ontrolChargePort\x12..mobilegateway.protos.ControlChargePortRequest\x1a/.mobilegateway.protos.ControlChargePortResponse\"\x00\x12s\n\x10\x44oorLocksControl\x12-.mobilegateway.protos.DoorLocksControlRequest\x1a..mobilegateway.protos.DoorLocksControlResponse\"\x00\x12v\n\x11\x46rontCargoControl\x12..mobilegateway.protos.FrontCargoControlRequest\x1a/.mobilegateway.protos.FrontCargoControlResponse\"\x00\x12p\n\x0fGetDocumentInfo\x12,.mobilegateway.protos.GetDocumentInfoRequest\x1a-.mobilegateway.protos.GetDocumentInfoResponse\"\x00\x12p\n\x0fGetVehicleState\x12,.mobilegateway.protos.GetVehicleStateRequest\x1a-.mobilegateway.protos.GetVehicleStateResponse\"\x00\x12[\n\x08HonkHorn\x12%.mobilegateway.protos.HonkHornRequest\x1a&.mobilegateway.protos.HonkHornResponse\"\x00\x12y\n\x12HvacDefrostControl\x12/.mobilegateway.protos.HvacDefrostControlRequest\x1a\x30.mobilegateway.protos.HvacDefrostControlResponse\"\x00\x12j\n\rLightsControl\x12*.mobilegateway.protos.LightsControlRequest\x1a+.mobilegateway.protos.LightsControlResponse\"\x00\x12s\n\x10RearCargoControl\x12-.mobilegateway.protos.RearCargoControlRequest\x1a..mobilegateway.protos.RearCargoControlResponse\"\x00\x12\x7f\n\x14SecurityAlarmControl\x12\x31.mobilegateway.protos.SecurityAlarmControlRequest\x1a\x32.mobilegateway.protos.SecurityAlarmControlResponse\"\x00\x12|\n\x13SetCabinTemperature\x12\x30.mobilegateway.protos.SetCabinTemperatureRequest\x1a\x31.mobilegateway.protos.SetCabinTemperatureResponse\"\x00\x12m\n\x0eSetChargeLimit\x12+.mobilegateway.protos.SetChargeLimitRequest\x1a,.mobilegateway.protos.SetChargeLimitResponse\"\x00\x12j\n\rWakeupVehicle\x12*.mobilegateway.protos.WakeupVehicleRequest\x1a+.mobilegateway.protos.WakeupVehicleResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle_state_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ACCESSLEVEL']._serialized_start=9009
  _globals['_ACCESSLEVEL']._serialized_end=9116
  _globals['_MODEL']._serialized_start=9118
  _globals['_MODEL']._serialized_end=9178
  _globals['_MODELVARIANT']._serialized_start=9181
  _globals['_MODELVARIANT']._serialized_end=9339
  _globals['_PAINTCOLOR']._serialized_start=9342
  _globals['_PAINTCOLOR']._serialized_end=9589
  _globals['_LOOK']._serialized_start=9591
  _globals['_LOOK']._serialized_end=9652
  _globals['_WHEELS']._serialized_start=9654
  _globals['_WHEELS']._serialized_end=9778
  _globals['_SUBSCRIPTIONSTATUS']._serialized_start=9780
  _globals['_SUBSCRIPTIONSTATUS']._serialized_end=9866
  _globals['_CHARGINGACCOUNTSTATUS']._serialized_start=9868
  _globals['_CHARGINGACCOUNTSTATUS']._serialized_end=9966
  _globals['_CHARGINGVENDOR']._serialized_start=9968
  _globals['_CHARGINGVENDOR']._serialized_end=10079
  _globals['_EDITION']._serialized_start=10081
  _globals['_EDITION']._serialized_end=10177
  _globals['_BATTERYTYPE']._serialized_start=10180
  _globals['_BATTERYTYPE']._serialized_end=10408
  _globals['_INTERIOR']._serialized_start=10410
  _globals['_INTERIOR']._serialized_end=10535
  _globals['_STRUTTYPE']._serialized_start=10537
  _globals['_STRUTTYPE']._serialized_end=10614
  _globals['_ROOFTYPE']._serialized_start=10616
  _globals['_ROOFTYPE']._serialized_end=10698
  _globals['_WARNINGSTATE']._serialized_start=10700
  _globals['_WARNINGSTATE']._serialized_end=10768
  _globals['_BATTERYPRECONSTATUS']._serialized_start=10771
  _globals['_BATTERYPRECONSTATUS']._serialized_end=10899
  _globals['_POWERSTATE']._serialized_start=10902
  _globals['_POWERSTATE']._serialized_end=11172
  _globals['_LOCKSTATE']._serialized_start=11174
  _globals['_LOCKSTATE']._serialized_end=11257
  _globals['_DOORSTATE']._serialized_start=11259
  _globals['_DOORSTATE']._serialized_end=11359
  _globals['_WALKAWAYSTATE']._serialized_start=11361
  _globals['_WALKAWAYSTATE']._serialized_end=11441
  _globals['_ACCESSREQUEST']._serialized_start=11443
  _globals['_ACCESSREQUEST']._serialized_end=11541
  _globals['_LIGHTSTATE']._serialized_start=11543
  _globals['_LIGHTSTATE']._serialized_end=11653
  _globals['_LIGHTACTION']._serialized_start=11655
  _globals['_LIGHTACTION']._serialized_end=11761
  _globals['_CHARGESTATE']._serialized_start=11764
  _globals['_CHARGESTATE']._serialized_end=11960
  _globals['_SCHEDULEDCHARGESTATE']._serialized_start=11963
  _globals['_SCHEDULEDCHARGESTATE']._serialized_end=12148
  _globals['_SCHEDULEDCHARGEUNAVAILABLESTATE']._serialized_start=12150
  _globals['_SCHEDULEDCHARGEUNAVAILABLESTATE']._serialized_end=12270
  _globals['_ENERGYTYPE']._serialized_start=12272
  _globals['_ENERGYTYPE']._serialized_end=12370
  _globals['_UPDATESTATE']._serialized_start=12373
  _globals['_UPDATESTATE']._serialized_end=12560
  _globals['_UPDATEAVAILABILITY']._serialized_start=12562
  _globals['_UPDATEAVAILABILITY']._serialized_end=12637
  _globals['_ALARMSTATUS']._serialized_start=12639
  _globals['_ALARMSTATUS']._serialized_end=12729
  _globals['_ALARMMODE']._serialized_start=12731
  _globals['_ALARMMODE']._serialized_end=12828
  _globals['_CLOUDCONNECTIONSTATE']._serialized_start=12830
  _globals['_CLOUDCONNECTIONSTATE']._serialized_end=12949
  _globals['_KEYLESSDRIVINGSTATE']._serialized_start=12951
  _globals['_KEYLESSDRIVINGSTATE']._serialized_end=13050
  _globals['_HVACPOWER']._serialized_start=13052
  _globals['_HVACPOWER']._serialized_end=13157
  _globals['_DEFROSTSTATE']._serialized_start=13159
  _globals['_DEFROSTSTATE']._serialized_end=13233
  _globals['_HVACPRECONDITIONSTATUS']._serialized_start=13236
  _globals['_HVACPRECONDITIONSTATUS']._serialized_end=13382
  _globals['_KEEPCLIMATESTATUS']._serialized_start=13385
  _globals['_KEEPCLIMATESTATUS']._serialized_end=13575
  _globals['_KEEPCLIMATECONDITION']._serialized_start=13577
  _globals['_KEEPCLIMATECONDITION']._serialized_end=13635
  _globals['_DRIVEMODE']._serialized_start=13638
  _globals['_DRIVEMODE']._serialized_end=13770
  _globals['_PRIVACYMODE']._serialized_start=13772
  _globals['_PRIVACYMODE']._serialized_end=13890
  _globals['_GEARPOSITION']._serialized_start=13892
  _globals['_GEARPOSITION']._serialized_end=13991
  _globals['_SHAREDTRIPSTATE']._serialized_start=13993
  _globals['_SHAREDTRIPSTATE']._serialized_end=14062
  _globals['_PANICSTATE']._serialized_start=14064
  _globals['_PANICSTATE']._serialized_end=14121
  _globals['_TCUSTATE']._serialized_start=14123
  _globals['_TCUSTATE']._serialized_end=14212
  _globals['_LTETYPE']._serialized_start=14214
  _globals['_LTETYPE']._serialized_end=14279
  _globals['_INTERNETSTATUS']._serialized_start=14281
  _globals['_INTERNETSTATUS']._serialized_end=14377
  _globals['_CHARGEACTION']._serialized_start=14379
  _globals['_CHARGEACTION']._serialized_end=14469
  _globals['_DOCUMENTTYPE']._serialized_start=14472
  _globals['_DOCUMENTTYPE']._serialized_end=14621
  _globals['_CHARGINGSUBSCRIPTION']._serialized_start=54
  _globals['_CHARGINGSUBSCRIPTION']._serialized_end=193
  _globals['_CHARGINGACCOUNT']._serialized_start=196
  _globals['_CHARGINGACCOUNT']._serialized_end=428
  _globals['_SPECIALIDENTIFIERS']._serialized_start=430
  _globals['_SPECIALIDENTIFIERS']._serialized_end=470
  _globals['_RESERVATION']._serialized_start=472
  _globals['_RESERVATION']._serialized_end=499
  _globals['_VEHICLECONFIG']._serialized_start=502
  _globals['_VEHICLECONFIG']._serialized_end=1417
  _globals['_BATTERYSTATE']._serialized_start=1420
  _globals['_BATTERYSTATE']._serialized_end=1851
  _globals['_CABINSTATE']._serialized_start=1853
  _globals['_CABINSTATE']._serialized_end=1911
  _globals['_BODYSTATE']._serialized_start=1914
  _globals['_BODYSTATE']._serialized_end=2496
  _globals['_CHASSISSTATE']._serialized_start=2499
  _globals['_CHASSISSTATE']._serialized_end=3294
  _globals['_CHARGINGSTATE']._serialized_start=3297
  _globals['_CHARGINGSTATE']._serialized_end=3918
  _globals['_LOCATION']._serialized_start=3920
  _globals['_LOCATION']._serialized_end=3967
  _globals['_GPS']._serialized_start=3969
  _globals['_GPS']._serialized_end=4091
  _globals['_SOFTWAREUPDATE']._serialized_start=4094
  _globals['_SOFTWAREUPDATE']._serialized_end=4380
  _globals['_ALARMSTATE']._serialized_start=4382
  _globals['_ALARMSTATE']._serialized_end=4492
  _globals['_HVACSTATE']._serialized_start=4495
  _globals['_HVACSTATE']._serialized_end=4752
  _globals['_MOBILEAPPREQSTATE']._serialized_start=4755
  _globals['_MOBILEAPPREQSTATE']._serialized_end=5386
  _globals['_TCUINTERNETSTATE']._serialized_start=5389
  _globals['_TCUINTERNETSTATE']._serialized_end=5647
  _globals['_VEHICLESTATE']._serialized_start=5650
  _globals['_VEHICLESTATE']._serialized_end=6677
  _globals['_VEHICLE']._serialized_start=6680
  _globals['_VEHICLE']._serialized_end=6870
  _globals['_APPLYSOFTWAREUPDATEREQUEST']._serialized_start=6872
  _globals['_APPLYSOFTWAREUPDATEREQUEST']._serialized_end=6920
  _globals['_APPLYSOFTWAREUPDATERESPONSE']._serialized_start=6922
  _globals['_APPLYSOFTWAREUPDATERESPONSE']._serialized_end=6951
  _globals['_CANCELSCHEDULEDUPDATEREQUEST']._serialized_start=6953
  _globals['_CANCELSCHEDULEDUPDATEREQUEST']._serialized_end=7003
  _globals['_CANCELSCHEDULEDUPDATERESPONSE']._serialized_start=7005
  _globals['_CANCELSCHEDULEDUPDATERESPONSE']._serialized_end=7036
  _globals['_CHARGECONTROLREQUEST']._serialized_start=7038
  _globals['_CHARGECONTROLREQUEST']._serialized_end=7132
  _globals['_CHARGECONTROLRESPONSE']._serialized_start=7134
  _globals['_CHARGECONTROLRESPONSE']._serialized_end=7157
  _globals['_CONTROLCHARGEPORTREQUEST']._serialized_start=7159
  _globals['_CONTROLCHARGEPORTREQUEST']._serialized_end=7261
  _globals['_CONTROLCHARGEPORTRESPONSE']._serialized_start=7263
  _globals['_CONTROLCHARGEPORTRESPONSE']._serialized_end=7290
  _globals['_DOORLOCKSCONTROLREQUEST']._serialized_start=7292
  _globals['_DOORLOCKSCONTROLREQUEST']._serialized_end=7413
  _globals['_DOORLOCKSCONTROLRESPONSE']._serialized_start=7415
  _globals['_DOORLOCKSCONTROLRESPONSE']._serialized_end=7441
  _globals['_FRONTCARGOCONTROLREQUEST']._serialized_start=7443
  _globals['_FRONTCARGOCONTROLREQUEST']._serialized_end=7545
  _globals['_FRONTCARGOCONTROLRESPONSE']._serialized_start=7547
  _globals['_FRONTCARGOCONTROLRESPONSE']._serialized_end=7574
  _globals['_DOCUMENTINFOUNKNOWN']._serialized_start=7576
  _globals['_DOCUMENTINFOUNKNOWN']._serialized_end=7616
  _globals['_DOCUMENTINFO']._serialized_start=7619
  _globals['_DOCUMENTINFO']._serialized_end=7781
  _globals['_GETDOCUMENTINFOREQUEST']._serialized_start=7783
  _globals['_GETDOCUMENTINFOREQUEST']._serialized_end=7883
  _globals['_GETDOCUMENTINFORESPONSE']._serialized_start=7885
  _globals['_GETDOCUMENTINFORESPONSE']._serialized_end=7973
  _globals['_GETVEHICLESTATEREQUEST']._serialized_start=7975
  _globals['_GETVEHICLESTATEREQUEST']._serialized_end=8019
  _globals['_GETVEHICLESTATERESPONSE']._serialized_start=8021
  _globals['_GETVEHICLESTATERESPONSE']._serialized_end=8117
  _globals['_HONKHORNREQUEST']._serialized_start=8119
  _globals['_HONKHORNREQUEST']._serialized_end=8156
  _globals['_HONKHORNRESPONSE']._serialized_start=8158
  _globals['_HONKHORNRESPONSE']._serialized_end=8176
  _globals['_HVACDEFROSTCONTROLREQUEST']._serialized_start=8178
  _globals['_HVACDEFROSTCONTROLREQUEST']._serialized_end=8283
  _globals['_HVACDEFROSTCONTROLRESPONSE']._serialized_start=8285
  _globals['_HVACDEFROSTCONTROLRESPONSE']._serialized_end=8313
  _globals['_LIGHTSCONTROLREQUEST']._serialized_start=8315
  _globals['_LIGHTSCONTROLREQUEST']._serialized_end=8408
  _globals['_LIGHTSCONTROLRESPONSE']._serialized_start=8410
  _globals['_LIGHTSCONTROLRESPONSE']._serialized_end=8433
  _globals['_REARCARGOCONTROLREQUEST']._serialized_start=8435
  _globals['_REARCARGOCONTROLREQUEST']._serialized_end=8536
  _globals['_REARCARGOCONTROLRESPONSE']._serialized_start=8538
  _globals['_REARCARGOCONTROLRESPONSE']._serialized_end=8564
  _globals['_SECURITYALARMCONTROLREQUEST']._serialized_start=8566
  _globals['_SECURITYALARMCONTROLREQUEST']._serialized_end=8662
  _globals['_SECURITYALARMCONTROLRESPONSE']._serialized_start=8664
  _globals['_SECURITYALARMCONTROLRESPONSE']._serialized_end=8694
  _globals['_SETCABINTEMPERATUREREQUEST']._serialized_start=8696
  _globals['_SETCABINTEMPERATUREREQUEST']._serialized_end=8813
  _globals['_SETCABINTEMPERATURERESPONSE']._serialized_start=8815
  _globals['_SETCABINTEMPERATURERESPONSE']._serialized_end=8844
  _globals['_SETCHARGELIMITREQUEST']._serialized_start=8846
  _globals['_SETCHARGELIMITREQUEST']._serialized_end=8912
  _globals['_SETCHARGELIMITRESPONSE']._serialized_start=8914
  _globals['_SETCHARGELIMITRESPONSE']._serialized_end=8938
  _globals['_WAKEUPVEHICLEREQUEST']._serialized_start=8940
  _globals['_WAKEUPVEHICLEREQUEST']._serialized_end=8982
  _globals['_WAKEUPVEHICLERESPONSE']._serialized_start=8984
  _globals['_WAKEUPVEHICLERESPONSE']._serialized_end=9007
  _globals['_VEHICLESTATESERVICE']._serialized_start=14624
  _globals['_VEHICLESTATESERVICE']._serialized_end=16512
# @@protoc_insertion_point(module_scope)
