import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_participant_data import PacketParticipantsData, ParticipantData


def single():
    return ParticipantData(
        m_ai_controlled=1,
        m_driver_id=255,
        m_network_id=13,
        m_team_id=2,
        m_my_team=0,
        m_race_number=31,
        m_nationality=22,
        m_name=b"Test" + b"\x00" * 44,
        m_your_telemetry=1,
    )


def single__dict_representation():
    return {
        "m_ai_controlled": 1,
        "m_driver_id": 255,
        "m_network_id": 13,
        "m_team_id": 2,
        "m_my_team": 0,
        "m_race_number": 31,
        "m_nationality": 22,
        "m_name": "Test",
        "m_your_telemetry": 1,
    }


def single__json_representation():
    return """{
      "m_ai_controlled": 1,
      "m_driver_id": 255,
      "m_my_team": 0,
      "m_name": "Test",
      "m_nationality": 22,
      "m_network_id": 13,
      "m_race_number": 31,
      "m_team_id": 2,
      "m_your_telemetry": 1
    }"""


def single__binary_representation():
    return (
        b"\x01\xff\x0d\x02\x00\x1f\x16\x54\x65\x73\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x01"
    )


@pytest.fixture
def packet():
    return PacketParticipantsData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=4,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_num_active_cars=20,
        m_participants=(ParticipantData * 22)(*[single() for _ in range(22)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 4,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_num_active_cars": 20,
        "m_participants": [single__dict_representation() for _ in range(22)],
    }


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 4,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_num_active_cars": 20,\n'
        '  "m_participants": [\n    '
        f"{entries}\n"
        "  ]\n"
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x04\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff\x14"
        + single__binary_representation() * 22
    )


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


def test_packet_participants_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_participants_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_participants_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_participants_data__to_binary(packet, binary_representation):
    print("".join(f"\\x{x:02x}" for x in packet.pack()))
    assert packet.pack() == binary_representation


def test_packet_participants_data__from_binary(binary_representation, dict_representation):
    packet = PacketParticipantsData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
