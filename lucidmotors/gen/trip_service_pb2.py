# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trip_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12trip_service.proto\x12\x14mobilegateway.protos\"{\n\x08Waypoint\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x39\n\rwaypoint_type\x18\x05 \x01(\x0e\x32\".mobilegateway.protos.WaypointType\"\x89\x02\n\x04Trip\x12\x18\n\x10\x64\x65stination_name\x18\x02 \x01(\t\x12\x1c\n\x0f\x64istance_meters\x18\x03 \x01(\x04H\x00\x88\x01\x01\x12\x1d\n\x10\x65lapsed_time_sec\x18\x04 \x01(\x04H\x01\x88\x01\x01\x12\x1b\n\x0e\x63harging_stops\x18\x05 \x01(\rH\x02\x88\x01\x01\x12\x31\n\twaypoints\x18\x07 \x03(\x0b\x32\x1e.mobilegateway.protos.Waypoint\x12\x13\n\x06sender\x18\x08 \x01(\tH\x03\x88\x01\x01\x42\x12\n\x10_distance_metersB\x13\n\x11_elapsed_time_secB\x11\n\x0f_charging_stopsB\t\n\x07_sender\"P\n\x10ShareTripRequest\x12(\n\x04trip\x18\x02 \x01(\x0b\x32\x1a.mobilegateway.protos.Trip\x12\x12\n\nvehicle_id\x18\x03 \x01(\t\"\x13\n\x11ShareTripResponse*a\n\x0cWaypointType\x12\x19\n\x15WAYPOINT_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16WAYPOINT_TYPE_CHARGING\x10\x01\x12\x1a\n\x16WAYPOINT_TYPE_WAYPOINT\x10\x02\x32m\n\x0bTripService\x12^\n\tShareTrip\x12&.mobilegateway.protos.ShareTripRequest\x1a\'.mobilegateway.protos.ShareTripResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trip_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_WAYPOINTTYPE']._serialized_start=540
  _globals['_WAYPOINTTYPE']._serialized_end=637
  _globals['_WAYPOINT']._serialized_start=44
  _globals['_WAYPOINT']._serialized_end=167
  _globals['_TRIP']._serialized_start=170
  _globals['_TRIP']._serialized_end=435
  _globals['_SHARETRIPREQUEST']._serialized_start=437
  _globals['_SHARETRIPREQUEST']._serialized_end=517
  _globals['_SHARETRIPRESPONSE']._serialized_start=519
  _globals['_SHARETRIPRESPONSE']._serialized_end=538
  _globals['_TRIPSERVICE']._serialized_start=639
  _globals['_TRIPSERVICE']._serialized_end=748
# @@protoc_insertion_point(module_scope)
