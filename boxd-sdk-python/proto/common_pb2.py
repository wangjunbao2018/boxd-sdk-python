# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import block_pb2 as block__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='rpcpb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x05rpcpb\x1a\x0b\x62lock.proto\"\x87\x01\n\x04Utxo\x12#\n\tout_point\x18\x01 \x01(\x0b\x32\x10.corepb.OutPoint\x12\x1d\n\x06tx_out\x18\x02 \x01(\x0b\x32\r.corepb.TxOut\x12\x14\n\x0c\x62lock_height\x18\x03 \x01(\r\x12\x13\n\x0bis_coinbase\x18\x04 \x01(\x08\x12\x10\n\x08is_spent\x18\x05 \x01(\x08\"-\n\x0c\x42\x61seResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[block__pb2.DESCRIPTOR,])




_UTXO = _descriptor.Descriptor(
  name='Utxo',
  full_name='rpcpb.Utxo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='out_point', full_name='rpcpb.Utxo.out_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_out', full_name='rpcpb.Utxo.tx_out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='rpcpb.Utxo.block_height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_coinbase', full_name='rpcpb.Utxo.is_coinbase', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_spent', full_name='rpcpb.Utxo.is_spent', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=37,
  serialized_end=172,
)


_BASERESPONSE = _descriptor.Descriptor(
  name='BaseResponse',
  full_name='rpcpb.BaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='rpcpb.BaseResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='rpcpb.BaseResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=174,
  serialized_end=219,
)

_UTXO.fields_by_name['out_point'].message_type = block__pb2._OUTPOINT
_UTXO.fields_by_name['tx_out'].message_type = block__pb2._TXOUT
DESCRIPTOR.message_types_by_name['Utxo'] = _UTXO
DESCRIPTOR.message_types_by_name['BaseResponse'] = _BASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Utxo = _reflection.GeneratedProtocolMessageType('Utxo', (_message.Message,), dict(
  DESCRIPTOR = _UTXO,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:rpcpb.Utxo)
  ))
_sym_db.RegisterMessage(Utxo)

BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), dict(
  DESCRIPTOR = _BASERESPONSE,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:rpcpb.BaseResponse)
  ))
_sym_db.RegisterMessage(BaseResponse)


# @@protoc_insertion_point(module_scope)
