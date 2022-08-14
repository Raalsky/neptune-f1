import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class CarStatusData(Packet):
    _fields_ = [
        # Traction control - 0 = off, 1 = medium, 2 = full
        ("m_traction_control", ctypes.c_uint8),
        # 0 (off) - 1 (on)
        ("m_anti_lock_brakes", ctypes.c_uint8),
        # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        ("m_fuel_mix", ctypes.c_uint8),
        # Front brake bias (percentage)
        ("m_front_brake_bias", ctypes.c_uint8),
        # Pit limiter status - 0 = off, 1 = on
        ("m_pit_limiter_status", ctypes.c_uint8),
        # Current fuel mass
        ("m_fuel_in_tank", ctypes.c_float),
        # Fuel capacity
        ("m_fuel_capacity", ctypes.c_float),
        # Fuel remaining in terms of laps (value on MFD)
        ("m_fuel_remaining_laps", ctypes.c_float),
        # Cars max RPM, point of rev limiter
        ("m_max_rpm", ctypes.c_uint16),
        # Cars idle RPM
        ("m_idle_rpm", ctypes.c_uint16),
        # Maximum number of gears
        ("m_max_gears", ctypes.c_uint8),
        # 0 = not allowed, 1 = allowed
        ("m_drs_allowed", ctypes.c_uint8),
        # 0 = DRS not available, non-zero - DRS will be available
        # in [X] metres
        ("m_drs_activation_distance", ctypes.c_uint16),
        # F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1
        # 7 = inter, 8 = wet
        # F1 Classic - 9 = dry, 10 = wet
        # F2 – 11 = super soft, 12 = soft, 13 = medium, 14 = hard
        # 15 = wet
        ("m_actual_tyre_compound", ctypes.c_uint8),
        # F1 visual (can be different from actual compound)
        # 16 = soft, 17 = medium, 18 = hard, 7 = inter, 8 = wet
        # F1 Classic – same as above
        # F2 ‘19, 15 = wet, 19 – super soft, 20 = soft
        # 21 = medium , 22 = hard
        ("m_visual_tyre_compound", ctypes.c_uint8),
        # Age in laps of the current set of tyres
        ("m_tyres_age_laps", ctypes.c_uint8),
        # -1 = invalid/unknown, 0 = none, 1 = green
        # 2 = blue, 3 = yellow, 4 = red
        ("m_vehicle_fia_flags", ctypes.c_int8),
        # ERS energy store in Joules
        ("m_ers_store_energy", ctypes.c_float),
        # ERS deployment mode, 0 = none, 1 = medium
        # 2 = hotlap, 3 = overtake
        ("m_ers_deploy_mode", ctypes.c_uint8),
        # ERS energy harvested this lap by MGU-K
        ("m_ers_harvested_this_lap_mguk", ctypes.c_float),
        # ERS energy harvested this lap by MGU-H
        ("m_ers_harvested_this_lap_mguh", ctypes.c_float),
        # ERS energy deployed this lap
        ("m_ers_deployed_this_lap", ctypes.c_float),
        # Whether the car is paused in a network game
        ("m_network_paused", ctypes.c_uint8),
    ]


class PacketCarStatusData(Packet):
    _id_ = 7
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Car status data array
        ("m_car_status_data", CarStatusData * 22),
    ]
