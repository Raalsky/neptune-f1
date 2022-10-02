import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_car_damage_data import CarDamageData, PacketCarDamageData
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


def single_car_damage():
    return CarDamageData(
        m_brakes_damage=(ctypes.c_uint8 * 4)(10, 20, 30, 40),
        m_diffuser_damage=0,
        m_drs_fault=1,
        m_engine_cewear=10,
        m_engine_damage=20,
        m_engine_eswear=30,
        m_engine_icewear=40,
        m_engine_mguhwear=50,
        m_engine_mgukwear=60,
        m_engine_tcwear=70,
        m_floor_damage=12,
        m_front_left_wing_damage=20,
        m_front_right_wing_damage=40,
        m_gear_box_damage=38,
        m_rear_wing_damage=4,
        m_sidepod_damage=19,
        m_tyres_damage=(ctypes.c_uint8 * 4)(10, 20, 30, 40),
        m_tyres_wear=(ctypes.c_float * 4)(0.0, 1.0, 0.5, 0.0),
    )


def single_car_damage__dict_representation():
    return {
        "m_brakes_damage": [10, 20, 30, 40],
        "m_diffuser_damage": 0,
        "m_drs_fault": 1,
        "m_engine_cewear": 10,
        "m_engine_damage": 20,
        "m_engine_eswear": 30,
        "m_engine_icewear": 40,
        "m_engine_mguhwear": 50,
        "m_engine_mgukwear": 60,
        "m_engine_tcwear": 70,
        "m_floor_damage": 12,
        "m_front_left_wing_damage": 20,
        "m_front_right_wing_damage": 40,
        "m_gear_box_damage": 38,
        "m_rear_wing_damage": 4,
        "m_sidepod_damage": 19,
        "m_tyres_damage": [10, 20, 30, 40],
        "m_tyres_wear": [0.0, 1.0, 0.5, 0.0],
    }


@pytest.fixture
def packet():
    return PacketCarDamageData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=10,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_car_damage_data=(CarDamageData * 22)(*[single_car_damage() for _ in range(22)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 10,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_car_damage_data": [single_car_damage__dict_representation() for _ in range(22)],
    }


def single_car_damage__json_representation():
    return """{
      "m_brakes_damage": [
        10,
        20,
        30,
        40
      ],
      "m_diffuser_damage": 0,
      "m_drs_fault": 1,
      "m_engine_cewear": 10,
      "m_engine_damage": 20,
      "m_engine_eswear": 30,
      "m_engine_icewear": 40,
      "m_engine_mguhwear": 50,
      "m_engine_mgukwear": 60,
      "m_engine_tcwear": 70,
      "m_floor_damage": 12,
      "m_front_left_wing_damage": 20,
      "m_front_right_wing_damage": 40,
      "m_gear_box_damage": 38,
      "m_rear_wing_damage": 4,
      "m_sidepod_damage": 19,
      "m_tyres_damage": [
        10,
        20,
        30,
        40
      ],
      "m_tyres_wear": [
        0.0,
        1.0,
        0.5,
        0.0
      ]
    }"""


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single_car_damage__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_car_damage_data": [\n    '
        f"{entries}\n"
        "  ],\n"
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 10,\n'
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
    entry = (
        b"\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x3f\x00\x00\x00\x00\x0a\x14\x1e\x28\x0a\x14\x1e\x28\x14"
        b"\x28\x04\x0c\x00\x13\x01\x26\x14\x32\x1e\x0a\x28\x3c\x46"
    )
    return (
        b"\xe5\x07\x01\x17\x19\x0a\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff" + entry * 22
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Tyre wear (percentage)
        ("m_tyres_wear", ctypes.c_float * 4),
        # Tyre damage (percentage)
        ("m_tyres_damage", ctypes.c_uint8 * 4),
        # Brakes damage (percentage)
        ("m_brakes_damage", ctypes.c_uint8 * 4),
        # Front left wing damage (percentage)
        ("m_front_left_wing_damage", ctypes.c_uint8),
        # Front right wing damage (percentage)
        ("m_front_right_wing_damage", ctypes.c_uint8),
        # Rear wing damage (percentage)
        ("m_rear_wing_damage", ctypes.c_uint8),
        # Floor damage (percentage)
        ("m_floor_damage", ctypes.c_uint8),
        # Diffuser damage (percentage)
        ("m_diffuser_damage", ctypes.c_uint8),
        # Sidepod damage (percentage)
        ("m_sidepod_damage", ctypes.c_uint8),
        # Indicator for DRS fault, 0 = OK, 1 = fault
        ("m_drs_fault", ctypes.c_uint8),
        # Gear box damage (percentage)
        ("m_gear_box_damage", ctypes.c_uint8),
        # Engine damage (percentage)
        ("m_engine_damage", ctypes.c_uint8),
        # Engine wear MGU-H (percentage)
        ("m_engine_mguhwear", ctypes.c_uint8),
        # Engine wear ES (percentage)
        ("m_engine_eswear", ctypes.c_uint8),
        # Engine wear CE (percentage)
        ("m_engine_cewear", ctypes.c_uint8),
        # Engine wear ICE (percentage)
        ("m_engine_icewear", ctypes.c_uint8),
        # Engine wear MGU-K (percentage)
        ("m_engine_mgukwear", ctypes.c_uint8),
        # Engine wear TC (percentage)
        ("m_engine_tcwear", ctypes.c_uint8),
    ],
)
def test_car_damage_data__field__types(type_name, type_class):
    packet_type = CarDamageData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        ("m_car_damage_data", CarDamageData * 22),
    ],
)
def test_packet_car_damage_data__field__types(type_name, type_class):
    packet_type = PacketCarDamageData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_car_damage_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_car_damage_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_car_damage_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_car_damage_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_car_damage_data__from_binary(binary_representation, dict_representation):
    packet = PacketCarDamageData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
