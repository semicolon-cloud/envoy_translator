# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/geoip_providers/common/v3/common.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7envoy/extensions/geoip_providers/common/v3/common.proto\x12*envoy.extensions.geoip_providers.common.v3\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xcd\x03\n\x19\x43ommonGeoipProviderConfig\x12\x83\x01\n\x12geo_headers_to_add\x18\x01 \x01(\x0b\x32].envoy.extensions.geoip_providers.common.v3.CommonGeoipProviderConfig.GeolocationHeadersToAddB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x1a\xa9\x02\n\x17GeolocationHeadersToAdd\x12\x1c\n\x07\x63ountry\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x19\n\x04\x63ity\x18\x02 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x1b\n\x06region\x18\x03 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x18\n\x03\x61sn\x18\x04 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x1c\n\x07is_anon\x18\x05 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x1d\n\x08\x61non_vpn\x18\x06 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12!\n\x0c\x61non_hosting\x18\x07 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x1d\n\x08\x61non_tor\x18\x08 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x12\x1f\n\nanon_proxy\x18\t \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xd0\x01\x01\x42\xad\x01\n8io.envoyproxy.envoy.extensions.geoip_providers.common.v3B\x0b\x43ommonProtoP\x01ZZgithub.com/envoyproxy/go-control-plane/envoy/extensions/geoip_providers/common/v3;commonv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.geoip_providers.common.v3.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n8io.envoyproxy.envoy.extensions.geoip_providers.common.v3B\013CommonProtoP\001ZZgithub.com/envoyproxy/go-control-plane/envoy/extensions/geoip_providers/common/v3;commonv3\272\200\310\321\006\002\020\002'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['country']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['country']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['city']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['city']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['region']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['region']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['asn']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['asn']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['is_anon']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['is_anon']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_vpn']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_vpn']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_hosting']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_hosting']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_tor']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_tor']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_proxy']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD'].fields_by_name['anon_proxy']._serialized_options = b'\372B\010r\006\300\001\001\320\001\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG'].fields_by_name['geo_headers_to_add']._options = None
  _globals['_COMMONGEOIPPROVIDERCONFIG'].fields_by_name['geo_headers_to_add']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_COMMONGEOIPPROVIDERCONFIG']._serialized_start=160
  _globals['_COMMONGEOIPPROVIDERCONFIG']._serialized_end=621
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD']._serialized_start=324
  _globals['_COMMONGEOIPPROVIDERCONFIG_GEOLOCATIONHEADERSTOADD']._serialized_end=621
# @@protoc_insertion_point(module_scope)