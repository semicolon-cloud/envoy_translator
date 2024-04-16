# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/trace/v3/zipkin.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"envoy/config/trace/v3/zipkin.proto\x12\x15\x65nvoy.config.trace.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xed\x03\n\x0cZipkinConfig\x12\"\n\x11\x63ollector_cluster\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12#\n\x12\x63ollector_endpoint\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x17\n\x0ftrace_id_128bit\x18\x03 \x01(\x08\x12\x37\n\x13shared_span_context\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12`\n\x1a\x63ollector_endpoint_version\x18\x05 \x01(\x0e\x32<.envoy.config.trace.v3.ZipkinConfig.CollectorEndpointVersion\x12\x1a\n\x12\x63ollector_hostname\x18\x06 \x01(\t\x12\x1f\n\x17split_spans_for_request\x18\x07 \x01(\x08\"x\n\x18\x43ollectorEndpointVersion\x12\x33\n%DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE\x10\x00\x1a\x08\x08\x01\xa8\xf7\xb4\x8b\x02\x01\x12\r\n\tHTTP_JSON\x10\x01\x12\x0e\n\nHTTP_PROTO\x10\x02\x12\x08\n\x04GRPC\x10\x03:)\x9a\xc5\x88\x1e$\n\"envoy.config.trace.v2.ZipkinConfigB\xb1\x01\n#io.envoyproxy.envoy.config.trace.v3B\x0bZipkinProtoP\x01ZDgithub.com/envoyproxy/go-control-plane/envoy/config/trace/v3;tracev3\xf2\x98\xfe\x8f\x05)\x12\'envoy.extensions.tracers.zipkin.v4alpha\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.trace.v3.zipkin_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#io.envoyproxy.envoy.config.trace.v3B\013ZipkinProtoP\001ZDgithub.com/envoyproxy/go-control-plane/envoy/config/trace/v3;tracev3\362\230\376\217\005)\022\'envoy.extensions.tracers.zipkin.v4alpha\272\200\310\321\006\002\020\002'
  _globals['_ZIPKINCONFIG_COLLECTORENDPOINTVERSION'].values_by_name["DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE"]._options = None
  _globals['_ZIPKINCONFIG_COLLECTORENDPOINTVERSION'].values_by_name["DEPRECATED_AND_UNAVAILABLE_DO_NOT_USE"]._serialized_options = b'\010\001\250\367\264\213\002\001'
  _globals['_ZIPKINCONFIG'].fields_by_name['collector_cluster']._options = None
  _globals['_ZIPKINCONFIG'].fields_by_name['collector_cluster']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_ZIPKINCONFIG'].fields_by_name['collector_endpoint']._options = None
  _globals['_ZIPKINCONFIG'].fields_by_name['collector_endpoint']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_ZIPKINCONFIG']._options = None
  _globals['_ZIPKINCONFIG']._serialized_options = b'\232\305\210\036$\n\"envoy.config.trace.v2.ZipkinConfig'
  _globals['_ZIPKINCONFIG']._serialized_start=254
  _globals['_ZIPKINCONFIG']._serialized_end=747
  _globals['_ZIPKINCONFIG_COLLECTORENDPOINTVERSION']._serialized_start=584
  _globals['_ZIPKINCONFIG_COLLECTORENDPOINTVERSION']._serialized_end=704
# @@protoc_insertion_point(module_scope)