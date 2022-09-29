from dataclasses import dataclass


@dataclass
class CarStatus:
    # Traction control - 0 = off, 1 = medium, 2 = full
    traction_control: int

    # 0 (off) - 1 (on)
    anti_lock_brakes: int

    # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
    fuel_mix: int

    # Front brake bias (percentage)
    front_brake_bias: int

    # Pit limiter status - 0 = off, 1 = on
    pit_limiter_status: int

    # Current fuel mass
    fuel_in_tank: float

    # Fuel capacity
    fuel_capacity: float

    # Fuel remaining in terms of laps (value on MFD)
    fuel_remaining_laps: float

    # Cars max RPM, point of rev limiter
    max_rpm: int

    # Cars idle RPM
    idle_rpm: int

    # Maximum number of gears
    max_gears: int

    # 0 = not allowed, 1 = allowed
    drs_allowed: int

    # 0 = DRS not available, non-zero - DRS will be available
    # in [X] metres
    drs_activation_distance: int

    # F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1
    # 7 = inter, 8 = wet
    # F1 Classic - 9 = dry, 10 = wet
    # F2 – 11 = super soft, 12 = soft, 13 = medium, 14 = hard
    # 15 = wet
    actual_tyre_compound: int

    # F1 visual (can be different from actual compound)
    # 16 = soft, 17 = medium, 18 = hard, 7 = inter, 8 = wet
    # F1 Classic – same as above
    # F2 ‘19, 15 = wet, 19 – super soft, 20 = soft
    # 21 = medium , 22 = hard
    visual_tyre_compound: int

    # Age in laps of the current set of tyres
    tyres_age_laps: int

    # -1 = invalid/unknown, 0 = none, 1 = green
    # 2 = blue, 3 = yellow, 4 = red
    vehicle_fia_flags: int

    # ERS energy store in Joules
    ers_store_energy: float

    # ERS deployment mode, 0 = none, 1 = medium
    # 2 = hotlap, 3 = overtake
    ers_deploy_mode: int

    # ERS energy harvested this lap by MGU-K
    ers_harvested_this_lap_mguk: float

    # ERS energy harvested this lap by MGU-H
    ers_harvested_this_lap_mguh: float

    # ERS energy deployed this lap
    ers_deployed_this_lap: float

    # Whether the car is paused in a network game
    network_paused: int


class CarsStatuses:
    cars_statuses: list[CarStatus]
