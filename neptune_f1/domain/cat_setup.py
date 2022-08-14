from dataclasses import dataclass


@dataclass
class CarSetupData:
    # Front wing aero
    front_wing: int

    # Rear wing aero
    rear_wing: int

    # Differential adjustment on throttle (percentage)
    on_throttle: int

    # Differential adjustment off throttle (percentage)
    off_throttle: int

    # Front camber angle (suspension geometry)
    front_camber: float

    # Rear camber angle (suspension geometry)
    rear_camber: float

    # Front toe angle (suspension geometry)
    front_toe: float

    # Rear toe angle (suspension geometry)
    rear_toe: float

    # Front suspension
    front_suspension: int

    # Rear suspension
    rear_suspension: int

    # Front anti-roll bar
    front_anti_roll_bar: int

    # Front anti-roll bar
    rear_anti_roll_bar: int

    # Front ride height
    front_suspension_height: int

    # Rear ride height
    rear_suspension_height: int

    # Brake pressure (percentage)
    brake_pressure: int

    # Brake bias (percentage)
    brake_bias: int

    # Rear left tyre pressure (PSI)
    rear_left_tyre_pressure: float

    # Rear right tyre pressure (PSI)
    rear_right_tyre_pressure: float

    # Front left tyre pressure (PSI)
    front_left_tyre_pressure: float

    # Front right tyre pressure (PSI)
    front_right_tyre_pressure: float

    # Ballast
    ballast: int

    # Fuel load
    fuel_load: float


@dataclass
class CarSetup:
    car_setups = list[CarSetupData]
