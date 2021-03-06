# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataset_store.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dataset_store.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x64\x61taset_store.proto\"\x10\n\x03Key\x12\t\n\x01k\x18\x01 \x01(\t\"\x12\n\x05Value\x12\t\n\x01v\x18\x01 \x01(\t\",\n\x06KVPair\x12\x0f\n\x01k\x18\x01 \x01(\x0b\x32\x04.Key\x12\x11\n\x01v\x18\x02 \x01(\x0b\x32\x06.Value\"\x18\n\nDatSetSpec\x12\n\n\x02Id\x18\x01 \x01(\x05\"\x1a\n\x0cIteratorSpec\x12\n\n\x02Id\x18\x01 \x01(\x05\"P\n\x15\x44\x61taSetIteratorConfig\x12\x11\n\tbatchSize\x18\x01 \x01(\x05\x12\x0f\n\x07shuffle\x18\x02 \x01(\x08\x12\x13\n\x0bshuffleSeed\x18\x03 \x01(\x05\"\'\n\x07\x44\x61taset\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t2\xaf\x01\n\x0e\x44\x61taSetService\x12.\n\x0e\x63reateIterator\x12\x0b.DatSetSpec\x1a\r.IteratorSpec\"\x00\x12)\n\x0cgetNextBatch\x12\r.IteratorSpec\x1a\x08.Dataset\"\x00\x12\"\n\x0cputDatapoint\x12\x07.KVPair\x1a\x07.KVPair\"\x00\x12\x1e\n\x0cgetDatapoint\x12\x04.Key\x1a\x06.Value\"\x00\x62\x06proto3'
)




_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='Key.k', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=23,
  serialized_end=39,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v', full_name='Value.v', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=41,
  serialized_end=59,
)


_KVPAIR = _descriptor.Descriptor(
  name='KVPair',
  full_name='KVPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='KVPair.k', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='KVPair.v', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=61,
  serialized_end=105,
)


_DATSETSPEC = _descriptor.Descriptor(
  name='DatSetSpec',
  full_name='DatSetSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='DatSetSpec.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=107,
  serialized_end=131,
)


_ITERATORSPEC = _descriptor.Descriptor(
  name='IteratorSpec',
  full_name='IteratorSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='IteratorSpec.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=133,
  serialized_end=159,
)


_DATASETITERATORCONFIG = _descriptor.Descriptor(
  name='DataSetIteratorConfig',
  full_name='DataSetIteratorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batchSize', full_name='DataSetIteratorConfig.batchSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shuffle', full_name='DataSetIteratorConfig.shuffle', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shuffleSeed', full_name='DataSetIteratorConfig.shuffleSeed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=161,
  serialized_end=241,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Dataset.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='Dataset.schema', index=1,
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
  serialized_start=243,
  serialized_end=282,
)

_KVPAIR.fields_by_name['k'].message_type = _KEY
_KVPAIR.fields_by_name['v'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['KVPair'] = _KVPAIR
DESCRIPTOR.message_types_by_name['DatSetSpec'] = _DATSETSPEC
DESCRIPTOR.message_types_by_name['IteratorSpec'] = _ITERATORSPEC
DESCRIPTOR.message_types_by_name['DataSetIteratorConfig'] = _DATASETITERATORCONFIG
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:Key)
  })
_sym_db.RegisterMessage(Key)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  })
_sym_db.RegisterMessage(Value)

KVPair = _reflection.GeneratedProtocolMessageType('KVPair', (_message.Message,), {
  'DESCRIPTOR' : _KVPAIR,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:KVPair)
  })
_sym_db.RegisterMessage(KVPair)

DatSetSpec = _reflection.GeneratedProtocolMessageType('DatSetSpec', (_message.Message,), {
  'DESCRIPTOR' : _DATSETSPEC,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:DatSetSpec)
  })
_sym_db.RegisterMessage(DatSetSpec)

IteratorSpec = _reflection.GeneratedProtocolMessageType('IteratorSpec', (_message.Message,), {
  'DESCRIPTOR' : _ITERATORSPEC,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:IteratorSpec)
  })
_sym_db.RegisterMessage(IteratorSpec)

DataSetIteratorConfig = _reflection.GeneratedProtocolMessageType('DataSetIteratorConfig', (_message.Message,), {
  'DESCRIPTOR' : _DATASETITERATORCONFIG,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:DataSetIteratorConfig)
  })
_sym_db.RegisterMessage(DataSetIteratorConfig)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'dataset_store_pb2'
  # @@protoc_insertion_point(class_scope:Dataset)
  })
_sym_db.RegisterMessage(Dataset)



_DATASETSERVICE = _descriptor.ServiceDescriptor(
  name='DataSetService',
  full_name='DataSetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=285,
  serialized_end=460,
  methods=[
  _descriptor.MethodDescriptor(
    name='createIterator',
    full_name='DataSetService.createIterator',
    index=0,
    containing_service=None,
    input_type=_DATSETSPEC,
    output_type=_ITERATORSPEC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getNextBatch',
    full_name='DataSetService.getNextBatch',
    index=1,
    containing_service=None,
    input_type=_ITERATORSPEC,
    output_type=_DATASET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='putDatapoint',
    full_name='DataSetService.putDatapoint',
    index=2,
    containing_service=None,
    input_type=_KVPAIR,
    output_type=_KVPAIR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDatapoint',
    full_name='DataSetService.getDatapoint',
    index=3,
    containing_service=None,
    input_type=_KEY,
    output_type=_VALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASETSERVICE)

DESCRIPTOR.services_by_name['DataSetService'] = _DATASETSERVICE

# @@protoc_insertion_point(module_scope)
