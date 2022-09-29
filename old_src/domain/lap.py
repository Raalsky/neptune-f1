from dataclasses import dataclass


@dataclass
class Lap:
    # Last lap time in milliseconds
    last_lap_time_in_ms: int

    # Current time around the lap in milliseconds
    current_lap_time_in_ms: int

    # Sector 1 time in milliseconds
    sector1_time_in_ms: int

    # Sector 2 time in milliseconds
    sector2_time_in_ms: int

    # Distance vehicle is around current lap in metres – could
    # be negative if line hasn’t been crossed yet
    lap_distance: float

    # Total distance travelled in session in metres – could
    # be negative if line hasn’t been crossed yet
    total_distance: float

    # Delta in seconds for safety car
    safety_car_delta: float

    # Car race position
    car_position: int

    # Current lap number
    current_lap_num: int

    # 0 = none, 1 = pitting, 2 = in pit area
    pit_status: int

    # Number of pit stops taken in this race
    num_pit_stops: int

    # 0 = sector1, 1 = sector2, 2 = sector3
    sector: int

    # Current lap invalid - 0 = valid, 1 = invalid
    current_lap_invalid: int

    # Accumulated time penalties in seconds to be added
    penalties: int

    # Accumulated number of warnings issued
    warnings: int

    # Num drive through pens left to serve
    num_unserved_drive_through_pens: int

    # Num stop go pens left to serve
    num_unserved_stop_go_pens: int

    # Grid position the vehicle started the race in
    grid_position: int

    # Status of driver - 0 = in garage, 1 = flying lap
    # 2 = in lap, 3 = out lap, 4 = on track
    driver_status: int

    # Result status - 0 = invalid, 1 = inactive, 2 = active
    # 3 = finished, 4 = didnotfinish, 5 = disqualified
    # 6 = not classified, 7 = retired
    result_status: int

    # Pit lane timing, 0 = inactive, 1 = active
    pit_lane_timer_active: int

    # If active, the current time spent in the pit lane in ms
    pit_lane_time_in_lane_in_ms: int

    # Time of the actual pit stop in ms
    pit_stop_timer_in_ms: int

    # Whether the car should serve a penalty at this stop
    pit_stop_should_serve_pen: int


@dataclass
class Laps:
    laps: list[Lap]
