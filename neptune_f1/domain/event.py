from dataclasses import dataclass


@dataclass
class FastestLap:
    # Vehicle index of car achieving fastest lap
    vehicle_idx: int

    # Lap time is in seconds
    lap_time: float


@dataclass
class Retirement:
    # Vehicle index of car retiring
    vehicle_idx: int


@dataclass
class TeamMateInPits:
    # Vehicle index of team mate
    vehicle_idx: int


@dataclass
class RaceWinner:
    # Vehicle index of the race winner
    vehicle_idx: int


@dataclass
class Penalty:
    # Penalty type – see Appendices
    penalty_type: int

    # Infringement type – see Appendices
    infringement_type: int

    # Vehicle index of the car the penalty is applied to
    vehicle_idx: int

    # Vehicle index of the other car involved
    other_vehicle_idx: int

    # Time gained, or time spent doing action in seconds
    time: int

    # Lap the penalty occurred on
    lap_num: int

    # Number of places gained by this
    places_gained: int


@dataclass
class SpeedTrap:
    # Vehicle index of the vehicle triggering speed trap
    vehicle_idx: int

    # Top speed achieved in kilometres per hour
    speed: int

    # Overall fastest speed in session = 1, otherwise 0
    overall_fastest_in_session: bool

    # Fastest speed for driver in session = 1, otherwise 0
    driver_fastest_in_session: bool


@dataclass
class StartLights:
    # Number of lights showing
    num_lights: int


@dataclass
class DriveThroughPenaltyServed:
    # Vehicle index of the vehicle serving drive through
    vehicle_idx: int


@dataclass
class StopGoPenaltyServed:
    # Vehicle index of the vehicle serving stop go
    vehicle_idx: int


@dataclass
class Flashback:
    # Frame identifier flashed back to
    flashback_frame_identifier: int

    # Session time flashed back to
    flashback_session_time: float


@dataclass
class ButtonPressed:
    # List which buttons are being pressed
    # currently - see appendices
    button_status: list[int]
