from dataclasses import dataclass


@dataclass
class CarTelemetry:
    # Speed of car in kilometres per hour
    speed: int

    # Amount of throttle applied (0.0 to 1.0)
    throttle: float

    # Steering (-1.0 (full lock left) to 1.0 (full lock right))
    steer: float

    # Amount of brake applied (0.0 to 1.0)
    brake: float

    # Amount of clutch applied (0 to 100)
    clutch: int

    # Gear selected (1-8, N=0, R=-1)
    gear: int

    # Engine RPM
    engine_rpm: int

    # 0 = off, 1 = on
    drs: bool

    # Rev lights indicator (percentage)
    rev_lights_percent: int

    # Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
    rev_lights_bit_value: int

    # Brakes temperature (celsius)
    brakes_temperature: list[int]

    # Tyres surface temperature (celsius)
    tyres_surface_temperature: list[int]

    # Tyres inner temperature (celsius)
    tyres_inner_temperature: list[int]

    # Engine temperature (celsius)
    engine_temperature: int

    # Tyres pressure (PSI)
    tyres_pressure: list[float]

    # Driving surface, see appendices
    surface_type: list[int]


@dataclass
class CarsTelemetry:
    cars_telemetry: list[CarTelemetry]
