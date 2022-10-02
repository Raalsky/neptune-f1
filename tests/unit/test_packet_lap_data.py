import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_lap_data import LapData, PacketLapData


def single():
    return LapData(
        m_last_lap_time_in_ms=83210,
        m_current_lap_time_in_ms=80925,
        m_sector1_time_in_ms=21481,
        m_sector2_time_in_ms=35023,
        m_lap_distance=4023.0,
        m_total_distance=39421.5,
        m_safety_car_delta=0.0,
        m_car_position=2,
        m_current_lap_num=18,
        m_pit_status=0,
        m_num_pit_stops=2,
        m_sector=2,
        m_current_lap_invalid=0,
        m_penalties=0,
        m_warnings=1,
        m_num_unserved_drive_through_pens=0,
        m_num_unserved_stop_go_pens=0,
        m_grid_position=5,
        m_driver_status=2,
        m_result_status=2,
        m_pit_lane_timer_active=0,
        m_pit_lane_time_in_lane_in_ms=0,
        m_pit_stop_timer_in_ms=0,
        m_pit_stop_should_serve_pen=0,
    )


def single__dict_representation():
    return {
        "m_last_lap_time_in_ms": 83210,
        "m_current_lap_time_in_ms": 80925,
        "m_sector1_time_in_ms": 21481,
        "m_sector2_time_in_ms": 35023,
        "m_lap_distance": 4023.0,
        "m_total_distance": 39421.5,
        "m_safety_car_delta": 0.0,
        "m_car_position": 2,
        "m_current_lap_num": 18,
        "m_pit_status": 0,
        "m_num_pit_stops": 2,
        "m_sector": 2,
        "m_current_lap_invalid": 0,
        "m_penalties": 0,
        "m_warnings": 1,
        "m_num_unserved_drive_through_pens": 0,
        "m_num_unserved_stop_go_pens": 0,
        "m_grid_position": 5,
        "m_driver_status": 2,
        "m_result_status": 2,
        "m_pit_lane_timer_active": 0,
        "m_pit_lane_time_in_lane_in_ms": 0,
        "m_pit_stop_timer_in_ms": 0,
        "m_pit_stop_should_serve_pen": 0,
    }


def single__json_representation():
    return """{
      "m_car_position": 2,
      "m_current_lap_invalid": 0,
      "m_current_lap_num": 18,
      "m_current_lap_time_in_ms": 80925,
      "m_driver_status": 2,
      "m_grid_position": 5,
      "m_lap_distance": 4023.0,
      "m_last_lap_time_in_ms": 83210,
      "m_num_pit_stops": 2,
      "m_num_unserved_drive_through_pens": 0,
      "m_num_unserved_stop_go_pens": 0,
      "m_penalties": 0,
      "m_pit_lane_time_in_lane_in_ms": 0,
      "m_pit_lane_timer_active": 0,
      "m_pit_status": 0,
      "m_pit_stop_should_serve_pen": 0,
      "m_pit_stop_timer_in_ms": 0,
      "m_result_status": 2,
      "m_safety_car_delta": 0.0,
      "m_sector": 2,
      "m_sector1_time_in_ms": 21481,
      "m_sector2_time_in_ms": 35023,
      "m_total_distance": 39421.5,
      "m_warnings": 1
    }"""


def single__binary_representation():
    return (
        b"\x0a\x45\x01\x00\x1d\x3c\x01\x00\xe9\x53\xcf\x88\x00\x70\x7b\x45\x80\xfd\x19\x47\x00\x00\x00\x00\x02\x12\x00"
        b"\x02\x02\x00\x00\x01\x00\x00\x05\x02\x02\x00\x00\x00\x00\x00\x00"
    )


