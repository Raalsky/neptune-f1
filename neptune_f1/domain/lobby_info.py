from dataclasses import dataclass


@dataclass
class Info:
    # Whether the vehicle is AI (1) or Human (0) controlled
    ai_controlled: bool

    # Team id - see appendix (255 if no team currently selected)
    team_id: int

    # Nationality of the driver
    nationality: int

    # Name of participant in UTF-8 format – null terminated
    # Will be truncated with ... (U+2026) if too long
    name: str

    # Car number of the player
    car_number: int

    # 0 = not ready, 1 = ready, 2 = spectating
    ready_status: int


@dataclass
class LobbyInfo:
    lobby_players: list[Info]
