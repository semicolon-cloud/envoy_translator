# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/tap/v3/common.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.common.matcher.v3 import matcher_pb2 as envoy_dot_config_dot_common_dot_matcher_dot_v3_dot_matcher__pb2
from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.core.v3 import extension_pb2 as envoy_dot_config_dot_core_dot_v3_dot_extension__pb2
from envoy.config.core.v3 import grpc_service_pb2 as envoy_dot_config_dot_core_dot_v3_dot_grpc__service__pb2
from envoy.config.route.v3 import route_components_pb2 as envoy_dot_config_dot_route_dot_v3_dot_route__components__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n envoy/config/tap/v3/common.proto\x12\x13\x65nvoy.config.tap.v3\x1a,envoy/config/common/matcher/v3/matcher.proto\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a$envoy/config/core/v3/extension.proto\x1a\'envoy/config/core/v3/grpc_service.proto\x1a,envoy/config/route/v3/route_components.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xc7\x02\n\tTapConfig\x12\x46\n\x0cmatch_config\x18\x01 \x01(\x0b\x32#.envoy.config.tap.v3.MatchPredicateB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12=\n\x05match\x18\x04 \x01(\x0b\x32..envoy.config.common.matcher.v3.MatchPredicate\x12\x42\n\routput_config\x18\x02 \x01(\x0b\x32!.envoy.config.tap.v3.OutputConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x43\n\x0btap_enabled\x18\x03 \x01(\x0b\x32..envoy.config.core.v3.RuntimeFractionalPercent:*\x9a\xc5\x88\x1e%\n#envoy.service.tap.v2alpha.TapConfig\"\x95\x07\n\x0eMatchPredicate\x12@\n\x08or_match\x18\x01 \x01(\x0b\x32,.envoy.config.tap.v3.MatchPredicate.MatchSetH\x00\x12\x41\n\tand_match\x18\x02 \x01(\x0b\x32,.envoy.config.tap.v3.MatchPredicate.MatchSetH\x00\x12\x38\n\tnot_match\x18\x03 \x01(\x0b\x32#.envoy.config.tap.v3.MatchPredicateH\x00\x12\x1c\n\tany_match\x18\x04 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x01H\x00\x12K\n\x1ahttp_request_headers_match\x18\x05 \x01(\x0b\x32%.envoy.config.tap.v3.HttpHeadersMatchH\x00\x12L\n\x1bhttp_request_trailers_match\x18\x06 \x01(\x0b\x32%.envoy.config.tap.v3.HttpHeadersMatchH\x00\x12L\n\x1bhttp_response_headers_match\x18\x07 \x01(\x0b\x32%.envoy.config.tap.v3.HttpHeadersMatchH\x00\x12M\n\x1chttp_response_trailers_match\x18\x08 \x01(\x0b\x32%.envoy.config.tap.v3.HttpHeadersMatchH\x00\x12T\n\x1fhttp_request_generic_body_match\x18\t \x01(\x0b\x32).envoy.config.tap.v3.HttpGenericBodyMatchH\x00\x12U\n http_response_generic_body_match\x18\n \x01(\x0b\x32).envoy.config.tap.v3.HttpGenericBodyMatchH\x00\x1a\x82\x01\n\x08MatchSet\x12<\n\x05rules\x18\x01 \x03(\x0b\x32#.envoy.config.tap.v3.MatchPredicateB\x08\xfa\x42\x05\x92\x01\x02\x08\x02:8\x9a\xc5\x88\x1e\x33\n1envoy.service.tap.v2alpha.MatchPredicate.MatchSet:/\x9a\xc5\x88\x1e*\n(envoy.service.tap.v2alpha.MatchPredicateB\x0b\n\x04rule\x12\x03\xf8\x42\x01\"|\n\x10HttpHeadersMatch\x12\x35\n\x07headers\x18\x01 \x03(\x0b\x32$.envoy.config.route.v3.HeaderMatcher:1\x9a\xc5\x88\x1e,\n*envoy.service.tap.v2alpha.HttpHeadersMatch\"\xe6\x01\n\x14HttpGenericBodyMatch\x12\x13\n\x0b\x62ytes_limit\x18\x01 \x01(\r\x12V\n\x08patterns\x18\x02 \x03(\x0b\x32:.envoy.config.tap.v3.HttpGenericBodyMatch.GenericTextMatchB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\x61\n\x10GenericTextMatch\x12\x1f\n\x0cstring_match\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00\x12\x1f\n\x0c\x62inary_match\x18\x02 \x01(\x0c\x42\x07\xfa\x42\x04z\x02\x10\x01H\x00\x42\x0b\n\x04rule\x12\x03\xf8\x42\x01\"\x86\x02\n\x0cOutputConfig\x12:\n\x05sinks\x18\x01 \x03(\x0b\x32\x1f.envoy.config.tap.v3.OutputSinkB\n\xfa\x42\x07\x92\x01\x04\x08\x01\x10\x01\x12;\n\x15max_buffered_rx_bytes\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12;\n\x15max_buffered_tx_bytes\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x11\n\tstreaming\x18\x04 \x01(\x08:-\x9a\xc5\x88\x1e(\n&envoy.service.tap.v2alpha.OutputConfig\"\xdc\x04\n\nOutputSink\x12@\n\x06\x66ormat\x18\x01 \x01(\x0e\x32&.envoy.config.tap.v3.OutputSink.FormatB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x42\n\x0fstreaming_admin\x18\x02 \x01(\x0b\x32\'.envoy.config.tap.v3.StreamingAdminSinkH\x00\x12;\n\x0c\x66ile_per_tap\x18\x03 \x01(\x0b\x32#.envoy.config.tap.v3.FilePerTapSinkH\x00\x12@\n\x0estreaming_grpc\x18\x04 \x01(\x0b\x32&.envoy.config.tap.v3.StreamingGrpcSinkH\x00\x12@\n\x0e\x62uffered_admin\x18\x05 \x01(\x0b\x32&.envoy.config.tap.v3.BufferedAdminSinkH\x00\x12\x41\n\x0b\x63ustom_sink\x18\x06 \x01(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfigH\x00\"~\n\x06\x46ormat\x12\x16\n\x12JSON_BODY_AS_BYTES\x10\x00\x12\x17\n\x13JSON_BODY_AS_STRING\x10\x01\x12\x10\n\x0cPROTO_BINARY\x10\x02\x12!\n\x1dPROTO_BINARY_LENGTH_DELIMITED\x10\x03\x12\x0e\n\nPROTO_TEXT\x10\x04:+\x9a\xc5\x88\x1e&\n$envoy.service.tap.v2alpha.OutputSinkB\x17\n\x10output_sink_type\x12\x03\xf8\x42\x01\"I\n\x12StreamingAdminSink:3\x9a\xc5\x88\x1e.\n,envoy.service.tap.v2alpha.StreamingAdminSink\"\\\n\x11\x42ufferedAdminSink\x12\x1b\n\nmax_traces\x18\x01 \x01(\x04\x42\x07\xfa\x42\x04\x32\x02 \x00\x12*\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"_\n\x0e\x46ilePerTapSink\x12\x1c\n\x0bpath_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01:/\x9a\xc5\x88\x1e*\n(envoy.service.tap.v2alpha.FilePerTapSink\"\x9a\x01\n\x11StreamingGrpcSink\x12\x0e\n\x06tap_id\x18\x01 \x01(\t\x12\x41\n\x0cgrpc_service\x18\x02 \x01(\x0b\x32!.envoy.config.core.v3.GrpcServiceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01:2\x9a\xc5\x88\x1e-\n+envoy.service.tap.v2alpha.StreamingGrpcSinkB|\n!io.envoyproxy.envoy.config.tap.v3B\x0b\x43ommonProtoP\x01Z@github.com/envoyproxy/go-control-plane/envoy/config/tap/v3;tapv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.tap.v3.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!io.envoyproxy.envoy.config.tap.v3B\013CommonProtoP\001Z@github.com/envoyproxy/go-control-plane/envoy/config/tap/v3;tapv3\272\200\310\321\006\002\020\002'
  _globals['_TAPCONFIG'].fields_by_name['match_config']._options = None
  _globals['_TAPCONFIG'].fields_by_name['match_config']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _globals['_TAPCONFIG'].fields_by_name['output_config']._options = None
  _globals['_TAPCONFIG'].fields_by_name['output_config']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_TAPCONFIG']._options = None
  _globals['_TAPCONFIG']._serialized_options = b'\232\305\210\036%\n#envoy.service.tap.v2alpha.TapConfig'
  _globals['_MATCHPREDICATE_MATCHSET'].fields_by_name['rules']._options = None
  _globals['_MATCHPREDICATE_MATCHSET'].fields_by_name['rules']._serialized_options = b'\372B\005\222\001\002\010\002'
  _globals['_MATCHPREDICATE_MATCHSET']._options = None
  _globals['_MATCHPREDICATE_MATCHSET']._serialized_options = b'\232\305\210\0363\n1envoy.service.tap.v2alpha.MatchPredicate.MatchSet'
  _globals['_MATCHPREDICATE'].oneofs_by_name['rule']._options = None
  _globals['_MATCHPREDICATE'].oneofs_by_name['rule']._serialized_options = b'\370B\001'
  _globals['_MATCHPREDICATE'].fields_by_name['any_match']._options = None
  _globals['_MATCHPREDICATE'].fields_by_name['any_match']._serialized_options = b'\372B\004j\002\010\001'
  _globals['_MATCHPREDICATE']._options = None
  _globals['_MATCHPREDICATE']._serialized_options = b'\232\305\210\036*\n(envoy.service.tap.v2alpha.MatchPredicate'
  _globals['_HTTPHEADERSMATCH']._options = None
  _globals['_HTTPHEADERSMATCH']._serialized_options = b'\232\305\210\036,\n*envoy.service.tap.v2alpha.HttpHeadersMatch'
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH'].oneofs_by_name['rule']._options = None
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH'].oneofs_by_name['rule']._serialized_options = b'\370B\001'
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH'].fields_by_name['string_match']._options = None
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH'].fields_by_name['string_match']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH'].fields_by_name['binary_match']._options = None
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH'].fields_by_name['binary_match']._serialized_options = b'\372B\004z\002\020\001'
  _globals['_HTTPGENERICBODYMATCH'].fields_by_name['patterns']._options = None
  _globals['_HTTPGENERICBODYMATCH'].fields_by_name['patterns']._serialized_options = b'\372B\005\222\001\002\010\001'
  _globals['_OUTPUTCONFIG'].fields_by_name['sinks']._options = None
  _globals['_OUTPUTCONFIG'].fields_by_name['sinks']._serialized_options = b'\372B\007\222\001\004\010\001\020\001'
  _globals['_OUTPUTCONFIG']._options = None
  _globals['_OUTPUTCONFIG']._serialized_options = b'\232\305\210\036(\n&envoy.service.tap.v2alpha.OutputConfig'
  _globals['_OUTPUTSINK'].oneofs_by_name['output_sink_type']._options = None
  _globals['_OUTPUTSINK'].oneofs_by_name['output_sink_type']._serialized_options = b'\370B\001'
  _globals['_OUTPUTSINK'].fields_by_name['format']._options = None
  _globals['_OUTPUTSINK'].fields_by_name['format']._serialized_options = b'\372B\005\202\001\002\020\001'
  _globals['_OUTPUTSINK']._options = None
  _globals['_OUTPUTSINK']._serialized_options = b'\232\305\210\036&\n$envoy.service.tap.v2alpha.OutputSink'
  _globals['_STREAMINGADMINSINK']._options = None
  _globals['_STREAMINGADMINSINK']._serialized_options = b'\232\305\210\036.\n,envoy.service.tap.v2alpha.StreamingAdminSink'
  _globals['_BUFFEREDADMINSINK'].fields_by_name['max_traces']._options = None
  _globals['_BUFFEREDADMINSINK'].fields_by_name['max_traces']._serialized_options = b'\372B\0042\002 \000'
  _globals['_FILEPERTAPSINK'].fields_by_name['path_prefix']._options = None
  _globals['_FILEPERTAPSINK'].fields_by_name['path_prefix']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_FILEPERTAPSINK']._options = None
  _globals['_FILEPERTAPSINK']._serialized_options = b'\232\305\210\036*\n(envoy.service.tap.v2alpha.FilePerTapSink'
  _globals['_STREAMINGGRPCSINK'].fields_by_name['grpc_service']._options = None
  _globals['_STREAMINGGRPCSINK'].fields_by_name['grpc_service']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_STREAMINGGRPCSINK']._options = None
  _globals['_STREAMINGGRPCSINK']._serialized_options = b'\232\305\210\036-\n+envoy.service.tap.v2alpha.StreamingGrpcSink'
  _globals['_TAPCONFIG']._serialized_start=454
  _globals['_TAPCONFIG']._serialized_end=781
  _globals['_MATCHPREDICATE']._serialized_start=784
  _globals['_MATCHPREDICATE']._serialized_end=1701
  _globals['_MATCHPREDICATE_MATCHSET']._serialized_start=1509
  _globals['_MATCHPREDICATE_MATCHSET']._serialized_end=1639
  _globals['_HTTPHEADERSMATCH']._serialized_start=1703
  _globals['_HTTPHEADERSMATCH']._serialized_end=1827
  _globals['_HTTPGENERICBODYMATCH']._serialized_start=1830
  _globals['_HTTPGENERICBODYMATCH']._serialized_end=2060
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH']._serialized_start=1963
  _globals['_HTTPGENERICBODYMATCH_GENERICTEXTMATCH']._serialized_end=2060
  _globals['_OUTPUTCONFIG']._serialized_start=2063
  _globals['_OUTPUTCONFIG']._serialized_end=2325
  _globals['_OUTPUTSINK']._serialized_start=2328
  _globals['_OUTPUTSINK']._serialized_end=2932
  _globals['_OUTPUTSINK_FORMAT']._serialized_start=2736
  _globals['_OUTPUTSINK_FORMAT']._serialized_end=2862
  _globals['_STREAMINGADMINSINK']._serialized_start=2934
  _globals['_STREAMINGADMINSINK']._serialized_end=3007
  _globals['_BUFFEREDADMINSINK']._serialized_start=3009
  _globals['_BUFFEREDADMINSINK']._serialized_end=3101
  _globals['_FILEPERTAPSINK']._serialized_start=3103
  _globals['_FILEPERTAPSINK']._serialized_end=3198
  _globals['_STREAMINGGRPCSINK']._serialized_start=3201
  _globals['_STREAMINGGRPCSINK']._serialized_end=3355
# @@protoc_insertion_point(module_scope)