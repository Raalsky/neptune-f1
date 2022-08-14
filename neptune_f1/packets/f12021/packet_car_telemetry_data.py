import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class CarTelemetryData(Packet):
    _fields_ = [
        # Speed of car in kilometres per hour
        ("m_speed", ctypes.c_uint16),
        # Amount of throttle applied (0.0 to 1.0)
        ("m_throttle", ctypes.c_float),
        # Steering (-1.0 (full lock left) to 1.0 (full lock right))
        ("m_steer", ctypes.c_float),
        # Amount of brake applied (0.0 to 1.0)
        ("m_brake", ctypes.c_float),
        # Amount of clutch applied (0 to 100)
        ("m_clutch", ctypes.c_uint8),
        # Gear selected (1-8, N=0, R=-1)
        ("m_gear", ctypes.c_int8),
        # Engine RPM
        ("m_engine_rpm", ctypes.c_uint16),
        # 0 = off, 1 = on
        ("m_drs", ctypes.c_uint8),
        # Rev lights indicator (percentage)
        ("m_rev_lights_percent", ctypes.c_uint8),
        # Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
        ("m_rev_lights_bit_value", ctypes.c_uint16),
        # Brakes temperature (celsius)
        ("m_brakes_temperature", ctypes.c_uint16 * 4),
        # Tyres surface temperature (celsius)
        ("m_tyres_surface_temperature", ctypes.c_uint8 * 4),
        # Tyres inner temperature (celsius)
        ("m_tyres_inner_temperature", ctypes.c_uint8 * 4),
        # Engine temperature (celsius)
        ("m_engine_temperature", ctypes.c_uint16),
        # Tyres pressure (PSI)
        ("m_tyres_pressure", ctypes.c_float * 4),
        # Driving surface, see appendices
        ("m_surface_type", ctypes.c_uint8 * 4),
    ]


class PacketCarTelemetryData(Packet):
    _id_ = 6
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Car Telemetry data array
        ("m_car_telemetry_data", CarTelemetryData * 22),
        # Index of MFD panel open - 255 = MFD closed
        # Single player, race – 0 = Car setup, 1 = Pits
        # 2 = Damage, 3 =  Engine, 4 = Temperatures
        # May vary depending on game mode
        ("m_mfd_panel_index", ctypes.c_uint8),
        # See above
        ("m_mfd_panel_index_secondary_player", ctypes.c_uint8),
        # Suggested gear for the player (1-8)
        # 0 if no gear suggested
        ("m_suggested_gear", ctypes.c_int8),
    ]
