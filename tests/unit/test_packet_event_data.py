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


def fastest_lap():
    return FastestLap(vehicle_idx=33, lap_time=80.0)


def fastest_lap__dict_representation():
    return {"vehicle_idx": 33, "lap_time": 80.0}


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


def retirement():
    return Retirement(vehicle_idx=33)


def retirement__dict_representation():
    return {"vehicle_idx": 33}


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


def team_mate_in_pits():
    return TeamMateInPits(vehicle_idx=33)


def team_mate_in_pits__dict_representation():
    return {"vehicle_idx": 33}


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


def race_winner():
    return RaceWinner(vehicle_idx=33)


def race_winner__dict_representation():
    return {"vehicle_idx": 33}


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


def penalty():
    return Penalty(
        penalty_type=4, infringement_type=3, vehicle_idx=33, other_vehicle_idx=22, time=5, lap_num=29, places_gained=0
    )


def penalty__dict_representation():
    return {
        "penalty_type": 4,
        "infringement_type": 3,
        "vehicle_idx": 33,
        "other_vehicle_idx": 22,
        "time": 5,
        "lap_num": 29,
        "places_gained": 0,
    }


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


def speed_trap():
    return SpeedTrap(vehicle_idx=33, speed=245, overall_fastest_in_session=1, driver_fastest_in_session=0)


def speed_trap__dict_representation():
    return {"vehicle_idx": 33, "speed": 245, "overall_fastest_in_session": 1, "driver_fastest_in_session": 0}


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


def start_lights():
    return StartLights(num_lights=2)


def start_lights__dict_representation():
    return {"num_lights": 2}


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


def drive_through_penalty_served():
    return DriveThroughPenaltyServed(vehicle_idx=33)


def drive_through_penalty_served__dict_representation():
    return {"vehicle_idx": 33}


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


def stop_go_penalty_served():
    return StopGoPenaltyServed(vehicle_idx=33)


def stop_go_penalty_served__dict_representation():
    return {"vehicle_idx": 33}


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


def flashback():
    return Flashback(flashback_frame_identifier=1234, flashback_session_time=782.0)


def flashback__dict_representation():
    return {"flashback_frame_identifier": 1234, "flashback_session_time": 782.0}


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


def buttons():
    return Buttons(m_button_status=26)


def buttons__dict_representation():
    return {"m_button_status": 26}


def packet_builder(event_code, event_name, event_instance):
    return PacketEventData(
        m_header=PacketHeader(
            m_packet_format=2021,
            m_game_major_version=1,
            m_game_minor_version=23,
            m_packet_version=25,
            m_packet_id=3,
            m_session_uid=2501,
            m_session_time=25.01,
            m_frame_identifier=123,
            m_player_car_index=6,
            m_secondary_player_car_index=255,
        ),
        m_event_string_code=(ctypes.c_uint8 * 4)(*list(map(ord, event_code))),
        m_event_details=EventDataDetails(**{event_name: event_instance}),
    )


def dict_representation_builder(event_code, event_name, event__dict_representation):
    event_details = {
        "fastest_lap": fastest_lap__dict_representation(),
        "retirement": retirement__dict_representation(),
        "team_mate_in_pits": team_mate_in_pits__dict_representation(),
        "race_winner": race_winner__dict_representation(),
        "penalty": penalty__dict_representation(),
        "speed_trap": speed_trap__dict_representation(),
        "start_lights": start_lights__dict_representation(),
        "drive_through_penalty_served": drive_through_penalty_served__dict_representation(),
        "stop_go_penalty_served": stop_go_penalty_served__dict_representation(),
        "flashback": flashback__dict_representation(),
        "buttons": buttons__dict_representation(),
    }
    event_details.update({event_name: event__dict_representation})

    return {
        "m_header": {
            "m_packet_format": 2021,
            "m_game_major_version": 1,
            "m_game_minor_version": 23,
            "m_packet_version": 25,
            "m_packet_id": 3,
            "m_session_uid": 2501,
            "m_session_time": 25.01,
            "m_frame_identifier": 123,
            "m_player_car_index": 6,
            "m_secondary_player_car_index": 255,
        },
        "m_event_string_code": list(map(ord, event_code)),
        "m_event_details": event_details,
    }


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


@pytest.mark.parametrize(
    "event_short, event_name, event_builder, event_dict_representation_builder",
    [
        ("FAST", "fastest_lap", fastest_lap, fastest_lap__dict_representation),
        ("RETI", "retirement", retirement, retirement__dict_representation),
        ("TEAM", "team_mate_in_pits", team_mate_in_pits, team_mate_in_pits__dict_representation),
        ("RACE", "race_winner", race_winner, race_winner__dict_representation),
        ("PENA", "penalty", penalty, penalty__dict_representation),
        ("SPEE", "speed_trap", speed_trap, speed_trap__dict_representation),
        ("STAR", "start_lights", start_lights, start_lights__dict_representation),
        (
            "DRIV",
            "drive_through_penalty_served",
            drive_through_penalty_served,
            drive_through_penalty_served__dict_representation,
        ),
        ("STOP", "stop_go_penalty_served", stop_go_penalty_served, stop_go_penalty_served__dict_representation),
        ("FLAS", "flashback", flashback, flashback__dict_representation),
        ("BUTT", "buttons", buttons, buttons__dict_representation),
    ],
)
def test_packet_car_status_data__to_dict(event_short, event_name, event_builder, event_dict_representation_builder):
    packet = packet_builder(event_short, event_name, event_builder())
    expected_dict_representation = dict_representation_builder(
        event_short, event_name, event_dict_representation_builder()
    )
    actual_dict_representation = packet.to_dict()

    assert actual_dict_representation["m_header"] == expected_dict_representation["m_header"]
    assert actual_dict_representation["m_event_string_code"] == expected_dict_representation["m_event_string_code"]
    assert (
        actual_dict_representation["m_event_details"][event_name]
        == expected_dict_representation["m_event_details"][event_name]
    )
