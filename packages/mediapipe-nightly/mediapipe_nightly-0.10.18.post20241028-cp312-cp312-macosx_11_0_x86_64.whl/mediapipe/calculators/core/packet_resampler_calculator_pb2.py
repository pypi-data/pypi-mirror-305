# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/packet_resampler_calculator.proto
# Protobuf Python Version: 4.25.5
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<mediapipe/calculators/core/packet_resampler_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x89\x04\n PacketResamplerCalculatorOptions\x12\x16\n\nframe_rate\x18\x01 \x01(\x01:\x02-1\x12U\n\routput_header\x18\x02 \x01(\x0e\x32\x38.mediapipe.PacketResamplerCalculatorOptions.OutputHeader:\x04NONE\x12\x1f\n\x11\x66lush_last_packet\x18\x03 \x01(\x08:\x04true\x12\x0e\n\x06jitter\x18\x04 \x01(\x01\x12%\n\x16jitter_with_reflection\x18\t \x01(\x08:\x05\x66\x61lse\x12$\n\x15reproducible_sampling\x18\n \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0e\x62\x61se_timestamp\x18\x05 \x01(\x03\x12\x12\n\nstart_time\x18\x06 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x03\x12\x1b\n\x0cround_limits\x18\x08 \x01(\x08:\x05\x66\x61lse\"B\n\x0cOutputHeader\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bPASS_HEADER\x10\x01\x12\x17\n\x13UPDATE_VIDEO_HEADER\x10\x02\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xe4\xde\xd3- \x01(\x0b\x32+.mediapipe.PacketResamplerCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.core.packet_resampler_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PACKETRESAMPLERCALCULATOROPTIONS']._serialized_start=114
  _globals['_PACKETRESAMPLERCALCULATOROPTIONS']._serialized_end=635
  _globals['_PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER']._serialized_start=478
  _globals['_PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER']._serialized_end=544
# @@protoc_insertion_point(module_scope)
