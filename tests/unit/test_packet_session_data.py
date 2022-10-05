import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_session_data import (
    MarshalZone,
    PacketSessionData,
    WeatherForecastSample,
)


def marshal_zone():
    return MarshalZone(m_zone_start=0.0, m_zone_flag=0)


def marshal_zone__dict_representation():
    return {"m_zone_start": 0.0, "m_zone_flag": 0}


def marshal_zone__json_representation():
    return """{
      "m_zone_flag": 0,
      "m_zone_start": 0.0
    }"""


def marshal_zone__binary_representation():
    return b"\x00\x00\x00\x00\x00"


def weather_forecast_sample():
    return WeatherForecastSample(
        m_session_type=1,
        m_time_offset=5,
        m_weather=0,
        m_track_temperature=18,
        m_track_temperature_change=1,
        m_air_temperature=10,
        m_air_temperature_change=2,
        m_rain_percentage=12,
    )


def weather_forecast_sample__dict_representation():
    return {
        "m_session_type": 1,
        "m_time_offset": 5,
        "m_weather": 0,
        "m_track_temperature": 18,
        "m_track_temperature_change": 1,
        "m_air_temperature": 10,
        "m_air_temperature_change": 2,
        "m_rain_percentage": 12,
    }


def weather_forecast_sample__json_representation():
    return """{
      "m_air_temperature": 10,
      "m_air_temperature_change": 2,
      "m_rain_percentage": 12,
      "m_session_type": 1,
      "m_time_offset": 5,
      "m_track_temperature": 18,
      "m_track_temperature_change": 1,
      "m_weather": 0
    }"""


def weather_forecast_sample__binary_representation():
    return b"\x01\x05\x00\x12\x01\x0a\x02\x0c"


@pytest.fixture
def packet():
    return PacketSessionData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=1,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_weather=0,
        m_track_temperature=34,
        m_air_temperature=28,
        m_total_laps=65,
        m_track_length=4321,
        m_session_type=10,
        m_track_id=2,
        m_formula=0,
        m_session_time_left=256,
        m_session_duration=2543,
        m_pit_speed_limit=60,
        m_game_paused=0,
        m_is_spectating=0,
        m_spectator_car_index=0,
        m_sli_pro_native_support=0,
        m_num_marshal_zones=2,
        m_marshal_zones=(MarshalZone * 21)(*[marshal_zone() for _ in range(21)]),
        m_safety_car_status=0,
        m_network_game=0,
        m_num_weather_forecast_samples=12,
        m_weather_forecast_samples=(WeatherForecastSample * 56)(*[weather_forecast_sample() for _ in range(56)]),
        m_forecast_accuracy=0,
        m_ai_difficulty=70,
        m_season_link_identifier=5432,
        m_weekend_link_identifier=432,
        m_session_link_identifier=431,
        m_pit_stop_window_ideal_lap=12,
        m_pit_stop_window_latest_lap=12,
        m_pit_stop_rejoin_position=2,
        m_steering_assist=0,
        m_braking_assist=0,
        m_gearbox_assist=3,
        m_pit_assist=1,
        m_pit_release_assist=1,
        m_ersassist=1,
        m_drsassist=1,
        m_dynamic_racing_line=1,
        m_dynamic_racing_line_type=1,
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 1,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_weather": 0,
        "m_track_temperature": 34,
        "m_air_temperature": 28,
        "m_total_laps": 65,
        "m_track_length": 4321,
        "m_session_type": 10,
        "m_track_id": 2,
        "m_formula": 0,
        "m_session_time_left": 256,
        "m_session_duration": 2543,
        "m_pit_speed_limit": 60,
        "m_game_paused": 0,
        "m_is_spectating": 0,
        "m_spectator_car_index": 0,
        "m_sli_pro_native_support": 0,
        "m_num_marshal_zones": 2,
        "m_marshal_zones": [marshal_zone__dict_representation() for _ in range(21)],
        "m_safety_car_status": 0,
        "m_network_game": 0,
        "m_num_weather_forecast_samples": 12,
        "m_weather_forecast_samples": [weather_forecast_sample__dict_representation() for _ in range(56)],
        "m_forecast_accuracy": 0,
        "m_ai_difficulty": 70,
        "m_season_link_identifier": 5432,
        "m_weekend_link_identifier": 432,
        "m_session_link_identifier": 431,
        "m_pit_stop_window_ideal_lap": 12,
        "m_pit_stop_window_latest_lap": 12,
        "m_pit_stop_rejoin_position": 2,
        "m_steering_assist": 0,
        "m_braking_assist": 0,
        "m_gearbox_assist": 3,
        "m_pit_assist": 1,
        "m_pit_release_assist": 1,
        "m_ersassist": 1,
        "m_drsassist": 1,
        "m_dynamic_racing_line": 1,
        "m_dynamic_racing_line_type": 1,
    }


