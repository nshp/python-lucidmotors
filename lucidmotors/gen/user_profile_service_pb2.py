# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_profile_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1auser_profile_service.proto\x12\x14mobilegateway.protos\"\x9b\x01\n\x0bUserProfile\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x13\n\x06locale\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x16\n\tphoto_url\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nfirst_name\x18\x05 \x01(\t\x12\x11\n\tlast_name\x18\x06 \x01(\tB\t\n\x07_localeB\x0c\n\n_photo_url\"\x1d\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x02 \x01(\t\"\xdd\x01\n\x0fUserProfileData\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06locale\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12\x0c\n\x04\x63ity\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\x13\n\x0bpostal_code\x18\t \x01(\t\x12\x0f\n\x07\x63ountry\x18\n \x01(\t\x12\x30\n\x05phone\x18\x0b \x01(\x0b\x32!.mobilegateway.protos.PhoneNumber\"\x17\n\x15SetUserProfileRequest\"\x18\n\x16SetUserProfileResponse\"\x17\n\x15GetUserProfileRequest\"P\n\x16GetUserProfileResponse\x12\x36\n\x07profile\x18\x01 \x01(\x0b\x32%.mobilegateway.protos.UserProfileData\"4\n\x1dUploadUserProfilePhotoRequest\x12\x13\n\x0bphoto_bytes\x18\x01 \x01(\t\"3\n\x1eUploadUserProfilePhotoResponse\x12\x11\n\tphoto_url\x18\x01 \x01(\t\"\x1b\n\x19ReferralHistoryApiRequest\"\x1c\n\x1aReferralHistoryApiResponse2\xf5\x03\n\x12UserProfileService\x12m\n\x0eGetUserProfile\x12+.mobilegateway.protos.GetUserProfileRequest\x1a,.mobilegateway.protos.GetUserProfileResponse\"\x00\x12m\n\x0eSetUserProfile\x12+.mobilegateway.protos.SetUserProfileRequest\x1a,.mobilegateway.protos.SetUserProfileResponse\"\x00\x12\x85\x01\n\x16UploadUserProfilePhoto\x12\x33.mobilegateway.protos.UploadUserProfilePhotoRequest\x1a\x34.mobilegateway.protos.UploadUserProfilePhotoResponse\"\x00\x12y\n\x12ReferralHistoryApi\x12/.mobilegateway.protos.ReferralHistoryApiRequest\x1a\x30.mobilegateway.protos.ReferralHistoryApiResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_profile_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERPROFILE']._serialized_start=53
  _globals['_USERPROFILE']._serialized_end=208
  _globals['_PHONENUMBER']._serialized_start=210
  _globals['_PHONENUMBER']._serialized_end=239
  _globals['_USERPROFILEDATA']._serialized_start=242
  _globals['_USERPROFILEDATA']._serialized_end=463
  _globals['_SETUSERPROFILEREQUEST']._serialized_start=465
  _globals['_SETUSERPROFILEREQUEST']._serialized_end=488
  _globals['_SETUSERPROFILERESPONSE']._serialized_start=490
  _globals['_SETUSERPROFILERESPONSE']._serialized_end=514
  _globals['_GETUSERPROFILEREQUEST']._serialized_start=516
  _globals['_GETUSERPROFILEREQUEST']._serialized_end=539
  _globals['_GETUSERPROFILERESPONSE']._serialized_start=541
  _globals['_GETUSERPROFILERESPONSE']._serialized_end=621
  _globals['_UPLOADUSERPROFILEPHOTOREQUEST']._serialized_start=623
  _globals['_UPLOADUSERPROFILEPHOTOREQUEST']._serialized_end=675
  _globals['_UPLOADUSERPROFILEPHOTORESPONSE']._serialized_start=677
  _globals['_UPLOADUSERPROFILEPHOTORESPONSE']._serialized_end=728
  _globals['_REFERRALHISTORYAPIREQUEST']._serialized_start=730
  _globals['_REFERRALHISTORYAPIREQUEST']._serialized_end=757
  _globals['_REFERRALHISTORYAPIRESPONSE']._serialized_start=759
  _globals['_REFERRALHISTORYAPIRESPONSE']._serialized_end=787
  _globals['_USERPROFILESERVICE']._serialized_start=790
  _globals['_USERPROFILESERVICE']._serialized_end=1291
# @@protoc_insertion_point(module_scope)
