import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class CarSetupData(Packet):
    _fields_ = [
        # Front wing aero
        ("m_front_wing", ctypes.c_uint8),
        # Rear wing aero
        ("m_rear_wing", ctypes.c_uint8),
        # Differential adjustment on throttle (percentage)
        ("m_on_throttle", ctypes.c_uint8),
        # Differential adjustment off throttle (percentage)
        ("m_off_throttle", ctypes.c_uint8),
        # Front camber angle (suspension geometry)
        ("m_front_camber", ctypes.c_float),
        # Rear camber angle (suspension geometry)
        ("m_rear_camber", ctypes.c_float),
        # Front toe angle (suspension geometry)
        ("m_front_toe", ctypes.c_float),
        # Rear toe angle (suspension geometry)
        ("m_rear_toe", ctypes.c_float),
        # Front suspension
        ("m_front_suspension", ctypes.c_uint8),
        # Rear suspension
        ("m_rear_suspension", ctypes.c_uint8),
        # Front anti-roll bar
        ("m_front_anti_roll_bar", ctypes.c_uint8),
        # Front anti-roll bar
        ("m_rear_anti_roll_bar", ctypes.c_uint8),
        # Front ride height
        ("m_front_suspension_height", ctypes.c_uint8),
        # Rear ride height
        ("m_rear_suspension_height", ctypes.c_uint8),
        # Brake pressure (percentage)
        ("m_brake_pressure", ctypes.c_uint8),
        # Brake bias (percentage)
        ("m_brake_bias", ctypes.c_uint8),
        # Rear left tyre pressure (PSI)
        ("m_rear_left_tyre_pressure", ctypes.c_float),
        # Rear right tyre pressure (PSI)
        ("m_rear_right_tyre_pressure", ctypes.c_float),
        # Front left tyre pressure (PSI)
        ("m_front_left_tyre_pressure", ctypes.c_float),
        # Front right tyre pressure (PSI)
        ("m_front_right_tyre_pressure", ctypes.c_float),
        # Ballast
        ("m_ballast", ctypes.c_uint8),
        # Fuel load
        ("m_fuel_load", ctypes.c_float),
    ]


class PacketCarSetupData(Packet):
    _id_ = 5
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Car setup data array
        ("m_car_setups", CarSetupData * 22),
    ]