@pytest.fixture
def json_representation():
    marshal_zones = ",\n    ".join(marshal_zone__json_representation() for _ in range(21))
    weather_forecast_samples = ",\n    ".join(weather_forecast_sample__json_representation() for _ in range(56))

    return (
        "{\n"
        '  "m_ai_difficulty": 70,\n'
        '  "m_air_temperature": 28,\n'
        '  "m_braking_assist": 0,\n'
        '  "m_drsassist": 1,\n'
        '  "m_dynamic_racing_line": 1,\n'
        '  "m_dynamic_racing_line_type": 1,\n'
        '  "m_ersassist": 1,\n'
        '  "m_forecast_accuracy": 0,\n'
        '  "m_formula": 0,\n'
        '  "m_game_paused": 0,\n'
        '  "m_gearbox_assist": 3,\n'
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 1,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  },\n"
        '  "m_is_spectating": 0,\n'
        '  "m_marshal_zones": [\n    '
        f"{marshal_zones}\n"
        "  ],\n"
        '  "m_network_game": 0,\n'
        '  "m_num_marshal_zones": 2,\n'
        '  "m_num_weather_forecast_samples": 12,\n'
        '  "m_pit_assist": 1,\n'
        '  "m_pit_release_assist": 1,\n'
        '  "m_pit_speed_limit": 60,\n'
        '  "m_pit_stop_rejoin_position": 2,\n'
        '  "m_pit_stop_window_ideal_lap": 12,\n'
        '  "m_pit_stop_window_latest_lap": 12,\n'
        '  "m_safety_car_status": 0,\n'
        '  "m_season_link_identifier": 5432,\n'
        '  "m_session_duration": 2543,\n'
        '  "m_session_link_identifier": 431,\n'
        '  "m_session_time_left": 256,\n'
        '  "m_session_type": 10,\n'
        '  "m_sli_pro_native_support": 0,\n'
        '  "m_spectator_car_index": 0,\n'
        '  "m_steering_assist": 0,\n'
        '  "m_total_laps": 65,\n'
        '  "m_track_id": 2,\n'
        '  "m_track_length": 4321,\n'
        '  "m_track_temperature": 34,\n'
        '  "m_weather": 0,\n'
        '  "m_weather_forecast_samples": [\n    '
        f"{weather_forecast_samples}\n"
        "  ],\n"
        '  "m_weekend_link_identifier": 432\n'
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x01\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + b"\x00\x22\x1c\x41\xe1\x10\x0a\x02\x00\x00\x01\xef\x09\x3c\x00\x00\x00\x00\x02"
        + marshal_zone__binary_representation() * 21
        + b"\x00\x00\x0c"
        + weather_forecast_sample__binary_representation() * 56
        + b"\x00\x46\x38\x15\x00\x00\xb0\x01\x00\x00\xaf\x01\x00\x00\x0c\x0c\x02\x00\x00\x03\x01\x01\x01\x01\x01\x01"
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Fraction (0..1) of way through the lap the marshal zone starts
        ("m_zone_start", ctypes.c_float),
        # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        ("m_zone_flag", ctypes.c_int8),
    ],
)
def test_marshal_zone__field__types(type_name, type_class):
    packet_type = MarshalZone()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1
        # 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2
        # 12 = Time Trial
        ("m_session_type", ctypes.c_uint8),
        # Time in minutes the forecast is for
        ("m_time_offset", ctypes.c_uint8),
        # Weather - 0 = clear, 1 = light cloud, 2 = overcast
        # 3 = light rain, 4 = heavy rain, 5 = storm
        ("m_weather", ctypes.c_uint8),
        # Track temp. in degrees Celsius
        ("m_track_temperature", ctypes.c_int8),
        # Track temp. change – 0 = up, 1 = down, 2 = no change
        ("m_track_temperature_change", ctypes.c_int8),
        # Air temp. in degrees celsius
        ("m_air_temperature", ctypes.c_int8),
        # Air temp. change – 0 = up, 1 = down, 2 = no change
        ("m_air_temperature_change", ctypes.c_int8),
        # Rain percentage (0-100)
        ("m_rain_percentage", ctypes.c_uint8),
    ],
)
def test_weather_forecast_sample__field__types(type_name, type_class):
    packet_type = WeatherForecastSample()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Weather - 0 = clear, 1 = light cloud, 2 = overcast
        # 3 = light rain, 4 = heavy rain, 5 = storm
        ("m_weather", ctypes.c_uint8),
        # Track temp. in degrees celsius
        ("m_track_temperature", ctypes.c_int8),
        # Air temp. in degrees celsius
        ("m_air_temperature", ctypes.c_int8),
        # Total number of laps in this race
        ("m_total_laps", ctypes.c_uint8),
        # Track length in metres
        ("m_track_length", ctypes.c_uint16),
        # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
        # 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
        # 10 = R, 11 = R2, 12 = R3, 13 = Time Trial
        ("m_session_type", ctypes.c_uint8),
        # -1 for unknown, 0-21 for tracks, see appendix
        ("m_track_id", ctypes.c_int8),
        # Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2,
        # 3 = F1 Generic
        ("m_formula", ctypes.c_uint8),
        # Time left in session in seconds
        ("m_session_time_left", ctypes.c_uint16),
        # Session duration in seconds
        ("m_session_duration", ctypes.c_uint16),
        # Pit speed limit in kilometres per hour
        ("m_pit_speed_limit", ctypes.c_uint8),
        # Whether the game is paused
        ("m_game_paused", ctypes.c_uint8),
        # Whether the player is spectating
        ("m_is_spectating", ctypes.c_uint8),
        # Index of the car being spectated
        ("m_spectator_car_index", ctypes.c_uint8),
        # SLI Pro support, 0 = inactive, 1 = active
        ("m_sli_pro_native_support", ctypes.c_uint8),
        # Number of marshal zones to follow
        ("m_num_marshal_zones", ctypes.c_uint8),
        # List of marshal zones – max 21
        ("m_marshal_zones", MarshalZone * 21),
        # 0 = no safety car, 1 = full
        # 2 = virtual, 3 = formation lap
        ("m_safety_car_status", ctypes.c_uint8),
        # 0 = offline, 1 = online
        ("m_network_game", ctypes.c_uint8),
        # Number of weather samples to follow
        ("m_num_weather_forecast_samples", ctypes.c_uint8),
        # Array of weather forecast samples
        ("m_weather_forecast_samples", WeatherForecastSample * 56),
        # 0 = Perfect, 1 = Approximate
        ("m_forecast_accuracy", ctypes.c_uint8),
        # AI Difficulty rating – 0-110
        ("m_ai_difficulty", ctypes.c_uint8),
        # Identifier for season - persists across saves
        ("m_season_link_identifier", ctypes.c_uint32),
        # Identifier for weekend - persists across saves
        ("m_weekend_link_identifier", ctypes.c_uint32),
        # Identifier for session - persists across saves
        ("m_session_link_identifier", ctypes.c_uint32),
        # Ideal lap to pit on for current strategy (player)
        ("m_pit_stop_window_ideal_lap", ctypes.c_uint8),
        # Latest lap to pit on for current strategy (player)
        ("m_pit_stop_window_latest_lap", ctypes.c_uint8),
        # Predicted position to rejoin at (player)
        ("m_pit_stop_rejoin_position", ctypes.c_uint8),
        # 0 = off, 1 = on
        ("m_steering_assist", ctypes.c_uint8),
        # 0 = off, 1 = low, 2 = medium, 3 = high
        ("m_braking_assist", ctypes.c_uint8),
        # 1 = manual, 2 = manual & suggested gear, 3 = auto
        ("m_gearbox_assist", ctypes.c_uint8),
        # 0 = off, 1 = on
        ("m_pit_assist", ctypes.c_uint8),
        # 0 = off, 1 = on
        ("m_pit_release_assist", ctypes.c_uint8),
        # 0 = off, 1 = on
        ("m_ersassist", ctypes.c_uint8),
        # 0 = off, 1 = on
        ("m_drsassist", ctypes.c_uint8),
        # 0 = off, 1 = corners only, 2 = full
        ("m_dynamic_racing_line", ctypes.c_uint8),
        # 0 = 2D, 1 = 3D
        ("m_dynamic_racing_line_type", ctypes.c_uint8),
    ],
)
def test_packet_session_data__field__types(type_name, type_class):
    packet_type = PacketSessionData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_packet_session_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_packet_session_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_packet_session_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_packet_session_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_packet_session_data__from_binary(binary_representation, dict_representation):
    packet = PacketSessionData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
