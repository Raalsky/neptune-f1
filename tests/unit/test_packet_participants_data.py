import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_participant_data import PacketParticipantsData, ParticipantData


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Whether the vehicle is AI (1) or Human (0) controlled
        ("m_ai_controlled", ctypes.c_uint8),
        # Driver id - see appendix, 255 if network human
        ("m_driver_id", ctypes.c_uint8),
        # Network id – unique identifier for network players
        ("m_network_id", ctypes.c_uint8),
        # Team id - see appendix
        ("m_team_id", ctypes.c_uint8),
        # My team flag – 1 = My Team, 0 = otherwise
        ("m_my_team", ctypes.c_uint8),
        # Race number of the car
        ("m_race_number", ctypes.c_uint8),
        # Nationality of the driver
        ("m_nationality", ctypes.c_uint8),
        # Name of participant in UTF-8 format – null terminated
        # Will be truncated with … (U+2026) if too long
        ("m_name", ctypes.c_char * 48),
        # The player's UDP setting, 0 = restricted, 1 = public
        ("m_your_telemetry", ctypes.c_uint8),
    ],
)
def test_participant_data__field__types(type_name, type_class):
    packet_type = ParticipantData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Number of active cars in the data – should match number of
        # cars on HUD
        ("m_num_active_cars", ctypes.c_uint8),
        ("m_participants", ParticipantData * 22),
    ],
)
def test_packet_participants_data__field__types(type_name, type_class):
    packet_type = PacketParticipantsData()

    assert (type_name, type_class) in packet_type._fields_
