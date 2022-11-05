import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_final_classification_data import (
    FinalClassificationData,
    PacketFinalClassificationData,
)
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


def single():
    return FinalClassificationData(
        m_position=2,
        m_num_laps=39,
        m_grid_position=2,
        m_points=19,
        m_num_pit_stops=1,
        m_result_status=3,
        m_best_lap_time_in_ms=5432,
        m_total_race_time=765432.0,
        m_penalties_time=0,
        m_num_penalties=0,
        m_num_tyre_stints=1,
        m_tyre_stints_actual=(ctypes.c_uint8 * 8)(16, 0, 0, 0, 0, 0, 0, 0),
        m_tyre_stints_visual=(ctypes.c_uint8 * 8)(16, 0, 0, 0, 0, 0, 0, 0),
    )


def single__dict_representation():
    return {
        "m_position": 2,
        "m_num_laps": 39,
        "m_grid_position": 2,
        "m_points": 19,
        "m_num_pit_stops": 1,
        "m_result_status": 3,
        "m_best_lap_time_in_ms": 5432,
        "m_total_race_time": 765432.0,
        "m_penalties_time": 0,
        "m_num_penalties": 0,
        "m_num_tyre_stints": 1,
        "m_tyre_stints_actual": [16, 0, 0, 0, 0, 0, 0, 0],
        "m_tyre_stints_visual": [16, 0, 0, 0, 0, 0, 0, 0],
    }


def single__json_representation():
    return """{
      "m_best_lap_time_in_ms": 5432,
      "m_grid_position": 2,
      "m_num_laps": 39,
      "m_num_penalties": 0,
      "m_num_pit_stops": 1,
      "m_num_tyre_stints": 1,
      "m_penalties_time": 0,
      "m_points": 19,
      "m_position": 2,
      "m_result_status": 3,
      "m_total_race_time": 765432.0,
      "m_tyre_stints_actual": [
        16,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "m_tyre_stints_visual": [
        16,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    }"""


def single__binary_representation():
    return (
        b"\x02\x27\x02\x13\x01\x03\x38\x15\x00\x00\x00\x00\x00\x00\xf0\x5b\x27\x41\x00\x00\x01\x10\x00\x00\x00\x00\x00"
        b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00"
    )


@pytest.fixture
def packet():
    return PacketFinalClassificationData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=8,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_num_cars=20,
        m_classification_data=(FinalClassificationData * 22)(*[single() for _ in range(22)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 8,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_num_cars": 20,
        "m_classification_data": [single__dict_representation() for _ in range(22)],
    }


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_classification_data": [\n    '
        f"{entries}\n"
        "  ],\n"
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 8,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_num_cars": 20\n'
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x08\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff\x14"
        + single__binary_representation() * 22
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Finishing position
        ("m_position", ctypes.c_uint8),
        # Number of laps completed
        ("m_num_laps", ctypes.c_uint8),
        # Grid position of the car
        ("m_grid_position", ctypes.c_uint8),
        # Number of points scored
        ("m_points", ctypes.c_uint8),
        # Number of pit stops made
        ("m_num_pit_stops", ctypes.c_uint8),
        # Result status - 0 = invalid, 1 = inactive, 2 = active
        # 3 = finished, 4 = didnotfinish, 5 = disqualified
        # 6 = not classified, 7 = retired
        ("m_result_status", ctypes.c_uint8),
        # Best lap time of the session in milliseconds
        ("m_best_lap_time_in_ms", ctypes.c_uint32),
        # Total race time in seconds without penalties
        ("m_total_race_time", ctypes.c_double),
        # Total penalties accumulated in seconds
        ("m_penalties_time", ctypes.c_uint8),
        # Number of penalties applied to this driver
        ("m_num_penalties", ctypes.c_uint8),
        # Number of tyres stints up to maximum
        ("m_num_tyre_stints", ctypes.c_uint8),
        # Actual tyres used by this driver
        ("m_tyre_stints_actual", ctypes.c_uint8 * 8),
        # Visual tyres used by this driver
        ("m_tyre_stints_visual", ctypes.c_uint8 * 8),
    ],
)
def test_final_classification_data__field__types(type_name, type_class):
    packet_type = FinalClassificationData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Number of cars in the final classification
        ("m_num_cars", ctypes.c_uint8),
        ("m_classification_data", FinalClassificationData * 22),
    ],
)
def test_packet_final_classification_data__field__types(type_name, type_class):
    packet_type = PacketFinalClassificationData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_final_classification_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_final_classification_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_final_classification_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_final_classification_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_final_classification_data__from_binary(binary_representation, dict_representation):
    packet = PacketFinalClassificationData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
