# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/tracking.proto
# Protobuf Python Version: 4.25.5
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.util.tracking import motion_models_pb2 as mediapipe_dot_util_dot_tracking_dot_motion__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&mediapipe/util/tracking/tracking.proto\x12\tmediapipe\x1a+mediapipe/util/tracking/motion_models.proto\"\xe5\x08\n\x0eMotionBoxState\x12\r\n\x05pos_x\x18\x01 \x01(\x02\x12\r\n\x05pos_y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x10\n\x05scale\x18\x05 \x01(\x02:\x01\x31\x12\x13\n\x08rotation\x18\x1e \x01(\x02:\x01\x30\x12,\n\x04quad\x18\" \x01(\x0b\x32\x1e.mediapipe.MotionBoxState.Quad\x12\x14\n\x0c\x61spect_ratio\x18# \x01(\x02\x12\x1f\n\x10request_grouping\x18% \x01(\x08:\x05\x66\x61lse\x12-\n\x0epnp_homography\x18$ \x01(\x0b\x32\x15.mediapipe.Homography\x12\n\n\x02\x64x\x18\x07 \x01(\x02\x12\n\n\x02\x64y\x18\x08 \x01(\x02\x12\x16\n\x0ekinetic_energy\x18\x11 \x01(\x02\x12\x14\n\x0cprior_weight\x18\t \x01(\x02\x12J\n\x0ctrack_status\x18\n \x01(\x0e\x32%.mediapipe.MotionBoxState.TrackStatus:\rBOX_UNTRACKED\x12#\n\x17spatial_prior_grid_size\x18\x0b \x01(\x05:\x02\x31\x30\x12\x19\n\rspatial_prior\x18\x0c \x03(\x02\x42\x02\x10\x01\x12\x1e\n\x12spatial_confidence\x18\r \x03(\x02\x42\x02\x10\x01\x12\x12\n\nprior_diff\x18\x0e \x01(\x02\x12\x18\n\x10motion_disparity\x18\x0f \x01(\x02\x12!\n\x19\x62\x61\x63kground_discrimination\x18\x10 \x01(\x02\x12\x17\n\x0finlier_center_x\x18\x12 \x01(\x02\x12\x17\n\x0finlier_center_y\x18\x13 \x01(\x02\x12\x12\n\ninlier_sum\x18\x18 \x01(\x02\x12\x14\n\x0cinlier_ratio\x18\x19 \x01(\x02\x12\x14\n\x0cinlier_width\x18\x16 \x01(\x02\x12\x15\n\rinlier_height\x18\x17 \x01(\x02\x12\x16\n\ninlier_ids\x18\x1a \x03(\rB\x02\x10\x01\x12\x1f\n\x13inlier_id_match_pos\x18\x1f \x03(\rB\x02\x10\x01\x12\x19\n\rinlier_length\x18\x1b \x03(\rB\x02\x10\x01\x12\x17\n\x0boutlier_ids\x18\x1c \x03(\rB\x02\x10\x01\x12 \n\x14outlier_id_match_pos\x18  \x03(\rB\x02\x10\x01\x12\x1b\n\x13tracking_confidence\x18! \x01(\x02\x12\x33\n\x08internal\x18\x1d \x01(\x0b\x32!.mediapipe.MotionBoxInternalState\x1a\x18\n\x04Quad\x12\x10\n\x08vertices\x18\x01 \x03(\x02\"\x87\x01\n\x0bTrackStatus\x12\x11\n\rBOX_UNTRACKED\x10\x00\x12\r\n\tBOX_EMPTY\x10\x01\x12\x13\n\x0f\x42OX_NO_FEATURES\x10\x02\x12\x0f\n\x0b\x42OX_TRACKED\x10\x03\x12\x12\n\x0e\x42OX_DUPLICATED\x10\x04\x12\x1c\n\x18\x42OX_TRACKED_OUT_OF_BOUND\x10\x05J\x04\x08\x14\x10\x15J\x04\x08\x15\x10\x16\"\xbc\x01\n\x16MotionBoxInternalState\x12\x11\n\x05pos_x\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x11\n\x05pos_y\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x0e\n\x02\x64x\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x0e\n\x02\x64y\x18\x04 \x03(\x02\x42\x02\x10\x01\x12\x15\n\tcamera_dx\x18\x05 \x03(\x02\x42\x02\x10\x01\x12\x15\n\tcamera_dy\x18\x06 \x03(\x02\x42\x02\x10\x01\x12\x14\n\x08track_id\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x18\n\x0cinlier_score\x18\x08 \x03(\x02\x42\x02\x10\x01\"\x9d\x13\n\x10TrackStepOptions\x12\x62\n\x10tracking_degrees\x18\x1c \x01(\x0e\x32+.mediapipe.TrackStepOptions.TrackingDegrees:\x1bTRACKING_DEGREE_TRANSLATION\x12&\n\x17track_object_and_camera\x18  \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0firls_iterations\x18\x01 \x01(\x05:\x01\x35\x12\x1b\n\rspatial_sigma\x18\x02 \x01(\x02:\x04\x30.15\x12\x1f\n\x10min_motion_sigma\x18\x03 \x01(\x02:\x05\x30.002\x12\"\n\x15relative_motion_sigma\x18\x04 \x01(\x02:\x03\x30.3\x12)\n\x1amotion_disparity_low_level\x18\x06 \x01(\x02:\x05\x30.008\x12*\n\x1bmotion_disparity_high_level\x18\x07 \x01(\x02:\x05\x30.016\x12\x1c\n\x0f\x64isparity_decay\x18\x08 \x01(\x02:\x03\x30.8\x12 \n\x13motion_prior_weight\x18\t \x01(\x02:\x03\x30.2\x12\x32\n#background_discrimination_low_level\x18\n \x01(\x02:\x05\x30.004\x12\x33\n$background_discrimination_high_level\x18\x0b \x01(\x02:\x05\x30.008\x12,\n\x1finlier_center_relative_distance\x18\x0c \x01(\x02:\x03\x30.1\x12 \n\x13inlier_spring_force\x18\r \x01(\x02:\x03\x30.3\x12-\n kinetic_center_relative_distance\x18\x0e \x01(\x02:\x03\x30.4\x12!\n\x14kinetic_spring_force\x18\x0f \x01(\x02:\x03\x30.5\x12\x36\n\'kinetic_spring_force_min_kinetic_energy\x18\x15 \x01(\x02:\x05\x30.003\x12#\n\x16velocity_update_weight\x18\x10 \x01(\x02:\x03\x30.7\x12\x1e\n\x12max_track_failures\x18\x11 \x01(\x05:\x02\x31\x30\x12\x1c\n\x0e\x65xpansion_size\x18\x12 \x01(\x02:\x04\x30.05\x12\x1e\n\x11inlier_low_weight\x18\x13 \x01(\x02:\x03\x32\x35\x30\x12\x1f\n\x12inlier_high_weight\x18\x14 \x01(\x02:\x03\x35\x30\x30\x12\"\n\x14kinetic_energy_decay\x18\x16 \x01(\x02:\x04\x30.98\x12\"\n\x15prior_weight_increase\x18\x17 \x01(\x02:\x03\x30.2\x12!\n\x12low_kinetic_energy\x18\x18 \x01(\x02:\x05\x30.001\x12\"\n\x13high_kinetic_energy\x18\x19 \x01(\x02:\x05\x30.004\x12$\n\x15return_internal_state\x18\x1a \x01(\x08:\x05\x66\x61lse\x12\x33\n%use_post_estimation_weights_for_state\x18\x1d \x01(\x08:\x04true\x12$\n\x15\x63ompute_spatial_prior\x18\x1b \x01(\x08:\x05\x66\x61lse\x12K\n\x13irls_initialization\x18\x1e \x01(\x0b\x32..mediapipe.TrackStepOptions.IrlsInitialization\x12+\n\x1cstatic_motion_temporal_ratio\x18! \x01(\x02:\x05\x30.003\x12n\n&cancel_tracking_with_occlusion_options\x18\" \x01(\x0b\x32>.mediapipe.TrackStepOptions.CancelTrackingWithOcclusionOptions\x12/\n#object_similarity_min_contd_inliers\x18# \x01(\x05:\x02\x33\x30\x12&\n\x18\x62ox_similarity_max_scale\x18$ \x01(\x02:\x04\x31.05\x12(\n\x1b\x62ox_similarity_max_rotation\x18% \x01(\x02:\x03\x30.2\x12&\n\x19quad_homography_max_scale\x18& \x01(\x02:\x03\x31.2\x12)\n\x1cquad_homography_max_rotation\x18\' \x01(\x02:\x03\x30.3\x12G\n\x11\x63\x61mera_intrinsics\x18( \x01(\x0b\x32,.mediapipe.TrackStepOptions.CameraIntrinsics\x12\"\n\x13\x66orced_pnp_tracking\x18) \x01(\x08:\x05\x66\x61lse\x1aY\n\x12IrlsInitialization\x12\x18\n\tactivated\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x12\n\x06rounds\x18\x02 \x01(\x05:\x02\x35\x30\x12\x15\n\x06\x63utoff\x18\x03 \x01(\x02:\x05\x30.005\x1a\x81\x01\n\"CancelTrackingWithOcclusionOptions\x12\x18\n\tactivated\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\"\n\x15min_motion_continuity\x18\x02 \x01(\x02:\x03\x30.4\x12\x1d\n\x10min_inlier_ratio\x18\x03 \x01(\x02:\x03\x30.1\x1a|\n\x10\x43\x61meraIntrinsics\x12\n\n\x02\x66x\x18\x01 \x01(\x02\x12\n\n\x02\x66y\x18\x02 \x01(\x02\x12\n\n\x02\x63x\x18\x03 \x01(\x02\x12\n\n\x02\x63y\x18\x04 \x01(\x02\x12\n\n\x02k0\x18\x05 \x01(\x02\x12\n\n\x02k1\x18\x06 \x01(\x02\x12\n\n\x02k2\x18\x07 \x01(\x02\x12\t\n\x01w\x18\x08 \x01(\x05\x12\t\n\x01h\x18\t \x01(\x05\"\xe6\x02\n\x0fTrackingDegrees\x12\x1f\n\x1bTRACKING_DEGREE_TRANSLATION\x10\x00\x12 \n\x1cTRACKING_DEGREE_CAMERA_SCALE\x10\x01\x12#\n\x1fTRACKING_DEGREE_CAMERA_ROTATION\x10\x02\x12)\n%TRACKING_DEGREE_CAMERA_ROTATION_SCALE\x10\x03\x12&\n\"TRACKING_DEGREE_CAMERA_PERSPECTIVE\x10\x04\x12 \n\x1cTRACKING_DEGREE_OBJECT_SCALE\x10\x05\x12#\n\x1fTRACKING_DEGREE_OBJECT_ROTATION\x10\x06\x12)\n%TRACKING_DEGREE_OBJECT_ROTATION_SCALE\x10\x07\x12&\n\"TRACKING_DEGREE_OBJECT_PERSPECTIVE\x10\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.util.tracking.tracking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['spatial_prior']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['spatial_prior']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE'].fields_by_name['spatial_confidence']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['spatial_confidence']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE'].fields_by_name['inlier_ids']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['inlier_ids']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE'].fields_by_name['inlier_id_match_pos']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['inlier_id_match_pos']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE'].fields_by_name['inlier_length']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['inlier_length']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE'].fields_by_name['outlier_ids']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['outlier_ids']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE'].fields_by_name['outlier_id_match_pos']._options = None
  _globals['_MOTIONBOXSTATE'].fields_by_name['outlier_id_match_pos']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['pos_x']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['pos_x']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['pos_y']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['pos_y']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['dx']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['dx']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['dy']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['dy']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['camera_dx']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['camera_dx']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['camera_dy']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['camera_dy']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['track_id']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['track_id']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['inlier_score']._options = None
  _globals['_MOTIONBOXINTERNALSTATE'].fields_by_name['inlier_score']._serialized_options = b'\020\001'
  _globals['_MOTIONBOXSTATE']._serialized_start=99
  _globals['_MOTIONBOXSTATE']._serialized_end=1224
  _globals['_MOTIONBOXSTATE_QUAD']._serialized_start=1050
  _globals['_MOTIONBOXSTATE_QUAD']._serialized_end=1074
  _globals['_MOTIONBOXSTATE_TRACKSTATUS']._serialized_start=1077
  _globals['_MOTIONBOXSTATE_TRACKSTATUS']._serialized_end=1212
  _globals['_MOTIONBOXINTERNALSTATE']._serialized_start=1227
  _globals['_MOTIONBOXINTERNALSTATE']._serialized_end=1415
  _globals['_TRACKSTEPOPTIONS']._serialized_start=1418
  _globals['_TRACKSTEPOPTIONS']._serialized_end=3879
  _globals['_TRACKSTEPOPTIONS_IRLSINITIALIZATION']._serialized_start=3171
  _globals['_TRACKSTEPOPTIONS_IRLSINITIALIZATION']._serialized_end=3260
  _globals['_TRACKSTEPOPTIONS_CANCELTRACKINGWITHOCCLUSIONOPTIONS']._serialized_start=3263
  _globals['_TRACKSTEPOPTIONS_CANCELTRACKINGWITHOCCLUSIONOPTIONS']._serialized_end=3392
  _globals['_TRACKSTEPOPTIONS_CAMERAINTRINSICS']._serialized_start=3394
  _globals['_TRACKSTEPOPTIONS_CAMERAINTRINSICS']._serialized_end=3518
  _globals['_TRACKSTEPOPTIONS_TRACKINGDEGREES']._serialized_start=3521
  _globals['_TRACKSTEPOPTIONS_TRACKINGDEGREES']._serialized_end=3879
# @@protoc_insertion_point(module_scope)
