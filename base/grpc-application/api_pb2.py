# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='endpoints',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tapi.proto\x12\tendpoints\x1a\x1bgoogle/protobuf/empty.proto\"\x1b\n\nStackUsers\x12\r\n\x05users\x18\x01 \x01(\t\"\x1d\n\tStackUser\x12\x10\n\x08username\x18\x01 \x01(\t2D\n\x05Users\x12;\n\x08GetUsers\x12\x16.google.protobuf.Empty\x1a\x15.endpoints.StackUsers\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_STACKUSERS = _descriptor.Descriptor(
  name='StackUsers',
  full_name='endpoints.StackUsers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='endpoints.StackUsers.users', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=53,
  serialized_end=80,
)


_STACKUSER = _descriptor.Descriptor(
  name='StackUser',
  full_name='endpoints.StackUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='endpoints.StackUser.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=82,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['StackUsers'] = _STACKUSERS
DESCRIPTOR.message_types_by_name['StackUser'] = _STACKUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StackUsers = _reflection.GeneratedProtocolMessageType('StackUsers', (_message.Message,), dict(
  DESCRIPTOR = _STACKUSERS,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.StackUsers)
  ))
_sym_db.RegisterMessage(StackUsers)

StackUser = _reflection.GeneratedProtocolMessageType('StackUser', (_message.Message,), dict(
  DESCRIPTOR = _STACKUSER,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.StackUser)
  ))
_sym_db.RegisterMessage(StackUser)



_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='endpoints.Users',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=113,
  serialized_end=181,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUsers',
    full_name='endpoints.Users.GetUsers',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_STACKUSERS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS

# @@protoc_insertion_point(module_scope)
