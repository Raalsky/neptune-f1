import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_car_setup_data import CarSetupData, PacketCarSetupData
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


def single():
    return CarSetupData(
        m_front_wing=2,
        m_rear_wing=3,
        m_on_throttle=40,
        m_off_throttle=70,
        m_front_camber=-0.5,
        m_rear_camber=0.0,
        m_front_toe=0.5,
        m_rear_toe=1.0,
        m_front_suspension=12,
        m_rear_suspension=24,
        m_front_anti_roll_bar=20,
        m_rear_anti_roll_bar=10,
        m_front_suspension_height=5,
        m_rear_suspension_height=4,
        m_brake_pressure=80,
        m_brake_bias=40,
        m_rear_left_tyre_pressure=1.0,
        m_rear_right_tyre_pressure=2.0,
        m_front_left_tyre_pressure=3.5,
        m_front_right_tyre_pressure=4.0,
        m_ballast=8,
        m_fuel_load=28.5,
    )


def single__dict_representation():
    return {
        "m_front_wing": 2,
        "m_rear_wing": 3,
        "m_on_throttle": 40,
        "m_off_throttle": 70,
        "m_front_camber": -0.5,
        "m_rear_camber": 0.0,
        "m_front_toe": 0.5,
        "m_rear_toe": 1.0,
        "m_front_suspension": 12,
        "m_rear_suspension": 24,
        "m_front_anti_roll_bar": 20,
        "m_rear_anti_roll_bar": 10,
        "m_front_suspension_height": 5,
        "m_rear_suspension_height": 4,
        "m_brake_pressure": 80,
        "m_brake_bias": 40,
        "m_rear_left_tyre_pressure": 1.0,
        "m_rear_right_tyre_pressure": 2.0,
        "m_front_left_tyre_pressure": 3.5,
        "m_front_right_tyre_pressure": 4.0,
        "m_ballast": 8,
        "m_fuel_load": 28.5,
    }


def single__json_representation():
    return """{
      "m_ballast": 8,
      "m_brake_bias": 40,
      "m_brake_pressure": 80,
      "m_front_anti_roll_bar": 20,
      "m_front_camber": -0.5,
      "m_front_left_tyre_pressure": 3.5,
      "m_front_right_tyre_pressure": 4.0,
      "m_front_suspension": 12,
      "m_front_suspension_height": 5,
      "m_front_toe": 0.5,
      "m_front_wing": 2,
      "m_fuel_load": 28.5,
      "m_off_throttle": 70,
      "m_on_throttle": 40,
      "m_rear_anti_roll_bar": 10,
      "m_rear_camber": 0.0,
      "m_rear_left_tyre_pressure": 1.0,
      "m_rear_right_tyre_pressure": 2.0,
      "m_rear_suspension": 24,
      "m_rear_suspension_height": 4,
      "m_rear_toe": 1.0,
      "m_rear_wing": 3
    }"""


def single__binary_representation():
    return (
        b"\x02\x03\x28\x46\x00\x00\x00\xbf\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x00\x80\x3f\x0c\x18\x14\x0a\x05\x04"
        b"\x50\x28\x00\x00\x80\x3f\x00\x00\x00\x40\x00\x00\x60\x40\x00\x00\x80\x40\x08\x00\x00\xe4\x41"
    )


@pytest.fixture
def packet():
    return PacketCarSetupData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=5,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_car_setups=(CarSetupData * 22)(*[single() for _ in range(22)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 5,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_car_setups": [single__dict_representation() for _ in range(22)],
    }


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_car_setups": [\n    '
        f"{entries}\n"
        "  ],\n"
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 5,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  }\n"
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x05\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + single__binary_representation() * 22
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Front wing aero
        ("m_front_wing", ctypes.c_uint8),
        # Rear wing aero
        ("m_rear_wing", ctypes.c_uint8),
        # Differential adjustment on throttle (percentage)
        ("m_on_throttle", ctypes.c_uint8),
        # Differential adjustment off throttle (percentage)
        ("m_off_throttle", ctypes.c_uint8),
        # Front camber angle (suspension geometry)
        ("m_front_camber", ctypes.c_float),
        # Rear camber angle (suspension geometry)
        ("m_rear_camber", ctypes.c_float),
        # Front toe angle (suspension geometry)
        ("m_front_toe", ctypes.c_float),
        # Rear toe angle (suspension geometry)
        ("m_rear_toe", ctypes.c_float),
        # Front suspension
        ("m_front_suspension", ctypes.c_uint8),
        # Rear suspension
        ("m_rear_suspension", ctypes.c_uint8),
        # Front anti-roll bar
        ("m_front_anti_roll_bar", ctypes.c_uint8),
        # Front anti-roll bar
        ("m_rear_anti_roll_bar", ctypes.c_uint8),
        # Front ride height
        ("m_front_suspension_height", ctypes.c_uint8),
        # Rear ride height
        ("m_rear_suspension_height", ctypes.c_uint8),
        # Brake pressure (percentage)
        ("m_brake_pressure", ctypes.c_uint8),
        # Brake bias (percentage)
        ("m_brake_bias", ctypes.c_uint8),
        # Rear left tyre pressure (PSI)
        ("m_rear_left_tyre_pressure", ctypes.c_float),
        # Rear right tyre pressure (PSI)
        ("m_rear_right_tyre_pressure", ctypes.c_float),
        # Front left tyre pressure (PSI)
        ("m_front_left_tyre_pressure", ctypes.c_float),
        # Front right tyre pressure (PSI)
        ("m_front_right_tyre_pressure", ctypes.c_float),
        # Ballast
        ("m_ballast", ctypes.c_uint8),
        # Fuel load
        ("m_fuel_load", ctypes.c_float),
    ],
)
def test_car_setup_data__field__types(type_name, type_class):
    packet_type = CarSetupData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        ("m_car_setups", CarSetupData * 22),
    ],
)
def test_packet_car_setup_data__field__types(type_name, type_class):
    packet_type = PacketCarSetupData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_car_setup_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_car_setup_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_car_setup_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_car_setup_data__to_binary(packet, binary_representation):
    print("".join(f"\\x{x:02x}" for x in packet.pack()))
    assert packet.pack() == binary_representation


def test_packet_car_setup_data__from_binary(binary_representation, dict_representation):
    packet = PacketCarSetupData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