@pytest.fixture
def packet():
    return PacketLapData(
        m_header=PacketHeader(
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
        ),
        m_lap_data=(LapData * 22)(*[single() for _ in range(22)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
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
        },
        "m_lap_data": [single__dict_representation() for _ in range(22)],
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
        '    "m_packet_id": 2,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_lap_data": [\n    '
        f"{entries}\n"
        "  ]\n"
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x02\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + single__binary_representation() * 22
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Last lap time in milliseconds
        ("m_last_lap_time_in_ms", ctypes.c_uint32),
        # Current time around the lap in milliseconds
        ("m_current_lap_time_in_ms", ctypes.c_uint32),
        # Sector 1 time in milliseconds
        ("m_sector1_time_in_ms", ctypes.c_uint16),
        # Sector 2 time in milliseconds
        ("m_sector2_time_in_ms", ctypes.c_uint16),
        # Distance vehicle is around current lap in metres – could
        # be negative if line hasn’t been crossed yet
        ("m_lap_distance", ctypes.c_float),
        # Total distance travelled in session in metres – could
        # be negative if line hasn’t been crossed yet
        ("m_total_distance", ctypes.c_float),
        # Delta in seconds for safety car
        ("m_safety_car_delta", ctypes.c_float),
        # Car race position
        ("m_car_position", ctypes.c_uint8),
        # Current lap number
        ("m_current_lap_num", ctypes.c_uint8),
        # 0 = none, 1 = pitting, 2 = in pit area
        ("m_pit_status", ctypes.c_uint8),
        # Number of pit stops taken in this race
        ("m_num_pit_stops", ctypes.c_uint8),
        # 0 = sector1, 1 = sector2, 2 = sector3
        ("m_sector", ctypes.c_uint8),
        # Current lap invalid - 0 = valid, 1 = invalid
        ("m_current_lap_invalid", ctypes.c_uint8),
        # Accumulated time penalties in seconds to be added
        ("m_penalties", ctypes.c_uint8),
        # Accumulated number of warnings issued
        ("m_warnings", ctypes.c_uint8),
        # Num drive through pens left to serve
        ("m_num_unserved_drive_through_pens", ctypes.c_uint8),
        # Num stop go pens left to serve
        ("m_num_unserved_stop_go_pens", ctypes.c_uint8),
        # Grid position the vehicle started the race in
        ("m_grid_position", ctypes.c_uint8),
        # Status of driver - 0 = in garage, 1 = flying lap
        # 2 = in lap, 3 = out lap, 4 = on track
        ("m_driver_status", ctypes.c_uint8),
        # Result status - 0 = invalid, 1 = inactive, 2 = active
        # 3 = finished, 4 = didnotfinish, 5 = disqualified
        # 6 = not classified, 7 = retired
        ("m_result_status", ctypes.c_uint8),
        # Pit lane timing, 0 = inactive, 1 = active
        ("m_pit_lane_timer_active", ctypes.c_uint8),
        # If active, the current time spent in the pit lane in ms
        ("m_pit_lane_time_in_lane_in_ms", ctypes.c_uint16),
        # Time of the actual pit stop in ms
        ("m_pit_stop_timer_in_ms", ctypes.c_uint16),
        # Whether the car should serve a penalty at this stop
        ("m_pit_stop_should_serve_pen", ctypes.c_uint8),
    ],
)
def test_lap_data__field__types(type_name, type_class):
    packet_type = LapData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Lap data for all cars on track
        ("m_lap_data", LapData * 22),
    ],
)
def test_packet_lap_data__field__types(type_name, type_class):
    packet_type = PacketLapData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_car_lap_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_car_lap_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_car_lap_data__to_json(packet, json_representation):
    print(packet.to_json())
    assert packet.to_json() == json_representation


def test_packet_car_lap_data__to_binary(packet, binary_representation):
    print("".join(f"\\x{x:02x}" for x in packet.pack()))
    assert packet.pack() == binary_representation


def test_packet_car_lap_data__from_binary(binary_representation, dict_representation):
    packet = PacketLapData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
