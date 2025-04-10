# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user_profile_service.proto
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
    'user_profile_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1auser_profile_service.proto\x12\x14mobilegateway.protos\"+\n\x0bPhoneNumber\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\t\"\x89\x02\n\x0fUserProfileData\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06locale\x18\x04 \x01(\t\x12\x11\n\tphoto_url\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12\x0c\n\x04\x63ity\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\x13\n\x0bpostal_code\x18\t \x01(\t\x12\x0f\n\x07\x63ountry\x18\n \x01(\t\x12\x31\n\x06phones\x18\x0b \x03(\x0b\x32!.mobilegateway.protos.PhoneNumber\x12\x16\n\x0epreferred_name\x18\x0c \x01(\t\"\x17\n\x15GetUserProfileRequest\"P\n\x16GetUserProfileResponse\x12\x36\n\x07profile\x18\x01 \x01(\x0b\x32%.mobilegateway.protos.UserProfileData\">\n\x15SetUserProfileRequest\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\"P\n\x16SetUserProfileResponse\x12\x36\n\x07profile\x18\x01 \x01(\x0b\x32%.mobilegateway.protos.UserProfileData\"4\n\x1dUploadUserProfilePhotoRequest\x12\x13\n\x0bphoto_bytes\x18\x01 \x01(\t\"3\n\x1eUploadUserProfilePhotoResponse\x12\x11\n\tphoto_url\x18\x01 \x01(\t\"\x1b\n\x19ReferralHistoryApiRequest\"\x1c\n\x1aReferralHistoryApiResponse2\xf5\x03\n\x12UserProfileService\x12m\n\x0eGetUserProfile\x12+.mobilegateway.protos.GetUserProfileRequest\x1a,.mobilegateway.protos.GetUserProfileResponse\"\x00\x12m\n\x0eSetUserProfile\x12+.mobilegateway.protos.SetUserProfileRequest\x1a,.mobilegateway.protos.SetUserProfileResponse\"\x00\x12\x85\x01\n\x16UploadUserProfilePhoto\x12\x33.mobilegateway.protos.UploadUserProfilePhotoRequest\x1a\x34.mobilegateway.protos.UploadUserProfilePhotoResponse\"\x00\x12y\n\x12ReferralHistoryApi\x12/.mobilegateway.protos.ReferralHistoryApiRequest\x1a\x30.mobilegateway.protos.ReferralHistoryApiResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_profile_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PHONENUMBER']._serialized_start=52
  _globals['_PHONENUMBER']._serialized_end=95
  _globals['_USERPROFILEDATA']._serialized_start=98
  _globals['_USERPROFILEDATA']._serialized_end=363
  _globals['_GETUSERPROFILEREQUEST']._serialized_start=365
  _globals['_GETUSERPROFILEREQUEST']._serialized_end=388
  _globals['_GETUSERPROFILERESPONSE']._serialized_start=390
  _globals['_GETUSERPROFILERESPONSE']._serialized_end=470
  _globals['_SETUSERPROFILEREQUEST']._serialized_start=472
  _globals['_SETUSERPROFILEREQUEST']._serialized_end=534
  _globals['_SETUSERPROFILERESPONSE']._serialized_start=536
  _globals['_SETUSERPROFILERESPONSE']._serialized_end=616
  _globals['_UPLOADUSERPROFILEPHOTOREQUEST']._serialized_start=618
  _globals['_UPLOADUSERPROFILEPHOTOREQUEST']._serialized_end=670
  _globals['_UPLOADUSERPROFILEPHOTORESPONSE']._serialized_start=672
  _globals['_UPLOADUSERPROFILEPHOTORESPONSE']._serialized_end=723
  _globals['_REFERRALHISTORYAPIREQUEST']._serialized_start=725
  _globals['_REFERRALHISTORYAPIREQUEST']._serialized_end=752
  _globals['_REFERRALHISTORYAPIRESPONSE']._serialized_start=754
  _globals['_REFERRALHISTORYAPIRESPONSE']._serialized_end=782
  _globals['_USERPROFILESERVICE']._serialized_start=785
  _globals['_USERPROFILESERVICE']._serialized_end=1286
# @@protoc_insertion_point(module_scope)
