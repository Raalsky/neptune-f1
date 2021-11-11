from dataclasses import dataclass


@dataclass
class Common:
    # 2021
    packet_format: int

    # Game major version - "X.00"
    game_major_version: int

    # Game minor version - "1.XX"
    game_minor_version: int

    # Version of this packet type, all start from 1
    packet_version: int

    # Identifier for the packet type, see below
    packet_id: int

    # Unique identifier for the session
    session_uid: int

    # Session timestamp
    session_time: float

    # Identifier for the frame the data was retrieved on
    frame_identifier: int

    # Index of player's car in the array
    player_car_index: int

    # Index of secondary player's car in the array (splitscreen)
    # 255 if no second player
    secondary_player_car_index: int
