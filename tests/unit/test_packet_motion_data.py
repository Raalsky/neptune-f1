import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_motion_data import CarMotionData, PacketMotionData


def single():
    return CarMotionData(
        m_world_position_x=256.0,
        m_world_position_y=-128.5,
        m_world_position_z=64.0,
        m_world_velocity_x=12.0,
        m_world_velocity_y=24.0,
        m_world_velocity_z=36.5,
        m_world_forward_dir_x=12345,
        m_world_forward_dir_y=23456,
        m_world_forward_dir_z=24567,
        m_world_right_dir_x=12345,
        m_world_right_dir_y=23456,
        m_world_right_dir_z=24567,
        m_g_force_lateral=1.5,
        m_g_force_vertical=1.0,
        m_g_force_longitudinal=0.5,
        m_yaw=0.5,
        m_pitch=-0.5,
        m_roll=1.0,
    )


def single__dict_representation():
    return {
        "m_world_position_x": 256.0,
        "m_world_position_y": -128.5,
        "m_world_position_z": 64.0,
        "m_world_velocity_x": 12.0,
        "m_world_velocity_y": 24.0,
        "m_world_velocity_z": 36.5,
        "m_world_forward_dir_x": 12345,
        "m_world_forward_dir_y": 23456,
        "m_world_forward_dir_z": 24567,
        "m_world_right_dir_x": 12345,
        "m_world_right_dir_y": 23456,
        "m_world_right_dir_z": 24567,
        "m_g_force_lateral": 1.5,
        "m_g_force_vertical": 1.0,
        "m_g_force_longitudinal": 0.5,
        "m_yaw": 0.5,
        "m_pitch": -0.5,
        "m_roll": 1.0,
    }


def single__json_representation():
    return """{
      "m_g_force_lateral": 1.5,
      "m_g_force_longitudinal": 0.5,
      "m_g_force_vertical": 1.0,
      "m_pitch": -0.5,
      "m_roll": 1.0,
      "m_world_forward_dir_x": 12345,
      "m_world_forward_dir_y": 23456,
      "m_world_forward_dir_z": 24567,
      "m_world_position_x": 256.0,
      "m_world_position_y": -128.5,
      "m_world_position_z": 64.0,
      "m_world_right_dir_x": 12345,
      "m_world_right_dir_y": 23456,
      "m_world_right_dir_z": 24567,
      "m_world_velocity_x": 12.0,
      "m_world_velocity_y": 24.0,
      "m_world_velocity_z": 36.5,
      "m_yaw": 0.5
    }"""


def single__binary_representation():
    return (
        b"\x00\x00\x80\x43\x00\x80\x00\xc3\x00\x00\x80\x42\x00\x00\x40\x41\x00\x00\xc0\x41\x00\x00\x12\x42\x39\x30\xa0"
        b"\x5b\xf7\x5f\x39\x30\xa0\x5b\xf7\x5f\x00\x00\xc0\x3f\x00\x00\x00\x3f\x00\x00\x80\x3f\x00\x00\x00\x3f\x00\x00"
        b"\x00\xbf\x00\x00\x80\x3f"
    )


