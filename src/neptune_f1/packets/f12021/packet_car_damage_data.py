import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class CarDamageData(Packet):
    _fields_ = [
        # Tyre wear (percentage)
        ("m_tyres_wear", ctypes.c_float * 4),
        # Tyre damage (percentage)
        ("m_tyres_damage", ctypes.c_uint8 * 4),
        # Brakes damage (percentage)
        ("m_brakes_damage", ctypes.c_uint8 * 4),
        # Front left wing damage (percentage)
        ("m_front_left_wing_damage", ctypes.c_uint8),
        # Front right wing damage (percentage)
        ("m_front_right_wing_damage", ctypes.c_uint8),
        # Rear wing damage (percentage)
        ("m_rear_wing_damage", ctypes.c_uint8),
        # Floor damage (percentage)
        ("m_floor_damage", ctypes.c_uint8),
        # Diffuser damage (percentage)
        ("m_diffuser_damage", ctypes.c_uint8),
        # Sidepod damage (percentage)
        ("m_sidepod_damage", ctypes.c_uint8),
        # Indicator for DRS fault, 0 = OK, 1 = fault
        ("m_drs_fault", ctypes.c_uint8),
        # Gear box damage (percentage)
        ("m_gear_box_damage", ctypes.c_uint8),
        # Engine damage (percentage)
        ("m_engine_damage", ctypes.c_uint8),
        # Engine wear MGU-H (percentage)
        ("m_engine_mguhwear", ctypes.c_uint8),
        # Engine wear ES (percentage)
        ("m_engine_eswear", ctypes.c_uint8),
        # Engine wear CE (percentage)
        ("m_engine_cewear", ctypes.c_uint8),
        # Engine wear ICE (percentage)
        ("m_engine_icewear", ctypes.c_uint8),
        # Engine wear MGU-K (percentage)
        ("m_engine_mgukwear", ctypes.c_uint8),
        # Engine wear TC (percentage)
        ("m_engine_tcwear", ctypes.c_uint8),
    ]


class PacketCarDamageData(Packet):
    _id_ = 10
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Car damage data array
        ("m_car_damage_data", CarDamageData * 22),
    ]
