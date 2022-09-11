from dataclasses import dataclass

from neptune_f1.packets.f12021 import LapHistoryData, TyreStintHistoryData


@dataclass
class LapHistory:
    # Lap time in milliseconds
    lap_time_in_ms: int

    # Sector 1 time in milliseconds
    sector1_time_in_ms: int

    # Sector 2 time in milliseconds
    sector2_time_in_ms: int

    # Sector 3 time in milliseconds
    sector3_time_in_ms: int

    # 0x01 bit set-lap valid,      0x02 bit set-sector 1 valid
    # 0x04 bit set-sector 2 valid, 0x08 bit set-sector 3 valid
    lap_valid_bit_flags: int


@dataclass
class TyreStintHistory:
    # Lap the tyre usage ends on (255 of current tyre)
    end_lap: int

    # Actual tyres used by this driver
    tyre_actual_compound: int

    # Visual tyres used by this driver
    tyre_visual_compound: int


@dataclass
class SessionHistory:
    # Index of the car this lap data relates to
    car_idx: int

    # Num laps in the data (including current partial lap)
    num_laps: int

    # Number of tyre stints in the data
    num_tyre_stints: int

    # Lap the best lap time was achieved on
    best_lap_time_lap_num: int

    # Lap the best Sector 1 time was achieved on
    best_sector1_lap_num: int

    # Lap the best Sector 2 time was achieved on
    best_sector2_lap_num: int

    # Lap the best Sector 3 time was achieved on
    best_sector3_lap_num: int

    # 100 laps of data max
    lap_history_data: list[LapHistoryData]

    # Tyre stints history array
    tyre_stints_history_data: list[TyreStintHistoryData]