@pytest.fixture
def packet():
    return PacketMotionData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=0,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_car_motion_data=(CarMotionData * 22)(*[single() for _ in range(22)]),
        m_suspension_position=(ctypes.c_float * 4)(0.0, 1.0, 2.0, 3.0),
        m_suspension_velocity=(ctypes.c_float * 4)(0.0, 1.0, 2.0, 3.0),
        m_suspension_acceleration=(ctypes.c_float * 4)(0.0, 1.0, 2.0, 3.0),
        m_wheel_speed=(ctypes.c_float * 4)(0.0, 1.0, 2.0, 3.0),
        m_wheel_slip=(ctypes.c_float * 4)(0.0, 1.0, 2.0, 3.0),
        m_local_velocity_x=-2.0,
        m_local_velocity_y=-1.5,
        m_local_velocity_z=-1.0,
        m_angular_velocity_x=-0.5,
        m_angular_velocity_y=0.0,
        m_angular_velocity_z=0.5,
        m_angular_acceleration_x=1.0,
        m_angular_acceleration_y=1.5,
        m_angular_acceleration_z=2.0,
        m_front_wheels_angle=2.5,
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 0,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_car_motion_data": [single__dict_representation() for _ in range(22)],
        "m_suspension_position": [0.0, 1.0, 2.0, 3.0],
        "m_suspension_velocity": [0.0, 1.0, 2.0, 3.0],
        "m_suspension_acceleration": [0.0, 1.0, 2.0, 3.0],
        "m_wheel_speed": [0.0, 1.0, 2.0, 3.0],
        "m_wheel_slip": [0.0, 1.0, 2.0, 3.0],
        "m_local_velocity_x": -2.0,
        "m_local_velocity_y": -1.5,
        "m_local_velocity_z": -1.0,
        "m_angular_velocity_x": -0.5,
        "m_angular_velocity_y": 0.0,
        "m_angular_velocity_z": 0.5,
        "m_angular_acceleration_x": 1.0,
        "m_angular_acceleration_y": 1.5,
        "m_angular_acceleration_z": 2.0,
        "m_front_wheels_angle": 2.5,
    }


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_angular_acceleration_x": 1.0,\n'
        '  "m_angular_acceleration_y": 1.5,\n'
        '  "m_angular_acceleration_z": 2.0,\n'
        '  "m_angular_velocity_x": -0.5,\n'
        '  "m_angular_velocity_y": 0.0,\n'
        '  "m_angular_velocity_z": 0.5,\n'
        '  "m_car_motion_data": [\n    '
        f"{entries}\n"
        "  ],\n"
        '  "m_front_wheels_angle": 2.5,\n'
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 0,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_local_velocity_x": -2.0,\n'
        '  "m_local_velocity_y": -1.5,\n'
        '  "m_local_velocity_z": -1.0,\n'
        '  "m_suspension_acceleration": [\n'
        "    0.0,\n"
        "    1.0,\n"
        "    2.0,\n"
        "    3.0\n"
        "  ],\n"
        '  "m_suspension_position": [\n'
        "    0.0,\n"
        "    1.0,\n"
        "    2.0,\n"
        "    3.0\n"
        "  ],\n"
        '  "m_suspension_velocity": [\n'
        "    0.0,\n"
        "    1.0,\n"
        "    2.0,\n"
        "    3.0\n"
        "  ],\n"
        '  "m_wheel_slip": [\n'
        "    0.0,\n"
        "    1.0,\n"
        "    2.0,\n"
        "    3.0\n"
        "  ],\n"
        '  "m_wheel_speed": [\n'
        "    0.0,\n"
        "    1.0,\n"
        "    2.0,\n"
        "    3.0\n"
        "  ]\n"
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x00\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + single__binary_representation() * 22
        + b"\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x40\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00"
        b"\x00\x40\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x40\x00\x00\x40\x40\x00\x00\x00\x00"
        b"\x00\x00\x80\x3f\x00\x00\x00\x40\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x40\x00\x00"
        b"\x40\x40\x00\x00\x00\xc0\x00\x00\xc0\xbf\x00\x00\x80\xbf\x00\x00\x00\xbf\x00\x00\x00\x00\x00\x00\x00\x3f"
        b"\x00\x00\x80\x3f\x00\x00\xc0\x3f\x00\x00\x00\x40\x00\x00\x20\x40"
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
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
    ],
)
def test_car_motion_data__field__types(type_name, type_class):
    packet_type = CarMotionData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Data for all cars on track
        ("m_car_motion_data", CarMotionData * 22),
        # Extra player car ONLY data
        # Note: All wheel arrays have the following order:
        # RL, RR, FL, FR
        ("m_suspension_position", ctypes.c_float * 4),
        ("m_suspension_velocity", ctypes.c_float * 4),
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
    ],
)
def test_packet_motion_data__field__types(type_name, type_class):
    packet_type = PacketMotionData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_motion_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_motion_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_motion_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_motion_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_motion_data__from_binary(binary_representation, dict_representation):
    packet = PacketMotionData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
