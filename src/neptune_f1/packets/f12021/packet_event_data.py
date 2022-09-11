import ctypes

from .packet_header import PacketHeader
from .utils import Packet, PacketMixin


class FastestLap(Packet):
    _fields_ = [
        # Vehicle index of car achieving fastest lap
        ("vehicle_idx", ctypes.c_uint8),
        # Lap time is in seconds
        ("lap_time", ctypes.c_float),
    ]


class Retirement(Packet):
    _fields_ = [
        # Vehicle index of car retiring
        ("vehicle_idx", ctypes.c_uint8),
    ]


class TeamMateInPits(Packet):
    _fields_ = [
        # Vehicle index of team mate
        ("vehicle_idx", ctypes.c_uint8),
    ]


class RaceWinner(Packet):
    _fields_ = [
        # Vehicle index of the race winner
        ("vehicle_idx", ctypes.c_uint8),
    ]


class Penalty(Packet):
    _fields_ = [
        # Penalty type – see Appendices
        ("penalty_type", ctypes.c_uint8),
        # Infringement type – see Appendices
        ("infringement_type", ctypes.c_uint8),
        # Vehicle index of the car the penalty is applied to
        ("vehicle_idx", ctypes.c_uint8),
        # Vehicle index of the other car involved
        ("other_vehicle_idx", ctypes.c_uint8),
        # Time gained, or time spent doing action in seconds
        ("time", ctypes.c_uint8),
        # Lap the penalty occurred on
        ("lap_num", ctypes.c_uint8),
        # Number of places gained by this
        ("places_gained", ctypes.c_uint8),
    ]


class SpeedTrap(Packet):
    _fields_ = [
        # Vehicle index of the vehicle triggering speed trap
        ("vehicle_idx", ctypes.c_uint8),
        # Top speed achieved in kilometres per hour
        ("speed", ctypes.c_float),
        # Overall fastest speed in session = 1, otherwise 0
        ("overall_fastest_in_session", ctypes.c_uint8),
        # Fastest speed for driver in session = 1, otherwise 0
        ("driver_fastest_in_session", ctypes.c_uint8),
    ]


class StartLights(Packet):
    _fields_ = [
        # Number of lights showing
        ("num_lights", ctypes.c_uint8),
    ]


class DriveThroughPenaltyServed(Packet):
    _fields_ = [
        # Vehicle index of the vehicle serving drive through
        ("vehicle_idx", ctypes.c_uint8),
    ]


class StopGoPenaltyServed(Packet):
    _fields_ = [
        # Vehicle index of the vehicle serving stop go
        ("vehicle_idx", ctypes.c_uint8),
    ]


class Flashback(Packet):
    _fields_ = [
        # Frame identifier flashed back to
        ("flashback_frame_identifier", ctypes.c_uint32),
        # Session time flashed back to
        ("flashback_session_time", ctypes.c_float),
    ]


class Buttons(Packet):
    _fields_ = [
        # Bit flags specifying which buttons are being pressed
        # currently - see appendices
        ("m_button_status", ctypes.c_uint32),
    ]


class EventDataDetails(ctypes.Union, PacketMixin):
    _fields_ = [
        ("fastest_lap", FastestLap),
        ("retirement", Retirement),
        ("team_mate_in_pits", TeamMateInPits),
        ("race_winner", RaceWinner),
        ("penalty", Penalty),
        ("speed_trap", SpeedTrap),
        ("start_lights", StartLights),
        ("drive_through_penalty_served", DriveThroughPenaltyServed),
        ("stop_go_penalty_served", StopGoPenaltyServed),
        ("flashback", Flashback),
        ("buttons", Buttons),
    ]


class PacketEventData(Packet):
    _id_ = 3
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Event string code, see below
        ("m_event_string_code", ctypes.c_uint8 * 4),
        # Event details - should be interpreted differently
        # for each type
        ("m_event_details", EventDataDetails),
    ]
