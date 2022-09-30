import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # 2021
        ("m_packet_format", ctypes.c_uint16),
        # Game major version - "X.00"
        ("m_game_major_version", ctypes.c_uint8),
        # Game minor version - "1.XX"
        ("m_game_minor_version", ctypes.c_uint8),
        # Version of this packet type, all start from 1
        ("m_packet_version", ctypes.c_uint8),
        # Identifier for the packet type, see below
        ("m_packet_id", ctypes.c_uint8),
        # Unique identifier for the session
        ("m_session_uid", ctypes.c_uint64),
        # Session timestamp
        ("m_session_time", ctypes.c_float),
        # Identifier for the frame the data was retrieved on
        ("m_frame_identifier", ctypes.c_uint32),
        # Index of player's car in the array
        ("m_player_car_index", ctypes.c_uint8),
        # Index of secondary player's car in the array (splitscreen)
        # 255 if no second player
        ("m_secondary_player_car_index", ctypes.c_uint8),
    ],
)
def test_packet_header__field__types(type_name, type_class):
    packet_type = PacketHeader()

    assert (type_name, type_class) in packet_type._fields_