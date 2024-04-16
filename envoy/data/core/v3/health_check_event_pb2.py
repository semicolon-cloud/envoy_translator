# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/data/core/v3/health_check_event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import address_pb2 as envoy_dot_config_dot_core_dot_v3_dot_address__pb2
from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+envoy/data/core/v3/health_check_event.proto\x12\x12\x65nvoy.data.core.v3\x1a\"envoy/config/core/v3/address.proto\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xfb\x05\n\x10HealthCheckEvent\x12L\n\x13health_checker_type\x18\x01 \x01(\x0e\x32%.envoy.data.core.v3.HealthCheckerTypeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12+\n\x04host\x18\x02 \x01(\x0b\x32\x1d.envoy.config.core.v3.Address\x12\x1d\n\x0c\x63luster_name\x18\x03 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12N\n\x15\x65ject_unhealthy_event\x18\x04 \x01(\x0b\x32-.envoy.data.core.v3.HealthCheckEjectUnhealthyH\x00\x12\x46\n\x11\x61\x64\x64_healthy_event\x18\x05 \x01(\x0b\x32).envoy.data.core.v3.HealthCheckAddHealthyH\x00\x12L\n\x1ahealth_check_failure_event\x18\x07 \x01(\x0b\x32&.envoy.data.core.v3.HealthCheckFailureH\x00\x12H\n\x15\x64\x65graded_healthy_host\x18\x08 \x01(\x0b\x32\'.envoy.data.core.v3.DegradedHealthyHostH\x00\x12K\n\x17no_longer_degraded_host\x18\t \x01(\x0b\x32(.envoy.data.core.v3.NoLongerDegradedHostH\x00\x12-\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x08metadata\x18\n \x01(\x0b\x32\x1e.envoy.config.core.v3.Metadata\x12\x30\n\x08locality\x18\x0b \x01(\x0b\x32\x1e.envoy.config.core.v3.Locality:/\x9a\xc5\x88\x1e*\n(envoy.data.core.v2alpha.HealthCheckEventB\x0c\n\x05\x65vent\x12\x03\xf8\x42\x01\"\xa1\x01\n\x19HealthCheckEjectUnhealthy\x12J\n\x0c\x66\x61ilure_type\x18\x01 \x01(\x0e\x32*.envoy.data.core.v3.HealthCheckFailureTypeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01:8\x9a\xc5\x88\x1e\x33\n1envoy.data.core.v2alpha.HealthCheckEjectUnhealthy\"b\n\x15HealthCheckAddHealthy\x12\x13\n\x0b\x66irst_check\x18\x01 \x01(\x08:4\x9a\xc5\x88\x1e/\n-envoy.data.core.v2alpha.HealthCheckAddHealthy\"\xa8\x01\n\x12HealthCheckFailure\x12J\n\x0c\x66\x61ilure_type\x18\x01 \x01(\x0e\x32*.envoy.data.core.v3.HealthCheckFailureTypeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x13\n\x0b\x66irst_check\x18\x02 \x01(\x08:1\x9a\xc5\x88\x1e,\n*envoy.data.core.v2alpha.HealthCheckFailure\"I\n\x13\x44\x65gradedHealthyHost:2\x9a\xc5\x88\x1e-\n+envoy.data.core.v2alpha.DegradedHealthyHost\"K\n\x14NoLongerDegradedHost:3\x9a\xc5\x88\x1e.\n,envoy.data.core.v2alpha.NoLongerDegradedHost*S\n\x16HealthCheckFailureType\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0b\n\x07PASSIVE\x10\x01\x12\x0b\n\x07NETWORK\x10\x02\x12\x13\n\x0fNETWORK_TIMEOUT\x10\x03*G\n\x11HealthCheckerType\x12\x08\n\x04HTTP\x10\x00\x12\x07\n\x03TCP\x10\x01\x12\x08\n\x04GRPC\x10\x02\x12\t\n\x05REDIS\x10\x03\x12\n\n\x06THRIFT\x10\x04\x42\x85\x01\n io.envoyproxy.envoy.data.core.v3B\x15HealthCheckEventProtoP\x01Z@github.com/envoyproxy/go-control-plane/envoy/data/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.data.core.v3.health_check_event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n io.envoyproxy.envoy.data.core.v3B\025HealthCheckEventProtoP\001Z@github.com/envoyproxy/go-control-plane/envoy/data/core/v3;corev3\272\200\310\321\006\002\020\002'
  _globals['_HEALTHCHECKEVENT'].oneofs_by_name['event']._options = None
  _globals['_HEALTHCHECKEVENT'].oneofs_by_name['event']._serialized_options = b'\370B\001'
  _globals['_HEALTHCHECKEVENT'].fields_by_name['health_checker_type']._options = None
  _globals['_HEALTHCHECKEVENT'].fields_by_name['health_checker_type']._serialized_options = b'\372B\005\202\001\002\020\001'
  _globals['_HEALTHCHECKEVENT'].fields_by_name['cluster_name']._options = None
  _globals['_HEALTHCHECKEVENT'].fields_by_name['cluster_name']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_HEALTHCHECKEVENT']._options = None
  _globals['_HEALTHCHECKEVENT']._serialized_options = b'\232\305\210\036*\n(envoy.data.core.v2alpha.HealthCheckEvent'
  _globals['_HEALTHCHECKEJECTUNHEALTHY'].fields_by_name['failure_type']._options = None
  _globals['_HEALTHCHECKEJECTUNHEALTHY'].fields_by_name['failure_type']._serialized_options = b'\372B\005\202\001\002\020\001'
  _globals['_HEALTHCHECKEJECTUNHEALTHY']._options = None
  _globals['_HEALTHCHECKEJECTUNHEALTHY']._serialized_options = b'\232\305\210\0363\n1envoy.data.core.v2alpha.HealthCheckEjectUnhealthy'
  _globals['_HEALTHCHECKADDHEALTHY']._options = None
  _globals['_HEALTHCHECKADDHEALTHY']._serialized_options = b'\232\305\210\036/\n-envoy.data.core.v2alpha.HealthCheckAddHealthy'
  _globals['_HEALTHCHECKFAILURE'].fields_by_name['failure_type']._options = None
  _globals['_HEALTHCHECKFAILURE'].fields_by_name['failure_type']._serialized_options = b'\372B\005\202\001\002\020\001'
  _globals['_HEALTHCHECKFAILURE']._options = None
  _globals['_HEALTHCHECKFAILURE']._serialized_options = b'\232\305\210\036,\n*envoy.data.core.v2alpha.HealthCheckFailure'
  _globals['_DEGRADEDHEALTHYHOST']._options = None
  _globals['_DEGRADEDHEALTHYHOST']._serialized_options = b'\232\305\210\036-\n+envoy.data.core.v2alpha.DegradedHealthyHost'
  _globals['_NOLONGERDEGRADEDHOST']._options = None
  _globals['_NOLONGERDEGRADEDHOST']._serialized_options = b'\232\305\210\036.\n,envoy.data.core.v2alpha.NoLongerDegradedHost'
  _globals['_HEALTHCHECKFAILURETYPE']._serialized_start=1613
  _globals['_HEALTHCHECKFAILURETYPE']._serialized_end=1696
  _globals['_HEALTHCHECKERTYPE']._serialized_start=1698
  _globals['_HEALTHCHECKERTYPE']._serialized_end=1769
  _globals['_HEALTHCHECKEVENT']._serialized_start=261
  _globals['_HEALTHCHECKEVENT']._serialized_end=1024
  _globals['_HEALTHCHECKEJECTUNHEALTHY']._serialized_start=1027
  _globals['_HEALTHCHECKEJECTUNHEALTHY']._serialized_end=1188
  _globals['_HEALTHCHECKADDHEALTHY']._serialized_start=1190
  _globals['_HEALTHCHECKADDHEALTHY']._serialized_end=1288
  _globals['_HEALTHCHECKFAILURE']._serialized_start=1291
  _globals['_HEALTHCHECKFAILURE']._serialized_end=1459
  _globals['_DEGRADEDHEALTHYHOST']._serialized_start=1461
  _globals['_DEGRADEDHEALTHYHOST']._serialized_end=1534
  _globals['_NOLONGERDEGRADEDHOST']._serialized_start=1536
  _globals['_NOLONGERDEGRADEDHOST']._serialized_end=1611
# @@protoc_insertion_point(module_scope)
