import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class CarMotionData(Packet):
    _fields_ = [
        # World space X position
        ("m_world_position_x", ctypes.c_float),
        # World space Y position
        ("m_world_position_y", ctypes.c_float),
        # World space Z position
        ("m_world_position_z", ctypes.c_float),
        # Velocity in world space X
        ("m_world_velocity_x", ctypes.c_float),
        # Velocity in world space Y
        ("m_world_velocity_y", ctypes.c_float),
        # Velocity in world space Z
        ("m_world_velocity_z", ctypes.c_float),
        # World space forward X direction (normalised)
        ("m_world_forward_dir_x", ctypes.c_int16),
        # World space forward Y direction (normalised)
        ("m_world_forward_dir_y", ctypes.c_int16),
        # World space forward Z direction (normalised)
        ("m_world_forward_dir_z", ctypes.c_int16),
        # World space right X direction (normalised)
        ("m_world_right_dir_x", ctypes.c_int16),
        # World space right Y direction (normalised)
        ("m_world_right_dir_y", ctypes.c_int16),
        # World space right Z direction (normalised)
        ("m_world_right_dir_z", ctypes.c_int16),
        # Lateral G-Force component
        ("m_g_force_lateral", ctypes.c_float),
        # Longitudinal G-Force component
        ("m_g_force_longitudinal", ctypes.c_float),
        # Vertical G-Force component
        ("m_g_force_vertical", ctypes.c_float),
        # Yaw angle in radians
        ("m_yaw", ctypes.c_float),
        # Pitch angle in radians
        ("m_pitch", ctypes.c_float),
        # Roll angle in radians
        ("m_roll", ctypes.c_float),
    ]


class PacketMotionData(Packet):
    _id_ = 0
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Data for all cars on track
        # Extra player car ONLY data
        ("m_car_motion_data", CarMotionData * 22),
        # Note: All wheel arrays have the following order:
        ("m_suspension_position", ctypes.c_float * 4),
        # RL, RR, FL, FR
        ("m_suspension_velocity", ctypes.c_float * 4),
        # RL, RR, FL, FR
        ("m_suspension_acceleration", ctypes.c_float * 4),
        # Speed of each wheel
        ("m_wheel_speed", ctypes.c_float * 4),
        # Slip ratio for each wheel
        ("m_wheel_slip", ctypes.c_float * 4),
        # Velocity in local space
        ("m_local_velocity_x", ctypes.c_float),
        # Velocity in local space
        ("m_local_velocity_y", ctypes.c_float),
        # Velocity in local space
        ("m_local_velocity_z", ctypes.c_float),
        # Angular velocity x-component
        ("m_angular_velocity_x", ctypes.c_float),
        # Angular velocity y-component
        ("m_angular_velocity_y", ctypes.c_float),
        # Angular velocity z-component
        ("m_angular_velocity_z", ctypes.c_float),
        # Angular velocity x-component
        ("m_angular_acceleration_x", ctypes.c_float),
        # Angular velocity y-component
        ("m_angular_acceleration_y", ctypes.c_float),
        # Angular velocity z-component
        ("m_angular_acceleration_z", ctypes.c_float),
        # Current front wheels angle in radians
        ("m_front_wheels_angle", ctypes.c_float),
    ]
