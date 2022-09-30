import ctypes

from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.utils import Packet

__all__ = ["PacketLobbyInfoData"]


class LobbyInfoData(Packet):
    _fields_ = [
        # Whether the vehicle is AI (1) or Human (0) controlled
        ("m_ai_controlled", ctypes.c_uint8),
        # Team id - see appendix (255 if no team currently selected)
        ("m_team_id", ctypes.c_uint8),
        # Nationality of the driver
        ("m_nationality", ctypes.c_uint8),
        # Name of participant in UTF-8 format – null terminated Will be truncated with ... (U+2026) if too long
        ("m_name", ctypes.c_char * 48),
        # Car number of the player
        ("m_car_number", ctypes.c_uint8),
        # 0 = not ready, 1 = ready, 2 = spectating
        ("m_ready_status", ctypes.c_uint8),
    ]


class PacketLobbyInfoData(Packet):
    _id_ = 9
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Number of players in the lobby data
        ("m_num_players", ctypes.c_uint8),
        ("m_lobby_players", LobbyInfoData * 22),
    ]
