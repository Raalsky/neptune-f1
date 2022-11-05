import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


@pytest.fixture
def packet():
    return PacketHeader(
        m_packet_format=2021,
        m_game_major_version=1,
        m_game_minor_version=23,
        m_packet_version=25,
        m_packet_id=2,
        m_session_uid=2501,
        m_session_time=25.01,
        m_frame_identifier=123,
        m_player_car_index=6,
        m_secondary_player_car_index=255,
    )


@pytest.fixture
def dict_representation():
    return {
        "m_packet_format": 2021,
        "m_game_major_version": 1,
        "m_game_minor_version": 23,
        "m_packet_version": 25,
        "m_packet_id": 2,
        "m_session_uid": 2501,
        "m_session_time": 25.01,
        "m_frame_identifier": 123,
        "m_player_car_index": 6,
        "m_secondary_player_car_index": 255,
    }


@pytest.fixture
def json_representation():
    return """{
  "m_frame_identifier": 123,
  "m_game_major_version": 1,
  "m_game_minor_version": 23,
  "m_packet_format": 2021,
  "m_packet_id": 2,
  "m_packet_version": 25,
  "m_player_car_index": 6,
  "m_secondary_player_car_index": 255,
  "m_session_time": 25.01,
  "m_session_uid": 2501
}"""


@pytest.fixture
def binary_representation():
    return b"\xe5\x07\x01\x17\x19\x02\xc5\x09\x00\x00\x00\x00\x00" b"\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"


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


def test_packet_header__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_header__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_header__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_header__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_header__from_binary(binary_representation, dict_representation):
    packet = PacketHeader.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
