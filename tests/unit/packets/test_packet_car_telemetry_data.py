import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_car_telemetry_data import CarTelemetryData, PacketCarTelemetryData
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


def single():
    return CarTelemetryData(
        m_speed=254,
        m_throttle=1.0,
        m_steer=-0.5,
        m_brake=0.0,
        m_clutch=0,
        m_gear=7,
        m_engine_rpm=12345,
        m_drs=1,
        m_rev_lights_percent=70,
        m_rev_lights_bit_value=0,
        m_brakes_temperature=(ctypes.c_uint16 * 4)(450, 460, 470, 480),
        m_tyres_surface_temperature=(ctypes.c_uint8 * 4)(50, 60, 70, 80),
        m_tyres_inner_temperature=(ctypes.c_uint8 * 4)(45, 55, 65, 75),
        m_engine_temperature=90,
        m_tyres_pressure=(ctypes.c_float * 4)(0.5, 0.5, 1.0, 1.0),
        m_surface_type=(ctypes.c_uint8 * 4)(0, 1, 2, 3),
    )


def single__dict_representation():
    return {
        "m_speed": 254,
        "m_throttle": 1.0,
        "m_steer": -0.5,
        "m_brake": 0.0,
        "m_clutch": 0,
        "m_gear": 7,
        "m_engine_rpm": 12345,
        "m_drs": 1,
        "m_rev_lights_percent": 70,
        "m_rev_lights_bit_value": 0,
        "m_brakes_temperature": [450, 460, 470, 480],
        "m_tyres_surface_temperature": [50, 60, 70, 80],
        "m_tyres_inner_temperature": [45, 55, 65, 75],
        "m_engine_temperature": 90,
        "m_tyres_pressure": [0.5, 0.5, 1.0, 1.0],
        "m_surface_type": [0, 1, 2, 3],
    }


def single__json_representation():
    return """{
      "m_brake": 0.0,
      "m_brakes_temperature": [
        450,
        460,
        470,
        480
      ],
      "m_clutch": 0,
      "m_drs": 1,
      "m_engine_rpm": 12345,
      "m_engine_temperature": 90,
      "m_gear": 7,
      "m_rev_lights_bit_value": 0,
      "m_rev_lights_percent": 70,
      "m_speed": 254,
      "m_steer": -0.5,
      "m_surface_type": [
        0,
        1,
        2,
        3
      ],
      "m_throttle": 1.0,
      "m_tyres_inner_temperature": [
        45,
        55,
        65,
        75
      ],
      "m_tyres_pressure": [
        0.5,
        0.5,
        1.0,
        1.0
      ],
      "m_tyres_surface_temperature": [
        50,
        60,
        70,
        80
      ]
    }"""


def single__binary_representation():
    return (
        b"\xfe\x00\x00\x00\x80\x3f\x00\x00\x00\xbf\x00\x00\x00\x00\x00\x07\x39\x30\x01\x46\x00\x00\xc2\x01\xcc\x01\xd6"
        b"\x01\xe0\x01\x32\x3c\x46\x50\x2d\x37\x41\x4b\x5a\x00\x00\x00\x00\x3f\x00\x00\x00\x3f\x00\x00\x80\x3f\x00\x00"
        b"\x80\x3f\x00\x01\x02\x03"
    )


@pytest.fixture
def packet():
    return PacketCarTelemetryData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=6,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_car_telemetry_data=(CarTelemetryData * 22)(*[single() for _ in range(22)]),
        m_mfd_panel_index=255,
        m_mfd_panel_index_secondary_player=255,
        m_suggested_gear=7,
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 6,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_car_telemetry_data": [single__dict_representation() for _ in range(22)],
        "m_mfd_panel_index": 255,
        "m_mfd_panel_index_secondary_player": 255,
        "m_suggested_gear": 7,
    }


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_car_telemetry_data": [\n    '
        f"{entries}\n"
        "  ],\n"
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 6,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_mfd_panel_index": 255,\n'
        '  "m_mfd_panel_index_secondary_player": 255,\n'
        '  "m_suggested_gear": 7\n'
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x06\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + single__binary_representation() * 22
        + b"\xff\xff\x07"
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Speed of car in kilometres per hour
        ("m_speed", ctypes.c_uint16),
        # Amount of throttle applied (0.0 to 1.0)
        ("m_throttle", ctypes.c_float),
        # Steering (-1.0 (full lock left) to 1.0 (full lock right))
        ("m_steer", ctypes.c_float),
        # Amount of brake applied (0.0 to 1.0)
        ("m_brake", ctypes.c_float),
        # Amount of clutch applied (0 to 100)
        ("m_clutch", ctypes.c_uint8),
        # Gear selected (1-8, N=0, R=-1)
        ("m_gear", ctypes.c_int8),
        # Engine RPM
        ("m_engine_rpm", ctypes.c_uint16),
        # 0 = off, 1 = on
        ("m_drs", ctypes.c_uint8),
        # Rev lights indicator (percentage)
        ("m_rev_lights_percent", ctypes.c_uint8),
        # Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
        ("m_rev_lights_bit_value", ctypes.c_uint16),
        # Brakes temperature (celsius)
        ("m_brakes_temperature", ctypes.c_uint16 * 4),
        # Tyres surface temperature (celsius)
        ("m_tyres_surface_temperature", ctypes.c_uint8 * 4),
        # Tyres inner temperature (celsius)
        ("m_tyres_inner_temperature", ctypes.c_uint8 * 4),
        # Engine temperature (celsius)
        ("m_engine_temperature", ctypes.c_uint16),
        # Tyres pressure (PSI)
        ("m_tyres_pressure", ctypes.c_float * 4),
        # Driving surface, see appendices
        ("m_surface_type", ctypes.c_uint8 * 4),
    ],
)
def test_car_telemetry_data__field__types(type_name, type_class):
    packet_type = CarTelemetryData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Index of MFD panel open - 255 = MFD closed
        # Single player, race – 0 = Car setup, 1 = Pits
        # 2 = Damage, 3 =  Engine, 4 = Temperatures
        # May vary depending on game mode
        ("m_car_telemetry_data", CarTelemetryData * 22),
        # See above
        ("m_mfd_panel_index", ctypes.c_uint8),
        ("m_mfd_panel_index_secondary_player", ctypes.c_uint8),
        # Suggested gear for the player (1-8)
        # 0 if no gear suggested
        ("m_suggested_gear", ctypes.c_int8),
    ],
)
def test_packet_car_telemetry_data__field__types(type_name, type_class):
    packet_type = PacketCarTelemetryData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_car_telemetry_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_car_telemetry_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_car_telemetry_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_car_telemetry_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_car_telemetry_data__from_binary(binary_representation, dict_representation):
    packet = PacketCarTelemetryData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
