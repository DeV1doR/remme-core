# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: permission.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='permission.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10permission.proto\"\x84\x01\n\x10PermissionMethod\"p\n\x06Method\x12\x13\n\x0f\x43REATE_DOCUMENT\x10\x00\x12\x13\n\x0fUPDATE_DOCUMENT\x10\x01\x12\x11\n\rREAD_DOCUMENT\x10\x02\x12\x11\n\rCREATE_ACCESS\x10\x03\x12\x16\n\x12UPDATE_LIST_ACCESS\x10\x04\"7\n\x06\x41\x63\x63\x65ss\x12\x19\n\x11pub_container_key\x18\x01 \x01(\t\x12\x12\n\naccess_key\x18\x02 \x01(\t\"?\n\x08\x44ocument\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x19\n\x08\x61\x63\x63\x65sses\x18\x03 \x03(\x0b\x32\x07.Access\"\xa2\x01\n\x12PermissionProtocol\x12\x19\n\x11pub_container_key\x18\x01 \x01(\t\x12\x12\n\naccess_key\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x04 \x01(\t\x12\x1f\n\x17grant_pub_container_key\x18\x05 \x01(\t\x12\x19\n\x08\x61\x63\x63\x65sses\x18\x06 \x03(\x0b\x32\x07.Accessb\x06proto3')
)



_PERMISSIONMETHOD_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='PermissionMethod.Method',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE_DOCUMENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_DOCUMENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_DOCUMENT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_ACCESS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_LIST_ACCESS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=41,
  serialized_end=153,
)
_sym_db.RegisterEnumDescriptor(_PERMISSIONMETHOD_METHOD)


_PERMISSIONMETHOD = _descriptor.Descriptor(
  name='PermissionMethod',
  full_name='PermissionMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERMISSIONMETHOD_METHOD,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=153,
)


_ACCESS = _descriptor.Descriptor(
  name='Access',
  full_name='Access',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_container_key', full_name='Access.pub_container_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='Access.access_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=210,
)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Document.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Document.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accesses', full_name='Document.accesses', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=275,
)


_PERMISSIONPROTOCOL = _descriptor.Descriptor(
  name='PermissionProtocol',
  full_name='PermissionProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_container_key', full_name='PermissionProtocol.pub_container_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='PermissionProtocol.access_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='PermissionProtocol.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='document_id', full_name='PermissionProtocol.document_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grant_pub_container_key', full_name='PermissionProtocol.grant_pub_container_key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accesses', full_name='PermissionProtocol.accesses', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=440,
)

_PERMISSIONMETHOD_METHOD.containing_type = _PERMISSIONMETHOD
_DOCUMENT.fields_by_name['accesses'].message_type = _ACCESS
_PERMISSIONPROTOCOL.fields_by_name['accesses'].message_type = _ACCESS
DESCRIPTOR.message_types_by_name['PermissionMethod'] = _PERMISSIONMETHOD
DESCRIPTOR.message_types_by_name['Access'] = _ACCESS
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['PermissionProtocol'] = _PERMISSIONPROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PermissionMethod = _reflection.GeneratedProtocolMessageType('PermissionMethod', (_message.Message,), dict(
  DESCRIPTOR = _PERMISSIONMETHOD,
  __module__ = 'permission_pb2'
  # @@protoc_insertion_point(class_scope:PermissionMethod)
  ))
_sym_db.RegisterMessage(PermissionMethod)

Access = _reflection.GeneratedProtocolMessageType('Access', (_message.Message,), dict(
  DESCRIPTOR = _ACCESS,
  __module__ = 'permission_pb2'
  # @@protoc_insertion_point(class_scope:Access)
  ))
_sym_db.RegisterMessage(Access)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENT,
  __module__ = 'permission_pb2'
  # @@protoc_insertion_point(class_scope:Document)
  ))
_sym_db.RegisterMessage(Document)

PermissionProtocol = _reflection.GeneratedProtocolMessageType('PermissionProtocol', (_message.Message,), dict(
  DESCRIPTOR = _PERMISSIONPROTOCOL,
  __module__ = 'permission_pb2'
  # @@protoc_insertion_point(class_scope:PermissionProtocol)
  ))
_sym_db.RegisterMessage(PermissionProtocol)


# @@protoc_insertion_point(module_scope)
