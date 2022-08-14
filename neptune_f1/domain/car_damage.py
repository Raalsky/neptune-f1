from dataclasses import dataclass


@dataclass
class CarDamageData:
    # Tyre wear (percentage)
    tyres_wear: list[float]

    # Tyre damage (percentage)
    tyres_damage: list[int]

    # Brakes damage (percentage)
    brakes_damage: list[int]

    # Front left wing damage (percentage)
    front_left_wing_damage: int

    # Front right wing damage (percentage)
    front_right_wing_damage: int

    # Rear wing damage (percentage)
    rear_wing_damage: int

    # Floor damage (percentage)
    floor_damage: int

    # Diffuser damage (percentage)
    diffuser_damage: int

    # Sidepod damage (percentage)
    sidepod_damage: int

    # Indicator for DRS fault, 0 = OK, 1 = fault
    drs_fault: bool

    # Gear box damage (percentage)
    gear_box_damage: int

    # Engine damage (percentage)
    engine_damage: int

    # Engine wear MGU-H (percentage)
    engine_mguhwear: int

    # Engine wear ES (percentage)
    engine_eswear: int

    # Engine wear CE (percentage)
    engine_cewear: int

    # Engine wear ICE (percentage)
    engine_icewear: int

    # Engine wear MGU-K (percentage)
    engine_mgukwear: int

    # Engine wear TC (percentage)
    engine_tcwear: int


@dataclass
class CarDamage:
    car_damages: list[CarDamageData]
