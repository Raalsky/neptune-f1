import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class MarshalZone(Packet):
    _fields_ = [
        # Fraction (0..1) of way through the lap the marshal zone starts
        ("m_zone_start", ctypes.c_float),
        # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        ("m_zone_flag", ctypes.c_int8),
    ]


class WeatherForecastSample(Packet):
    _fields_ = [
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
    ]


class PacketSessionData(Packet):
    _id_ = 1
    _fields_ = [
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
    ]
