from dataclasses import dataclass


@dataclass
class CarMotion:
    # World space X position
    world_position_x: float

    # World space Y position
    world_position_y: float

    # World space Z position
    world_position_z: float

    # Velocity in world space X
    world_velocity_x: float

    # Velocity in world space Y
    world_velocity_y: float

    # Velocity in world space Z
    world_velocity_z: float

    # World space forward X direction (normalised)
    world_forward_dir_x: int

    # World space forward Y direction (normalised)
    world_forward_dir_y: int

    # World space forward Z direction (normalised)
    world_forward_dir_z: int

    # World space right X direction (normalised)
    world_right_dir_x: int

    # World space right Y direction (normalised)
    world_right_dir_y: int

    # World space right Z direction (normalised)
    world_right_dir_z: int

    # Lateral G-Force component
    g_force_lateral: float

    # Longitudinal G-Force component
    g_force_longitudinal: float

    # Vertical G-Force component
    g_force_vertical: float

    # Yaw angle in radians
    yaw: float

    # Pitch angle in radians
    pitch: float

    # Roll angle in radians
    roll: float


@dataclass
class CarsMotion:
    # Data for all cars on track
    # Extra player car ONLY data
    cars_motion: list[CarMotion]

    # Note: All wheel arrays have the following order:
    suspension_position: list[float]

    # RL, RR, FL, FR
    suspension_velocity: list[float]

    # RL, RR, FL, FR
    suspension_acceleration: list[float]

    # Speed of each wheel
    wheel_speed: list[float]

    # Slip ratio for each wheel
    wheel_slip: list[float]

    # Velocity in local space
    local_velocity_x: float

    # Velocity in local space
    local_velocity_y: float

    # Velocity in local space
    local_velocity_z: float

    # Angular velocity x-component
    angular_velocity_x: float

    # Angular velocity y-component
    angular_velocity_y: float

    # Angular velocity z-component
    angular_velocity_z: float

    # Angular velocity x-component
    angular_acceleration_x: float

    # Angular velocity y-component
    angular_acceleration_y: float

    # Angular velocity z-component
    angular_acceleration_z: float

    # Current front wheels angle in radians
    front_wheels_angle: float
