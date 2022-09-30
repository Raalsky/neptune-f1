import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_session_history_data import (
    LapHistoryData,
    PacketSessionHistoryData,
    TyreStintHistoryData,
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
        ("m_lap_valid_bit_flags", ctypes.c_uint8),
        # 0x04 bit set-sector 2 valid, 0x08 bit set-sector 3 valid
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