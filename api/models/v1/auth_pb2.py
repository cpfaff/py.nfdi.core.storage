# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/models/v1/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.models.v1 import common_models_pb2 as api_dot_models_dot_v1_dot_common__models__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/models/v1/auth.proto',
  package='api.models.v1',
  syntax='proto3',
  serialized_options=b'\n2com.github.ScienceObjectsDB.java_api.api.models.v1B\nAuthModelsP\001Z0github.com/ScienceObjectsDB/go-api/api/models/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x61pi/models/v1/auth.proto\x12\rapi.models.v1\x1a!api/models/v1/common_models.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"[\n\tTokenList\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12/\n\x05token\x18\x02 \x03(\x0b\x32\x19.api.models.v1.TokenEntryR\x05token\"\x81\x02\n\nTokenEntry\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12,\n\x07user_id\x18\x02 \x01(\x0b\x32\x13.api.models.v1.UserR\x06userId\x12\x14\n\x05token\x18\x03 \x01(\tR\x05token\x12\x33\n\x08resource\x18\x04 \x01(\x0e\x32\x17.api.models.v1.ResourceR\x08resource\x12\x34\n\x07\x63reated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x34\n\x07\x65xpires\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65xpires\"\xce\x01\n\x12\x43reateTokenRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12,\n\x06rights\x18\x02 \x03(\x0e\x32\x14.api.models.v1.RightR\x06rights\x12\x33\n\x08resource\x18\x03 \x01(\x0e\x32\x17.api.models.v1.ResourceR\x08resource\x12\x34\n\x07\x65xpires\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65xpiresBt\n2com.github.ScienceObjectsDB.java_api.api.models.v1B\nAuthModelsP\x01Z0github.com/ScienceObjectsDB/go-api/api/models/v1b\x06proto3'
  ,
  dependencies=[api_dot_models_dot_v1_dot_common__models__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TOKENLIST = _descriptor.Descriptor(
  name='TokenList',
  full_name='api.models.v1.TokenList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='api.models.v1.TokenList.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='projectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='api.models.v1.TokenList.token', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='token', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=202,
)


_TOKENENTRY = _descriptor.Descriptor(
  name='TokenEntry',
  full_name='api.models.v1.TokenEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.models.v1.TokenEntry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='api.models.v1.TokenEntry.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='api.models.v1.TokenEntry.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='token', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='api.models.v1.TokenEntry.resource', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='api.models.v1.TokenEntry.created', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='created', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expires', full_name='api.models.v1.TokenEntry.expires', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expires', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=462,
)


_CREATETOKENREQUEST = _descriptor.Descriptor(
  name='CreateTokenRequest',
  full_name='api.models.v1.CreateTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='api.models.v1.CreateTokenRequest.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rights', full_name='api.models.v1.CreateTokenRequest.rights', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='api.models.v1.CreateTokenRequest.resource', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expires', full_name='api.models.v1.CreateTokenRequest.expires', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expires', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=671,
)

_TOKENLIST.fields_by_name['token'].message_type = _TOKENENTRY
_TOKENENTRY.fields_by_name['user_id'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._USER
_TOKENENTRY.fields_by_name['resource'].enum_type = api_dot_models_dot_v1_dot_common__models__pb2._RESOURCE
_TOKENENTRY.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TOKENENTRY.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATETOKENREQUEST.fields_by_name['rights'].enum_type = api_dot_models_dot_v1_dot_common__models__pb2._RIGHT
_CREATETOKENREQUEST.fields_by_name['resource'].enum_type = api_dot_models_dot_v1_dot_common__models__pb2._RESOURCE
_CREATETOKENREQUEST.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['TokenList'] = _TOKENLIST
DESCRIPTOR.message_types_by_name['TokenEntry'] = _TOKENENTRY
DESCRIPTOR.message_types_by_name['CreateTokenRequest'] = _CREATETOKENREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenList = _reflection.GeneratedProtocolMessageType('TokenList', (_message.Message,), {
  'DESCRIPTOR' : _TOKENLIST,
  '__module__' : 'api.models.v1.auth_pb2'
  # @@protoc_insertion_point(class_scope:api.models.v1.TokenList)
  })
_sym_db.RegisterMessage(TokenList)

TokenEntry = _reflection.GeneratedProtocolMessageType('TokenEntry', (_message.Message,), {
  'DESCRIPTOR' : _TOKENENTRY,
  '__module__' : 'api.models.v1.auth_pb2'
  # @@protoc_insertion_point(class_scope:api.models.v1.TokenEntry)
  })
_sym_db.RegisterMessage(TokenEntry)

CreateTokenRequest = _reflection.GeneratedProtocolMessageType('CreateTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOKENREQUEST,
  '__module__' : 'api.models.v1.auth_pb2'
  # @@protoc_insertion_point(class_scope:api.models.v1.CreateTokenRequest)
  })
_sym_db.RegisterMessage(CreateTokenRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
