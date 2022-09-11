from dataclasses import dataclass


@dataclass
class MarshalZone:
    # Fraction (0..1) of way through the lap the marshal zone starts
    zone_start: float

    # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    zone_flag: int


@dataclass
class WeatherForecastSample:
    # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1
    # 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2
    # 12 = Time Trial
    session_type: int

    # Time in minutes the forecast is for
    time_offset: int

    # Weather - 0 = clear, 1 = light cloud, 2 = overcast
    # 3 = light rain, 4 = heavy rain, 5 = storm
    weather: int

    # Track temp. in degrees Celsius
    track_temperature: int

    # Track temp. change – 0 = up, 1 = down, 2 = no change
    track_temperature_change: int

    # Air temp. in degrees celsius
    air_temperature: int

    # Air temp. change – 0 = up, 1 = down, 2 = no change
    air_temperature_change: int

    # Rain percentage (0-100)
    rain_percentage: int


@dataclass
class SessionData:
    # Weather - 0 = clear, 1 = light cloud, 2 = overcast
    # 3 = light rain, 4 = heavy rain, 5 = storm
    weather: int

    # Track temp. in degrees celsius
    track_temperature: int

    # Air temp. in degrees celsius
    air_temperature: int

    # Total number of laps in this race
    total_laps: int

    # Track length in metres
    track_length: int

    # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
    # 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
    # 10 = R, 11 = R2, 12 = R3, 13 = Time Trial
    session_type: int

    # -1 for unknown, 0-21 for tracks, see appendix
    track_id: int

    # Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2,
    # 3 = F1 Generic
    formula: int

    # Time left in session in seconds
    session_time_left: int

    # Session duration in seconds
    session_duration: int

    # Pit speed limit in kilometres per hour
    pit_speed_limit: int

    # Whether the game is paused
    game_paused: bool

    # Whether the player is spectating
    is_spectating: bool

    # Index of the car being spectated
    spectator_car_index: int

    # SLI Pro support, 0 = inactive, 1 = active
    sli_pro_native_support: bool

    # Number of marshal zones to follow
    num_marshal_zones: int

    # List of marshal zones – max 21
    marshal_zones: list[MarshalZone]

    # 0 = no safety car, 1 = full
    # 2 = virtual, 3 = formation lap
    safety_car_status: int

    # 0 = offline, 1 = online
    network_game: bool

    # Number of weather samples to follow
    num_weather_forecast_samples: int

    # Array of weather forecast samples
    weather_forecast_samples: list[WeatherForecastSample]

    # 0 = Perfect, 1 = Approximate
    forecast_accuracy: bool

    # AI Difficulty rating – 0-110
    ai_difficulty: int

    # Identifier for season - persists across saves
    season_link_identifier: int

    # Identifier for weekend - persists across saves
    weekend_link_identifier: int

    # Identifier for session - persists across saves
    session_link_identifier: int

    # Ideal lap to pit on for current strategy (player)
    pit_stop_window_ideal_lap: int

    # Latest lap to pit on for current strategy (player)
    pit_stop_window_latest_lap: int

    # Predicted position to rejoin at (player)
    pit_stop_rejoin_position: int

    # 0 = off, 1 = on
    steering_assist: bool

    # 0 = off, 1 = low, 2 = medium, 3 = high
    braking_assist: int

    # 1 = manual, 2 = manual & suggested gear, 3 = auto
    gearbox_assist: int

    # 0 = off, 1 = on
    pit_assist: bool

    # 0 = off, 1 = on
    pit_release_assist: bool

    # 0 = off, 1 = on
    ersassist: bool

    # 0 = off, 1 = on
    drsassist: bool

    # 0 = off, 1 = corners only, 2 = full
    dynamic_racing_line: int

    # 0 = 2D, 1 = 3D
    dynamic_racing_line_type: int
