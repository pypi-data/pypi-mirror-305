# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/video/opencv_video_encoder_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAmediapipe/calculators/video/opencv_video_encoder_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xd4\x01\n#OpenCvVideoEncoderCalculatorOptions\x12\r\n\x05\x63odec\x18\x01 \x01(\t\x12\x14\n\x0cvideo_format\x18\x02 \x01(\t\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x32\\\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xfb\xb9\x93\x63 \x01(\x0b\x32..mediapipe.OpenCvVideoEncoderCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.video.opencv_video_encoder_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_OPENCVVIDEOENCODERCALCULATOROPTIONS']._serialized_start=119
  _globals['_OPENCVVIDEOENCODERCALCULATOROPTIONS']._serialized_end=331
# @@protoc_insertion_point(module_scope)
