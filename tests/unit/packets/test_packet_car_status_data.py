import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_car_status_data import CarStatusData, PacketCarStatusData
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


def single():
    return CarStatusData(
        m_traction_control=2,
        m_anti_lock_brakes=1,
        m_fuel_mix=3,
        m_front_brake_bias=55,
        m_pit_limiter_status=0,
        m_fuel_in_tank=29.5,
        m_fuel_capacity=55.0,
        m_fuel_remaining_laps=30.5,
        m_max_rpm=13000,
        m_idle_rpm=8000,
        m_max_gears=8,
        m_drs_allowed=1,
        m_drs_activation_distance=2530,
        m_actual_tyre_compound=16,
        m_visual_tyre_compound=16,
        m_tyres_age_laps=5,
        m_vehicle_fia_flags=1,
        m_ers_store_energy=50.0,
        m_ers_deploy_mode=2,
        m_ers_harvested_this_lap_mguk=4.0,
        m_ers_harvested_this_lap_mguh=2.0,
        m_ers_deployed_this_lap=12.0,
        m_network_paused=0,
    )


def single__dict_representation():
    return {
        "m_traction_control": 2,
        "m_anti_lock_brakes": 1,
        "m_fuel_mix": 3,
        "m_front_brake_bias": 55,
        "m_pit_limiter_status": 0,
        "m_fuel_in_tank": 29.5,
        "m_fuel_capacity": 55.0,
        "m_fuel_remaining_laps": 30.5,
        "m_max_rpm": 13000,
        "m_idle_rpm": 8000,
        "m_max_gears": 8,
        "m_drs_allowed": 1,
        "m_drs_activation_distance": 2530,
        "m_actual_tyre_compound": 16,
        "m_visual_tyre_compound": 16,
        "m_tyres_age_laps": 5,
        "m_vehicle_fia_flags": 1,
        "m_ers_store_energy": 50.0,
        "m_ers_deploy_mode": 2,
        "m_ers_harvested_this_lap_mguk": 4.0,
        "m_ers_harvested_this_lap_mguh": 2.0,
        "m_ers_deployed_this_lap": 12.0,
        "m_network_paused": 0,
    }


def single__json_representation():
    return """{
      "m_actual_tyre_compound": 16,
      "m_anti_lock_brakes": 1,
      "m_drs_activation_distance": 2530,
      "m_drs_allowed": 1,
      "m_ers_deploy_mode": 2,
      "m_ers_deployed_this_lap": 12.0,
      "m_ers_harvested_this_lap_mguh": 2.0,
      "m_ers_harvested_this_lap_mguk": 4.0,
      "m_ers_store_energy": 50.0,
      "m_front_brake_bias": 55,
      "m_fuel_capacity": 55.0,
      "m_fuel_in_tank": 29.5,
      "m_fuel_mix": 3,
      "m_fuel_remaining_laps": 30.5,
      "m_idle_rpm": 8000,
      "m_max_gears": 8,
      "m_max_rpm": 13000,
      "m_network_paused": 0,
      "m_pit_limiter_status": 0,
      "m_traction_control": 2,
      "m_tyres_age_laps": 5,
      "m_vehicle_fia_flags": 1,
      "m_visual_tyre_compound": 16
    }"""


def single__binary_representation():
    return (
        b"\x02\x01\x03\x37\x00\x00\x00\xec\x41\x00\x00\x5c\x42\x00\x00\xf4\x41\xc8\x32\x40\x1f\x08\x01\xe2\x09\x10\x10"
        b"\x05\x01\x00\x00\x48\x42\x02\x00\x00\x80\x40\x00\x00\x00\x40\x00\x00\x40\x41\x00"
    )


@pytest.fixture
def packet():
    return PacketCarStatusData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=7,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_car_status_data=(CarStatusData * 22)(*[single() for _ in range(22)]),
    )


@pytest.fixture
def dict_representation():
    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 7,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_car_status_data": [single__dict_representation() for _ in range(22)],
    }


@pytest.fixture
def json_representation():
    entries = ",\n    ".join(single__json_representation() for _ in range(22))

    return (
        "{\n"
        '  "m_car_status_data": [\n    '
        f"{entries}\n"
        "  ],\n"
        '  "m_header": {\n'
        '    "m_frame_identifier": 123,\n'
        '    "m_game_major_version": 1,\n'
        '    "m_game_minor_version": 23,\n'
        '    "m_packet_format": 2021,\n'
        '    "m_packet_id": 7,\n'
        '    "m_packet_version": 25,\n'
        '    "m_player_car_index": 6,\n'
        '    "m_secondary_player_car_index": 255,\n'
        '    "m_session_time": 25.01,\n'
        '    "m_session_uid": 2501\n'
        "  }\n"
        "}"
    )


@pytest.fixture
def binary_representation():
    return (
        b"\xe5\x07\x01\x17\x19\x07\xc5\x09\x00\x00\x00\x00\x00\x00\x7b\x14\xc8\x41\x7b\x00\x00\x00\x06\xff"
        + single__binary_representation() * 22
    )


@pytest.mark.parametrize(
    "type_name, type_class",
    [
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
    ],
)
def test_car_status_data__field__types(type_name, type_class):
    packet_type = CarStatusData()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        ("m_car_status_data", CarStatusData * 22),
    ],
)
def test_packet_car_status_data__field__types(type_name, type_class):
    packet_type = PacketCarStatusData()

    assert (type_name, type_class) in packet_type._fields_


def test_packet_car_status_data__to_dict(packet, dict_representation):
    assert packet.to_dict() == dict_representation


def test_packet_car_status_data__get_value(packet, dict_representation):
    for field, value in dict_representation.items():
        assert packet.get_value(field=field) == value


def test_packet_car_status_data__to_json(packet, json_representation):
    assert packet.to_json() == json_representation


def test_packet_car_status_data__to_binary(packet, binary_representation):
    assert packet.pack() == binary_representation


def test_packet_car_status_data__from_binary(binary_representation, dict_representation):
    packet = PacketCarStatusData.unpack(binary_representation)

    assert packet.to_dict() == dict_representation
