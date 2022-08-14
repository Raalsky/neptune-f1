import ctypes

from .packet_header import PacketHeader
from .utils import Packet


class LapData(Packet):
    _fields_ = [
        # Last lap time in milliseconds
        ("m_last_lap_time_in_ms", ctypes.c_uint32),
        # Current time around the lap in milliseconds
        ("m_current_lap_time_in_ms", ctypes.c_uint32),
        # Sector 1 time in milliseconds
        ("m_sector1_time_in_ms", ctypes.c_uint16),
        # Sector 2 time in milliseconds
        ("m_sector2_time_in_ms", ctypes.c_uint16),
        # Distance vehicle is around current lap in metres – could
        # be negative if line hasn’t been crossed yet
        ("m_lap_distance", ctypes.c_float),
        # Total distance travelled in session in metres – could
        # be negative if line hasn’t been crossed yet
        ("m_total_distance", ctypes.c_float),
        # Delta in seconds for safety car
        ("m_safety_car_delta", ctypes.c_float),
        # Car race position
        ("m_car_position", ctypes.c_uint8),
        # Current lap number
        ("m_current_lap_num", ctypes.c_uint8),
        # 0 = none, 1 = pitting, 2 = in pit area
        ("m_pit_status", ctypes.c_uint8),
        # Number of pit stops taken in this race
        ("m_num_pit_stops", ctypes.c_uint8),
        # 0 = sector1, 1 = sector2, 2 = sector3
        ("m_sector", ctypes.c_uint8),
        # Current lap invalid - 0 = valid, 1 = invalid
        ("m_current_lap_invalid", ctypes.c_uint8),
        # Accumulated time penalties in seconds to be added
        ("m_penalties", ctypes.c_uint8),
        # Accumulated number of warnings issued
        ("m_warnings", ctypes.c_uint8),
        # Num drive through pens left to serve
        ("m_num_unserved_drive_through_pens", ctypes.c_uint8),
        # Num stop go pens left to serve
        ("m_num_unserved_stop_go_pens", ctypes.c_uint8),
        # Grid position the vehicle started the race in
        ("m_grid_position", ctypes.c_uint8),
        # Status of driver - 0 = in garage, 1 = flying lap
        # 2 = in lap, 3 = out lap, 4 = on track
        ("m_driver_status", ctypes.c_uint8),
        # Result status - 0 = invalid, 1 = inactive, 2 = active
        # 3 = finished, 4 = didnotfinish, 5 = disqualified
        # 6 = not classified, 7 = retired
        ("m_result_status", ctypes.c_uint8),
        # Pit lane timing, 0 = inactive, 1 = active
        ("m_pit_lane_timer_active", ctypes.c_uint8),
        # If active, the current time spent in the pit lane in ms
        ("m_pit_lane_time_in_lane_in_ms", ctypes.c_uint16),
        # Time of the actual pit stop in ms
        ("m_pit_stop_timer_in_ms", ctypes.c_uint16),
        # Whether the car should serve a penalty at this stop
        ("m_pit_stop_should_serve_pen", ctypes.c_uint8),
    ]


class PacketLapData(Packet):
    _id_ = 2
    _fields_ = [
        # Header
        ("m_header", PacketHeader),
        # Lap data for all cars on track
        ("m_lap_data", LapData * 22),
    ]
