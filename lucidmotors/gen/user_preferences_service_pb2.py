# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user_preferences_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'user_preferences_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1euser_preferences_service.proto\x12\x14mobilegateway.protos\"\x07\n\x05\x45mpty\"n\n\x0fUserPreferences\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x11\n\tphoto_url\x18\x04 \x01(\t\x12\x12\n\nupdated_ns\x18\x12 \x01(\x04\x12\r\n\x05\x65mail\x18\x13 \x01(\t\"k\n\x1aGetUserPreferencesResponse\x12:\n\x0bpreferences\x18\x01 \x01(\x0b\x32%.mobilegateway.protos.UserPreferences\x12\x11\n\tcommit_ns\x18\x02 \x01(\x04\"Z\n\x1c\x43reateUserPreferencesRequest\x12:\n\x0bpreferences\x18\x01 \x01(\x0b\x32%.mobilegateway.protos.UserPreferences\"7\n\"GetUserPreferencesCommitIDResponse\x12\x11\n\tcommit_ns\x18\x01 \x01(\x04\x32\x97\x03\n\x16UserPreferencesService\x12j\n\x15\x43reateUserPreferences\x12\x32.mobilegateway.protos.CreateUserPreferencesRequest\x1a\x1b.mobilegateway.protos.Empty\"\x00\x12\x65\n\x12GetUserPreferences\x12\x1b.mobilegateway.protos.Empty\x1a\x30.mobilegateway.protos.GetUserPreferencesResponse\"\x00\x12X\n\x1aGetUserPreferencesCommitID\x12\x1b.mobilegateway.protos.Empty\x1a\x1b.mobilegateway.protos.Empty\"\x00\x12P\n\x12SetUserPreferences\x12\x1b.mobilegateway.protos.Empty\x1a\x1b.mobilegateway.protos.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_preferences_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=56
  _globals['_EMPTY']._serialized_end=63
  _globals['_USERPREFERENCES']._serialized_start=65
  _globals['_USERPREFERENCES']._serialized_end=175
  _globals['_GETUSERPREFERENCESRESPONSE']._serialized_start=177
  _globals['_GETUSERPREFERENCESRESPONSE']._serialized_end=284
  _globals['_CREATEUSERPREFERENCESREQUEST']._serialized_start=286
  _globals['_CREATEUSERPREFERENCESREQUEST']._serialized_end=376
  _globals['_GETUSERPREFERENCESCOMMITIDRESPONSE']._serialized_start=378
  _globals['_GETUSERPREFERENCESCOMMITIDRESPONSE']._serialized_end=433
  _globals['_USERPREFERENCESSERVICE']._serialized_start=436
  _globals['_USERPREFERENCESSERVICE']._serialized_end=843
# @@protoc_insertion_point(module_scope)
