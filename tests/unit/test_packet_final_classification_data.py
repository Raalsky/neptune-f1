import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_final_classification_data import (
    FinalClassificationData,
    PacketFinalClassificationData,
)
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


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
