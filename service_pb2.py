# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\x12\x07service\"<\n\x0bHashRequest\x12\x0f\n\x07\x63omando\x18\x01 \x01(\t\x12\r\n\x05\x63have\x18\x02 \x01(\t\x12\r\n\x05valor\x18\x03 \x01(\t\"-\n\tHashReply\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\x05\x12\x10\n\x08resposta\x18\x02 \x01(\t2\xdc\x01\n\x04Hash\x12\x34\n\x06\x43reate\x12\x14.service.HashRequest\x1a\x12.service.HashReply\"\x00\x12\x32\n\x04Read\x12\x14.service.HashRequest\x1a\x12.service.HashReply\"\x00\x12\x34\n\x06Update\x12\x14.service.HashRequest\x1a\x12.service.HashReply\"\x00\x12\x34\n\x06\x44\x65lete\x12\x14.service.HashRequest\x1a\x12.service.HashReply\"\x00\x62\x06proto3'
)




_HASHREQUEST = _descriptor.Descriptor(
  name='HashRequest',
  full_name='service.HashRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='comando', full_name='service.HashRequest.comando', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chave', full_name='service.HashRequest.chave', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valor', full_name='service.HashRequest.valor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=86,
)


_HASHREPLY = _descriptor.Descriptor(
  name='HashReply',
  full_name='service.HashReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='codigo', full_name='service.HashReply.codigo', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resposta', full_name='service.HashReply.resposta', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=88,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['HashRequest'] = _HASHREQUEST
DESCRIPTOR.message_types_by_name['HashReply'] = _HASHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HashRequest = _reflection.GeneratedProtocolMessageType('HashRequest', (_message.Message,), {
  'DESCRIPTOR' : _HASHREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:service.HashRequest)
  })
_sym_db.RegisterMessage(HashRequest)

HashReply = _reflection.GeneratedProtocolMessageType('HashReply', (_message.Message,), {
  'DESCRIPTOR' : _HASHREPLY,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:service.HashReply)
  })
_sym_db.RegisterMessage(HashReply)



_HASH = _descriptor.ServiceDescriptor(
  name='Hash',
  full_name='service.Hash',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=136,
  serialized_end=356,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='service.Hash.Create',
    index=0,
    containing_service=None,
    input_type=_HASHREQUEST,
    output_type=_HASHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='service.Hash.Read',
    index=1,
    containing_service=None,
    input_type=_HASHREQUEST,
    output_type=_HASHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='service.Hash.Update',
    index=2,
    containing_service=None,
    input_type=_HASHREQUEST,
    output_type=_HASHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='service.Hash.Delete',
    index=3,
    containing_service=None,
    input_type=_HASHREQUEST,
    output_type=_HASHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HASH)

DESCRIPTOR.services_by_name['Hash'] = _HASH

# @@protoc_insertion_point(module_scope)
