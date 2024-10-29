# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensor_converter_calculator.proto
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
from mediapipe.gpu import gpu_origin_pb2 as mediapipe_dot_gpu_dot_gpu__origin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>mediapipe/calculators/tensor/tensor_converter_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xb4\x04\n TensorConverterCalculatorOptions\x12\x19\n\x0bzero_center\x18\x01 \x01(\x08:\x04true\x12\'\n\x18use_custom_normalization\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x16\n\ncustom_div\x18\x07 \x01(\x02:\x02-1\x12\x16\n\ncustom_sub\x18\x08 \x01(\x02:\x02-1\x12\x1e\n\x0f\x66lip_vertically\x18\x02 \x01(\x08:\x05\x66\x61lse\x12-\n\ngpu_origin\x18\n \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12\x1b\n\x10max_num_channels\x18\x03 \x01(\x05:\x01\x33\x12\x1f\n\x10row_major_matrix\x18\x04 \x01(\x08:\x05\x66\x61lse\x12$\n\x15use_quantized_tensors\x18\x05 \x01(\x08:\x05\x66\x61lse\x12_\n\x19output_tensor_float_range\x18\t \x01(\x0b\x32<.mediapipe.TensorConverterCalculatorOptions.TensorFloatRange\x1a,\n\x10TensorFloatRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\x32Z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xad\x8d\x8c\xa0\x01 \x01(\x0b\x32+.mediapipe.TensorConverterCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.tensor.tensor_converter_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TENSORCONVERTERCALCULATOROPTIONS']._serialized_start=148
  _globals['_TENSORCONVERTERCALCULATOROPTIONS']._serialized_end=712
  _globals['_TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE']._serialized_start=576
  _globals['_TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE']._serialized_end=620
# @@protoc_insertion_point(module_scope)
