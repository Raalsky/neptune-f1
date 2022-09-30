import ctypes

import pytest

from neptune_f1.packets.codemasters_f12021.packet_event_data import (
    Buttons,
    DriveThroughPenaltyServed,
    EventDataDetails,
    FastestLap,
    Flashback,
    PacketEventData,
    Penalty,
    RaceWinner,
    Retirement,
    SpeedTrap,
    StartLights,
    StopGoPenaltyServed,
    TeamMateInPits,
)
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of car achieving fastest lap
        ("vehicle_idx", ctypes.c_uint8),
        # Lap time is in seconds
        ("lap_time", ctypes.c_float),
    ],
)
def test_fastest_lap__field__types(type_name, type_class):
    packet_type = FastestLap()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of car retiring
        ("vehicle_idx", ctypes.c_uint8),
    ],
)
def test_retirement__field__types(type_name, type_class):
    packet_type = Retirement()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of team mate
        ("vehicle_idx", ctypes.c_uint8),
    ],
)
def test_team_mate_in_pits__field__types(type_name, type_class):
    packet_type = TeamMateInPits()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of the race winner
        ("vehicle_idx", ctypes.c_uint8),
    ],
)
def test_race_winner__field__types(type_name, type_class):
    packet_type = RaceWinner()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
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
    ],
)
def test_penalty__field__types(type_name, type_class):
    packet_type = Penalty()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of the vehicle triggering speed trap
        ("vehicle_idx", ctypes.c_uint8),
        # Top speed achieved in kilometres per hour
        ("speed", ctypes.c_float),
        # Overall fastest speed in session = 1, otherwise 0
        ("overall_fastest_in_session", ctypes.c_uint8),
        # Fastest speed for driver in session = 1, otherwise 0
        ("driver_fastest_in_session", ctypes.c_uint8),
    ],
)
def test_speed_trap__field__types(type_name, type_class):
    packet_type = SpeedTrap()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Number of lights showing
        ("num_lights", ctypes.c_uint8),
    ],
)
def test_start_lights__field__types(type_name, type_class):
    packet_type = StartLights()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of the vehicle serving drive through
        ("vehicle_idx", ctypes.c_uint8),
    ],
)
def test_drive_through_penalty_served__field__types(type_name, type_class):
    packet_type = DriveThroughPenaltyServed()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Vehicle index of the vehicle serving stop go
        ("vehicle_idx", ctypes.c_uint8),
    ],
)
def test_stop_go_penalty_served__field__types(type_name, type_class):
    packet_type = StopGoPenaltyServed()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Frame identifier flashed back to
        ("flashback_frame_identifier", ctypes.c_uint32),
        # Session time flashed back to
        ("flashback_session_time", ctypes.c_float),
    ],
)
def test_flashback__field__types(type_name, type_class):
    packet_type = Flashback()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Bit flags specifying which buttons are being pressed
        # currently - see appendices
        ("m_button_status", ctypes.c_uint32),
    ],
)
def test_buttons__field__types(type_name, type_class):
    packet_type = Buttons()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
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
    ],
)
def test_event_data_details__field__types(type_name, type_class):
    packet_type = EventDataDetails()

    assert (type_name, type_class) in packet_type._fields_


@pytest.mark.parametrize(
    "type_name, type_class",
    [
        # Header
        ("m_header", PacketHeader),
        # Event string code, see below
        ("m_event_string_code", ctypes.c_uint8 * 4),
        # Event details - should be interpreted differently
        # for each type
        ("m_event_details", EventDataDetails),
    ],
)
def test_packet_event_data__field__types(type_name, type_class):
    packet_type = PacketEventData()

    assert (type_name, type_class) in packet_type._fields_
