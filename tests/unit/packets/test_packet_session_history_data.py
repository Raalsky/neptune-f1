import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_session_history_data import (
    LapHistoryData,
    PacketSessionHistoryData,
    TyreStintHistoryData,
)


def lap_history_data():
    return LapHistoryData(
        m_lap_time_in_ms=12345,
        m_sector1_time_in_ms=2345,
        m_sector2_time_in_ms=1234,
        m_sector3_time_in_ms=345,
        m_lap_valid_bit_flags=0x04,
    )


def lap_history_data__dict_representation():
    return {
        "m_lap_time_in_ms": 12345,
        "m_sector1_time_in_ms": 2345,
        "m_sector2_time_in_ms": 1234,
        "m_sector3_time_in_ms": 345,
        "m_lap_valid_bit_flags": 0x04,
    }


def lap_history_data__json_representation():
    return """{
      "m_lap_time_in_ms": 12345,
      "m_lap_valid_bit_flags": 4,
      "m_sector1_time_in_ms": 2345,
      "m_sector2_time_in_ms": 1234,
      "m_sector3_time_in_ms": 345
    }"""


def lap_history_data__binary_representation():
    return b"\x39\x30\x00\x00\x29\x09\xd2\x04\x59\x01\x04"


def tyre_stint_history_data():
    return TyreStintHistoryData(m_end_lap=255, m_tyre_actual_compound=16, m_tyre_visual_compound=16)


def tyre_stint_history_data__dict_representation():
    return {"m_end_lap": 255, "m_tyre_actual_compound": 16, "m_tyre_visual_compound": 16}


def tyre_stint_history_data__json_representation():
    return """{
      "m_end_lap": 255,
      "m_tyre_actual_compound": 16,
      "m_tyre_visual_compound": 16
    }"""


def tyre_stint_history_data__binary_representation():
    return b"\xff\x10\x10"


@pytest.fixture
def packet():
    return PacketSessionHistoryData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=11,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_car_idx=2,
        m_num_laps=65,
        m_num_tyre_stints=1,
        m_best_lap_time_lap_num=12,
        m_best_sector1_lap_num=12,
        m_best_sector2_lap_num=15,
        m_best_sector3_lap_num=12,
        m_lap_history_data=(LapHistoryData * 100)(*[lap_history_data() for _ in range(100)]),
        m_tyre_stints_history_data=(TyreStintHistoryData * 8)(*[tyre_stint_history_data() for _ in range(8)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 11,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_car_idx": 2,
        "m_num_laps": 65,
        "m_num_tyre_stints": 1,
        "m_best_lap_time_lap_num": 12,
        "m_best_sector1_lap_num": 12,
        "m_best_sector2_lap_num": 15,
        "m_best_sector3_lap_num": 12,
        "m_lap_history_data": [lap_history_data__dict_representation() for _ in range(100)],
        "m_tyre_stints_history_data": [tyre_stint_history_data__dict_representation() for _ in range(8)],
    }


@pytest.fixture
def json_representation():
    laps_history = ",\n    ".join(lap_history_data__json_representation() for _ in range(100))
    tyre_stints_history = ",\n    ".join(tyre_stint_history_data__json_representation() for _ in range(8))

    return (
        "{\n"
        '  "m_best_lap_time_lap_num": 12,\n'
        '  "m_best_sector1_lap_num": 12,\n'
        '  "m_best_sector2_lap_num": 15,\n'
        '  "m_best_sector3_lap_num": 12,\n'
        '  "m_car_idx": 2,\n'
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 11,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_lap_history_data": [\n    '
        f"{laps_history}\n"
        "  ],\n"
        '  "m_num_laps": 65,\n'
        '  "m_num_tyre_stints": 1,\n'
        '  "m_tyre_stints_history_data": [\n    '
        f"{tyre_stints_history}\n"
        "  ]\n"
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x0b\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + b"\x02\x41\x01\x0c\x0c\x0f\x0c"
        + lap_history_data__binary_representation() * 100
        + tyre_stint_history_data__binary_representation() * 8
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Lap time in milliseconds
        ("m_lap_time_in_ms", ctypes.c_uint32),
        # Sector 1 time in milliseconds
        ("m_sector1_time_in_ms", ctypes.c_uint16),
        # Sector 2 time in milliseconds
        ("m_sector2_time_in_ms", ctypes.c_uint16),
        # Sector 3 time in milliseconds
        ("m_sector3_time_in_ms", ctypes.c_uint16),
        # 0x01 bit set-lap valid,      0x02 bit set-sector 1 valid
        # 0x04 bit set-sector 2 valid, 0x08 bit set-sector 3 valid
        ("m_lap_valid_bit_flags", ctypes.c_uint8),
    ],
)
def test_lap_history_data__field__types(type_name, type_class):
    packet_type = LapHistoryData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Lap the tyre usage ends on (255 of current tyre)
        ("m_end_lap", ctypes.c_uint8),
        # Actual tyres used by this driver
        ("m_tyre_actual_compound", ctypes.c_uint8),
        # Visual tyres used by this driver
        ("m_tyre_visual_compound", ctypes.c_uint8),
    ],
)
def test_tyre_stint_history_data__story_data(type_name, type_class):
    packet_type = TyreStintHistoryData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Index of the car this lap data relates to
        ("m_car_idx", ctypes.c_uint8),
        # Num laps in the data (including current partial lap)
        ("m_num_laps", ctypes.c_uint8),
        # Number of tyre stints in the data
        ("m_num_tyre_stints", ctypes.c_uint8),
        # Lap the best lap time was achieved on
        ("m_best_lap_time_lap_num", ctypes.c_uint8),
        # Lap the best Sector 1 time was achieved on
        ("m_best_sector1_lap_num", ctypes.c_uint8),
        # Lap the best Sector 2 time was achieved on
        ("m_best_sector2_lap_num", ctypes.c_uint8),
        # Lap the best Sector 3 time was achieved on
        ("m_best_sector3_lap_num", ctypes.c_uint8),
        # 100 laps of data max
        ("m_lap_history_data", LapHistoryData * 100),
        ("m_tyre_stints_history_data", TyreStintHistoryData * 8),
    ],
)
def test_packet_session_history_data__field__types(type_name, type_class):
    packet_type = PacketSessionHistoryData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_session_history_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_session_history_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_session_history_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_session_history_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_session_history_data__from_binary(binary_representation, dict_representation):
    packet = PacketSessionHistoryData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
