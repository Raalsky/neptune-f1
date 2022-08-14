from dataclasses import dataclass


@dataclass
class FinalClassificationData:
    # Finishing position
    position: int

    # Number of laps completed
    num_laps: int

    # Grid position of the car
    grid_position: int

    # Number of points scored
    points: int

    # Number of pit stops made
    num_pit_stops: int

    # Result status - 0 = invalid, 1 = inactive, 2 = active
    # 3 = finished, 4 = didnotfinish, 5 = disqualified
    # 6 = not classified, 7 = retired
    result_status: int

    # Best lap time of the session in milliseconds
    best_lap_time_in_ms: int

    # Total race time in seconds without penalties
    total_race_time: int

    # Total penalties accumulated in seconds
    penalties_time: int

    # Number of penalties applied to this driver
    num_penalties: int

    # Number of tyres stints up to maximum
    num_tyre_stints: int

    # Actual tyres used by this driver
    tyre_stints_actual: list[int]

    # Visual tyres used by this driver
    tyre_stints_visual: list[int]


@dataclass
class FinalClassification:
    classification: list[FinalClassificationData]
