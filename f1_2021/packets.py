import json
import ctypes
import typing
import pathlib


def to_json(*args, **kwargs):
    kwargs.setdefault('indent', 2)

    kwargs['sort_keys'] = True
    kwargs['ensure_ascii'] = False
    kwargs['separators'] = (',', ': ')

    return json.dumps(*args, **kwargs)


class PacketMixin:
    def get_value(self: ctypes.Structure, field):
        """Returns the field's value and formats the types value

        """
        return self._format_type(getattr(self, field))

    def pack(self: ctypes.Structure):
        """Packs the current data structure into a compressed binary

        Returns:
            (bytes):
                - The packed binary

        """
        return bytes(self)

    @classmethod
    def size(cls: ctypes.Structure):
        return ctypes.sizeof(cls)

    @classmethod
    def unpack(cls: ctypes.Structure, buffer):
        """Attempts to unpack the binary structure into a python structure

        Args:
            buffer (bytes):
                - The encoded buffer to decode

        """
        return cls.from_buffer_copy(buffer)

    def to_dict(self: ctypes.Structure):
        """Returns a ``dict`` with key-values derived from _fields_

        """
        return {k: self.get_value(k) for k, _ in self._fields_}

    def to_json(self: ctypes.Structure):
        """Returns a ``str`` of sorted JSON derived from _fields_

        """
        return to_json(self.to_dict())

    def _format_type(self: ctypes.Structure, value):
        """A type helper to format values

        """
        class_name = type(value).__name__

        if class_name == 'float':
            return round(value, 3)

        if class_name == 'bytes':
            # return value.decode()
            return list(map(int, value))

        if isinstance(value, ctypes.Array):
            return self._format_array_type(value)

        if hasattr(value, 'to_dict'):
            return value.to_dict()

        return value

    def _format_array_type(self: ctypes.Structure, value):
        results = []

        for item in value:
            if isinstance(item, Packet):
                results.append(item.to_dict())
            else:
                results.append(item)

        return results

    def __repr__(self: ctypes.Structure):
        return self.to_json()


class Packet(ctypes.LittleEndianStructure, PacketMixin):
    """The base packet class for API version 2021"""
    _pack_ = 1
    _id_ = None
    _version_ = 1
    _format_ = 2021

    @classmethod
    def get_identifier(cls) -> typing.Union[None, int]:
        return cls._id_

    @classmethod
    def get_version(cls) -> int:
        return cls._version_

    @classmethod
    def get_format(cls) -> int:
        return cls._format_


class PacketFactory:
    @staticmethod
    def header_size() -> int:
        return PacketHeader.size()

    @staticmethod
    def packet_identifiers() -> typing.Mapping[typing.Tuple[int, int, int], Packet.__class__]:
        return {
            (
                # Packet format
                packet_cls.get_format(),
                # Packet type id
                packet_cls.get_identifier(),
                # Packet type version
                packet_cls.get_version()
            ): packet_cls
            for packet_cls in Packet.__subclasses__()
            if packet_cls.get_identifier() is not None
        }

    @classmethod
    def from_handler(cls, handler) -> typing.Union[None, Packet]:
        if raw_header_data := handler.read(PacketFactory.header_size()):
            packet_header_data = bytearray(raw_header_data)
            header = PacketHeader.unpack(packet_header_data)

            print(header)

            packet_type_id = header.m_packet_id
            packet_type_version = header.m_packet_version
            packet_format = header.m_packet_format

            packet_cls = PacketFactory.packet_identifiers().get(
                (packet_format, packet_type_id, packet_type_version)
            )

            print(packet_cls)

            assert packet_cls, \
                f"Packet spec (format={packet_format}, id={packet_type_id}, version={packet_type_version}) unknown"

            raw_packet_data = handler.read(packet_cls.size() - PacketFactory.header_size())
            packet_data = bytearray(raw_packet_data)

            data = packet_cls.unpack(packet_header_data + packet_data)

            print(data)

            return data


class Parser:
    @classmethod
    def from_file(cls, filepath: typing.Union[pathlib.Path, str]): # -> typing.Generator[None, Packet, None]:
        with open(filepath, "rb") as handler:
            # w = 0
            while packet := PacketFactory.from_handler(handler):
                yield packet
            #     if w > 2:
            #         break
            #     w += 1
            # with open("../data/test.bin", 'wb') as handler2:
            #     handler2.write(handler.read(5000))


class PacketHeader(Packet):
    _fields_ = [
        # 2021
        ('m_packet_format', ctypes.c_uint16),

        # Game major version - "X.00"
        ('m_game_major_version', ctypes.c_uint8),

        # Game minor version - "1.XX"
        ('m_game_minor_version', ctypes.c_uint8),

        # Version of this packet type, all start from 1
        ('m_packet_version', ctypes.c_uint8),

        # Identifier for the packet type, see below
        ('m_packet_id', ctypes.c_uint8),

        # Unique identifier for the session
        ('m_session_uid', ctypes.c_uint64),

        # Session timestamp
        ('m_session_time', ctypes.c_float),

        # Identifier for the frame the data was retrieved on
        ('m_frame_identifier', ctypes.c_uint32),

        # Index of player's car in the array
        ('m_player_car_index', ctypes.c_uint8),

        # Index of secondary player's car in the array (splitscreen)
        # 255 if no second player
        ('m_secondary_player_car_index', ctypes.c_uint8),
    ]


class CarMotionData(Packet):
    _fields_ = [
        # World space X position
        ('m_world_position_x', ctypes.c_float),

        # World space Y position
        ('m_world_position_y', ctypes.c_float),

        # World space Z position
        ('m_world_position_z', ctypes.c_float),

        # Velocity in world space X
        ('m_world_velocity_x', ctypes.c_float),

        # Velocity in world space Y
        ('m_world_velocity_y', ctypes.c_float),

        # Velocity in world space Z
        ('m_world_velocity_z', ctypes.c_float),

        # World space forward X direction (normalised)
        ('m_world_forward_dir_x', ctypes.c_int16),

        # World space forward Y direction (normalised)
        ('m_world_forward_dir_y', ctypes.c_int16),

        # World space forward Z direction (normalised)
        ('m_world_forward_dir_z', ctypes.c_int16),

        # World space right X direction (normalised)
        ('m_world_right_dir_x', ctypes.c_int16),

        # World space right Y direction (normalised)
        ('m_world_right_dir_y', ctypes.c_int16),

        # World space right Z direction (normalised)
        ('m_world_right_dir_z', ctypes.c_int16),

        # Lateral G-Force component
        ('m_g_force_lateral', ctypes.c_float),

        # Longitudinal G-Force component
        ('m_g_force_longitudinal', ctypes.c_float),

        # Vertical G-Force component
        ('m_g_force_vertical', ctypes.c_float),

        # Yaw angle in radians
        ('m_yaw', ctypes.c_float),

        # Pitch angle in radians
        ('m_pitch', ctypes.c_float),

        # Roll angle in radians
        ('m_roll', ctypes.c_float),
    ]


class PacketMotionData(Packet):
    _id_ = 0
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Data for all cars on track
        # Extra player car ONLY data
        ('m_car_motion_data', CarMotionData * 22),

        # Note: All wheel arrays have the following order:
        ('m_suspension_position', ctypes.c_float * 4),

        # RL, RR, FL, FR
        ('m_suspension_velocity', ctypes.c_float * 4),

        # RL, RR, FL, FR
        ('m_suspension_acceleration', ctypes.c_float * 4),

        # Speed of each wheel
        ('m_wheel_speed', ctypes.c_float * 4),

        # Slip ratio for each wheel
        ('m_wheel_slip', ctypes.c_float * 4),

        # Velocity in local space
        ('m_local_velocity_x', ctypes.c_float),

        # Velocity in local space
        ('m_local_velocity_y', ctypes.c_float),

        # Velocity in local space
        ('m_local_velocity_z', ctypes.c_float),

        # Angular velocity x-component
        ('m_angular_velocity_x', ctypes.c_float),

        # Angular velocity y-component
        ('m_angular_velocity_y', ctypes.c_float),

        # Angular velocity z-component
        ('m_angular_velocity_z', ctypes.c_float),

        # Angular velocity x-component
        ('m_angular_acceleration_x', ctypes.c_float),

        # Angular velocity y-component
        ('m_angular_acceleration_y', ctypes.c_float),

        # Angular velocity z-component
        ('m_angular_acceleration_z', ctypes.c_float),

        # Current front wheels angle in radians
        ('m_front_wheels_angle', ctypes.c_float),
    ]


class MarshalZone(Packet):
    _fields_ = [
        # Fraction (0..1) of way through the lap the marshal zone starts
        ('m_zone_start', ctypes.c_float),

        # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        ('m_zone_flag', ctypes.c_int8),
    ]


class WeatherForecastSample(Packet):
    _fields_ = [
        # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1
        # 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2
        # 12 = Time Trial
        ('m_session_type', ctypes.c_uint8),

        # Time in minutes the forecast is for
        ('m_time_offset', ctypes.c_uint8),

        # Weather - 0 = clear, 1 = light cloud, 2 = overcast
        # 3 = light rain, 4 = heavy rain, 5 = storm
        ('m_weather', ctypes.c_uint8),

        # Track temp. in degrees Celsius
        ('m_track_temperature', ctypes.c_int8),

        # Track temp. change – 0 = up, 1 = down, 2 = no change
        ('m_track_temperature_change', ctypes.c_int8),

        # Air temp. in degrees celsius
        ('m_air_temperature', ctypes.c_int8),

        # Air temp. change – 0 = up, 1 = down, 2 = no change
        ('m_air_temperature_change', ctypes.c_int8),

        # Rain percentage (0-100)
        ('m_rain_percentage', ctypes.c_uint8),
    ]


class PacketSessionData(Packet):
    _id_ = 1
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Weather - 0 = clear, 1 = light cloud, 2 = overcast
        # 3 = light rain, 4 = heavy rain, 5 = storm
        ('m_weather', ctypes.c_uint8),

        # Track temp. in degrees celsius
        ('m_track_temperature', ctypes.c_int8),

        # Air temp. in degrees celsius
        ('m_air_temperature', ctypes.c_int8),

        # Total number of laps in this race
        ('m_total_laps', ctypes.c_uint8),

        # Track length in metres
        ('m_track_length', ctypes.c_uint16),

        # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
        # 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
        # 10 = R, 11 = R2, 12 = R3, 13 = Time Trial
        ('m_session_type', ctypes.c_uint8),

        # -1 for unknown, 0-21 for tracks, see appendix
        ('m_track_id', ctypes.c_int8),

        # Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2,
        # 3 = F1 Generic
        ('m_formula', ctypes.c_uint8),

        # Time left in session in seconds
        ('m_session_time_left', ctypes.c_uint16),

        # Session duration in seconds
        ('m_session_duration', ctypes.c_uint16),

        # Pit speed limit in kilometres per hour
        ('m_pit_speed_limit', ctypes.c_uint8),

        # Whether the game is paused
        ('m_game_paused', ctypes.c_uint8),

        # Whether the player is spectating
        ('m_is_spectating', ctypes.c_uint8),

        # Index of the car being spectated
        ('m_spectator_car_index', ctypes.c_uint8),

        # SLI Pro support, 0 = inactive, 1 = active
        ('m_sli_pro_native_support', ctypes.c_uint8),

        # Number of marshal zones to follow
        ('m_num_marshal_zones', ctypes.c_uint8),

        # List of marshal zones – max 21
        ('m_marshal_zones', MarshalZone * 21),

        # 0 = no safety car, 1 = full
        # 2 = virtual, 3 = formation lap
        ('m_safety_car_status', ctypes.c_uint8),

        # 0 = offline, 1 = online
        ('m_network_game', ctypes.c_uint8),

        # Number of weather samples to follow
        ('m_num_weather_forecast_samples', ctypes.c_uint8),

        # Array of weather forecast samples
        ('m_weather_forecast_samples', WeatherForecastSample * 56),

        # 0 = Perfect, 1 = Approximate
        ('m_forecast_accuracy', ctypes.c_uint8),

        # AI Difficulty rating – 0-110
        ('m_ai_difficulty', ctypes.c_uint8),

        # Identifier for season - persists across saves
        ('m_season_link_identifier', ctypes.c_uint32),

        # Identifier for weekend - persists across saves
        ('m_weekend_link_identifier', ctypes.c_uint32),

        # Identifier for session - persists across saves
        ('m_session_link_identifier', ctypes.c_uint32),

        # Ideal lap to pit on for current strategy (player)
        ('m_pit_stop_window_ideal_lap', ctypes.c_uint8),

        # Latest lap to pit on for current strategy (player)
        ('m_pit_stop_window_latest_lap', ctypes.c_uint8),

        # Predicted position to rejoin at (player)
        ('m_pit_stop_rejoin_position', ctypes.c_uint8),

        # 0 = off, 1 = on
        ('m_steering_assist', ctypes.c_uint8),

        # 0 = off, 1 = low, 2 = medium, 3 = high
        ('m_braking_assist', ctypes.c_uint8),

        # 1 = manual, 2 = manual & suggested gear, 3 = auto
        ('m_gearbox_assist', ctypes.c_uint8),

        # 0 = off, 1 = on
        ('m_pit_assist', ctypes.c_uint8),

        # 0 = off, 1 = on
        ('m_pit_release_assist', ctypes.c_uint8),

        # 0 = off, 1 = on
        ('m_ersassist', ctypes.c_uint8),

        # 0 = off, 1 = on
        ('m_drsassist', ctypes.c_uint8),

        # 0 = off, 1 = corners only, 2 = full
        ('m_dynamic_racing_line', ctypes.c_uint8),

        # 0 = 2D, 1 = 3D
        ('m_dynamic_racing_line_type', ctypes.c_uint8),
    ]


class LapData(Packet):
    _fields_ = [
        # Last lap time in milliseconds
        ('m_last_lap_time_in_ms', ctypes.c_uint32),

        # Current time around the lap in milliseconds
        ('m_current_lap_time_in_ms', ctypes.c_uint32),

        # Sector 1 time in milliseconds
        ('m_sector1_time_in_ms', ctypes.c_uint16),

        # Sector 2 time in milliseconds
        ('m_sector2_time_in_ms', ctypes.c_uint16),

        # Distance vehicle is around current lap in metres – could
        # be negative if line hasn’t been crossed yet
        ('m_lap_distance', ctypes.c_float),

        # Total distance travelled in session in metres – could
        # be negative if line hasn’t been crossed yet
        ('m_total_distance', ctypes.c_float),

        # Delta in seconds for safety car
        ('m_safety_car_delta', ctypes.c_float),

        # Car race position
        ('m_car_position', ctypes.c_uint8),

        # Current lap number
        ('m_current_lap_num', ctypes.c_uint8),

        # 0 = none, 1 = pitting, 2 = in pit area
        ('m_pit_status', ctypes.c_uint8),

        # Number of pit stops taken in this race
        ('m_num_pit_stops', ctypes.c_uint8),

        # 0 = sector1, 1 = sector2, 2 = sector3
        ('m_sector', ctypes.c_uint8),

        # Current lap invalid - 0 = valid, 1 = invalid
        ('m_current_lap_invalid', ctypes.c_uint8),

        # Accumulated time penalties in seconds to be added
        ('m_penalties', ctypes.c_uint8),

        # Accumulated number of warnings issued
        ('m_warnings', ctypes.c_uint8),

        # Num drive through pens left to serve
        ('m_num_unserved_drive_through_pens', ctypes.c_uint8),

        # Num stop go pens left to serve
        ('m_num_unserved_stop_go_pens', ctypes.c_uint8),

        # Grid position the vehicle started the race in
        ('m_grid_position', ctypes.c_uint8),

        # Status of driver - 0 = in garage, 1 = flying lap
        # 2 = in lap, 3 = out lap, 4 = on track
        ('m_driver_status', ctypes.c_uint8),

        # Result status - 0 = invalid, 1 = inactive, 2 = active
        # 3 = finished, 4 = didnotfinish, 5 = disqualified
        # 6 = not classified, 7 = retired
        ('m_result_status', ctypes.c_uint8),

        # Pit lane timing, 0 = inactive, 1 = active
        ('m_pit_lane_timer_active', ctypes.c_uint8),

        # If active, the current time spent in the pit lane in ms
        ('m_pit_lane_time_in_lane_in_ms', ctypes.c_uint16),

        # Time of the actual pit stop in ms
        ('m_pit_stop_timer_in_ms', ctypes.c_uint16),

        # Whether the car should serve a penalty at this stop
        ('m_pit_stop_should_serve_pen', ctypes.c_uint8),
    ]


class PacketLapData(Packet):
    _id_ = 2
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Lap data for all cars on track
        ('m_lap_data', LapData * 22),
    ]


class FastestLap(Packet):
    _fields_ = [
        # Vehicle index of car achieving fastest lap
        ('vehicle_idx', ctypes.c_uint8),

        # Lap time is in seconds
        ('lap_time', ctypes.c_float),
    ]


class Retirement(Packet):
    _fields_ = [
        # Vehicle index of car retiring
        ('vehicle_idx', ctypes.c_uint8),
    ]


class TeamMateInPits(Packet):
    _fields_ = [
        # Vehicle index of team mate
        ('vehicle_idx', ctypes.c_uint8),
    ]


class RaceWinner(Packet):
    _fields_ = [
        # Vehicle index of the race winner
        ('vehicle_idx', ctypes.c_uint8),
    ]


class Penalty(Packet):
    _fields_ = [
        # Penalty type – see Appendices
        ('penalty_type', ctypes.c_uint8),

        # Infringement type – see Appendices
        ('infringement_type', ctypes.c_uint8),

        # Vehicle index of the car the penalty is applied to
        ('vehicle_idx', ctypes.c_uint8),

        # Vehicle index of the other car involved
        ('other_vehicle_idx', ctypes.c_uint8),

        # Time gained, or time spent doing action in seconds
        ('time', ctypes.c_uint8),

        # Lap the penalty occurred on
        ('lap_num', ctypes.c_uint8),

        # Number of places gained by this
        ('places_gained', ctypes.c_uint8),
    ]


class SpeedTrap(Packet):
    _fields_ = [
        # Vehicle index of the vehicle triggering speed trap
        ('vehicle_idx', ctypes.c_uint8),

        # Top speed achieved in kilometres per hour
        ('speed', ctypes.c_float),

        # Overall fastest speed in session = 1, otherwise 0
        ('overall_fastest_in_session', ctypes.c_uint8),

        # Fastest speed for driver in session = 1, otherwise 0
        ('driver_fastest_in_session', ctypes.c_uint8),
    ]


class StartLIghts(Packet):
    _fields_ = [
        # Number of lights showing
        ('num_lights', ctypes.c_uint8),
    ]


class DriveThroughPenaltyServed(Packet):
    _fields_ = [
        # Vehicle index of the vehicle serving drive through
        ('vehicle_idx', ctypes.c_uint8),
    ]


class StopGoPenaltyServed(Packet):
    _fields_ = [
        # Vehicle index of the vehicle serving stop go
        ('vehicle_idx', ctypes.c_uint8),
    ]


class Flashback(Packet):
    _fields_ = [
        # Frame identifier flashed back to
        ('flashback_frame_identifier', ctypes.c_uint32),

        # Session time flashed back to
        ('flashback_session_time', ctypes.c_float),
    ]


class Buttons(Packet):
    _fields_ = [
        # Bit flags specifying which buttons are being pressed
        # currently - see appendices
        ('m_button_status', ctypes.c_uint32),
    ]


class EventDataDetails(ctypes.Union, PacketMixin):
    _fields_ = [
        ('fastest_lap', FastestLap),
        ('retirement', Retirement),
        ('team_mate_in_pits', TeamMateInPits),
        ('race_winner', RaceWinner),
        ('penalty', Penalty),
        ('speed_trap', SpeedTrap),
        ('start_lights', StartLIghts),
        ('drive_through_penalty_served', DriveThroughPenaltyServed),
        ('stop_go_penalty_served', StopGoPenaltyServed),
        ('flashback', Flashback),
        ('buttons', Buttons),
    ]


class PacketEventData(Packet):
    _id_ = 3
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Event string code, see below
        ('m_event_string_code', ctypes.c_uint8 * 4),

        # Event details - should be interpreted differently
        # for each type
        ('m_event_details', EventDataDetails),
    ]


class ParticipantData(Packet):
    _fields_ = [
        # Whether the vehicle is AI (1) or Human (0) controlled
        ('m_ai_controlled', ctypes.c_uint8),

        # Driver id - see appendix, 255 if network human
        ('m_driver_id', ctypes.c_uint8),

        # Network id – unique identifier for network players
        ('m_network_id', ctypes.c_uint8),

        # Team id - see appendix
        ('m_team_id', ctypes.c_uint8),

        # My team flag – 1 = My Team, 0 = otherwise
        ('m_my_team', ctypes.c_uint8),

        # Race number of the car
        ('m_race_number', ctypes.c_uint8),

        # Nationality of the driver
        ('m_nationality', ctypes.c_uint8),

        # Name of participant in UTF-8 format – null terminated
        # Will be truncated with … (U+2026) if too long
        ('m_name', ctypes.c_char * 48),

        # The player's UDP setting, 0 = restricted, 1 = public
        ('m_your_telemetry', ctypes.c_uint8),
    ]


class PacketParticipantsData(Packet):
    _id_ = 4
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Number of active cars in the data – should match number of
        # cars on HUD
        ('m_num_active_cars', ctypes.c_uint8),

        # Participant data array
        ('m_participants', ParticipantData * 22),
    ]


class CarSetupData(Packet):
    _fields_ = [
        # Front wing aero
        ('m_front_wing', ctypes.c_uint8),

        # Rear wing aero
        ('m_rear_wing', ctypes.c_uint8),

        # Differential adjustment on throttle (percentage)
        ('m_on_throttle', ctypes.c_uint8),

        # Differential adjustment off throttle (percentage)
        ('m_off_throttle', ctypes.c_uint8),

        # Front camber angle (suspension geometry)
        ('m_front_camber', ctypes.c_float),

        # Rear camber angle (suspension geometry)
        ('m_rear_camber', ctypes.c_float),

        # Front toe angle (suspension geometry)
        ('m_front_toe', ctypes.c_float),

        # Rear toe angle (suspension geometry)
        ('m_rear_toe', ctypes.c_float),

        # Front suspension
        ('m_front_suspension', ctypes.c_uint8),

        # Rear suspension
        ('m_rear_suspension', ctypes.c_uint8),

        # Front anti-roll bar
        ('m_front_anti_roll_bar', ctypes.c_uint8),

        # Front anti-roll bar
        ('m_rear_anti_roll_bar', ctypes.c_uint8),

        # Front ride height
        ('m_front_suspension_height', ctypes.c_uint8),

        # Rear ride height
        ('m_rear_suspension_height', ctypes.c_uint8),

        # Brake pressure (percentage)
        ('m_brake_pressure', ctypes.c_uint8),

        # Brake bias (percentage)
        ('m_brake_bias', ctypes.c_uint8),

        # Rear left tyre pressure (PSI)
        ('m_rear_left_tyre_pressure', ctypes.c_float),

        # Rear right tyre pressure (PSI)
        ('m_rear_right_tyre_pressure', ctypes.c_float),

        # Front left tyre pressure (PSI)
        ('m_front_left_tyre_pressure', ctypes.c_float),

        # Front right tyre pressure (PSI)
        ('m_front_right_tyre_pressure', ctypes.c_float),

        # Ballast
        ('m_ballast', ctypes.c_uint8),

        # Fuel load
        ('m_fuel_load', ctypes.c_float),
    ]


class PacketCarSetupData(Packet):
    _id_ = 5
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Car setup data array
        ('m_car_setups', CarSetupData * 22),
    ]


class CarTelemetryData(Packet):
    _fields_ = [
        # Speed of car in kilometres per hour
        ('m_speed', ctypes.c_uint16),

        # Amount of throttle applied (0.0 to 1.0)
        ('m_throttle', ctypes.c_float),

        # Steering (-1.0 (full lock left) to 1.0 (full lock right))
        ('m_steer', ctypes.c_float),

        # Amount of brake applied (0.0 to 1.0)
        ('m_brake', ctypes.c_float),

        # Amount of clutch applied (0 to 100)
        ('m_clutch', ctypes.c_uint8),

        # Gear selected (1-8, N=0, R=-1)
        ('m_gear', ctypes.c_int8),

        # Engine RPM
        ('m_engine_rpm', ctypes.c_uint16),

        # 0 = off, 1 = on
        ('m_drs', ctypes.c_uint8),

        # Rev lights indicator (percentage)
        ('m_rev_lights_percent', ctypes.c_uint8),

        # Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
        ('m_rev_lights_bit_value', ctypes.c_uint16),

        # Brakes temperature (celsius)
        ('m_brakes_temperature', ctypes.c_uint16 * 4),

        # Tyres surface temperature (celsius)
        ('m_tyres_surface_temperature', ctypes.c_uint8 * 4),

        # Tyres inner temperature (celsius)
        ('m_tyres_inner_temperature', ctypes.c_uint8 * 4),

        # Engine temperature (celsius)
        ('m_engine_temperature', ctypes.c_uint16),

        # Tyres pressure (PSI)
        ('m_tyres_pressure', ctypes.c_float * 4),

        # Driving surface, see appendices
        ('m_surface_type', ctypes.c_uint8 * 4),
    ]


class PacketCarTelemetryData(Packet):
    _id_ = 6
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Car Telemetry data array
        ('m_car_telemetry_data', CarTelemetryData * 22),

        # Index of MFD panel open - 255 = MFD closed
        # Single player, race – 0 = Car setup, 1 = Pits
        # 2 = Damage, 3 =  Engine, 4 = Temperatures
        # May vary depending on game mode
        ('m_mfd_panel_index', ctypes.c_uint8),

        # See above
        ('m_mfd_panel_index_secondary_player', ctypes.c_uint8),

        # Suggested gear for the player (1-8)
        # 0 if no gear suggested
        ('m_suggested_gear', ctypes.c_int8),
    ]


class CarStatusData(Packet):
    _fields_ = [
        # Traction control - 0 = off, 1 = medium, 2 = full
        ('m_traction_control', ctypes.c_uint8),

        # 0 (off) - 1 (on)
        ('m_anti_lock_brakes', ctypes.c_uint8),

        # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        ('m_fuel_mix', ctypes.c_uint8),

        # Front brake bias (percentage)
        ('m_front_brake_bias', ctypes.c_uint8),

        # Pit limiter status - 0 = off, 1 = on
        ('m_pit_limiter_status', ctypes.c_uint8),

        # Current fuel mass
        ('m_fuel_in_tank', ctypes.c_float),

        # Fuel capacity
        ('m_fuel_capacity', ctypes.c_float),

        # Fuel remaining in terms of laps (value on MFD)
        ('m_fuel_remaining_laps', ctypes.c_float),

        # Cars max RPM, point of rev limiter
        ('m_max_rpm', ctypes.c_uint16),

        # Cars idle RPM
        ('m_idle_rpm', ctypes.c_uint16),

        # Maximum number of gears
        ('m_max_gears', ctypes.c_uint8),

        # 0 = not allowed, 1 = allowed
        ('m_drs_allowed', ctypes.c_uint8),

        # 0 = DRS not available, non-zero - DRS will be available
        # in [X] metres
        ('m_drs_activation_distance', ctypes.c_uint16),

        # F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1
        # 7 = inter, 8 = wet
        # F1 Classic - 9 = dry, 10 = wet
        # F2 – 11 = super soft, 12 = soft, 13 = medium, 14 = hard
        # 15 = wet
        ('m_actual_tyre_compound', ctypes.c_uint8),

        # F1 visual (can be different from actual compound)
        # 16 = soft, 17 = medium, 18 = hard, 7 = inter, 8 = wet
        # F1 Classic – same as above
        # F2 ‘19, 15 = wet, 19 – super soft, 20 = soft
        # 21 = medium , 22 = hard
        ('m_visual_tyre_compound', ctypes.c_uint8),

        # Age in laps of the current set of tyres
        ('m_tyres_age_laps', ctypes.c_uint8),

        # -1 = invalid/unknown, 0 = none, 1 = green
        # 2 = blue, 3 = yellow, 4 = red
        ('m_vehicle_fia_flags', ctypes.c_int8),

        # ERS energy store in Joules
        ('m_ers_store_energy', ctypes.c_float),

        # ERS deployment mode, 0 = none, 1 = medium
        # 2 = hotlap, 3 = overtake
        ('m_ers_deploy_mode', ctypes.c_uint8),

        # ERS energy harvested this lap by MGU-K
        ('m_ers_harvested_this_lap_mguk', ctypes.c_float),

        # ERS energy harvested this lap by MGU-H
        ('m_ers_harvested_this_lap_mguh', ctypes.c_float),

        # ERS energy deployed this lap
        ('m_ers_deployed_this_lap', ctypes.c_float),

        # Whether the car is paused in a network game
        ('m_network_paused', ctypes.c_uint8),
    ]


class PacketCarStatusData(Packet):
    _id_ = 7
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Car status data array
        ('m_car_status_data', CarStatusData * 22),
    ]


class FinalClassificationData(Packet):
    _fields_ = [
        # Finishing position
        ('m_position', ctypes.c_uint8),

        # Number of laps completed
        ('m_num_laps', ctypes.c_uint8),

        # Grid position of the car
        ('m_grid_position', ctypes.c_uint8),

        # Number of points scored
        ('m_points', ctypes.c_uint8),

        # Number of pit stops made
        ('m_num_pit_stops', ctypes.c_uint8),

        # Result status - 0 = invalid, 1 = inactive, 2 = active
        # 3 = finished, 4 = didnotfinish, 5 = disqualified
        # 6 = not classified, 7 = retired
        ('m_result_status', ctypes.c_uint8),

        # Best lap time of the session in milliseconds
        ('m_best_lap_time_in_ms', ctypes.c_uint32),

        # Total race time in seconds without penalties
        ('m_total_race_time', ctypes.c_double),

        # Total penalties accumulated in seconds
        ('m_penalties_time', ctypes.c_uint8),

        # Number of penalties applied to this driver
        ('m_num_penalties', ctypes.c_uint8),

        # Number of tyres stints up to maximum
        ('m_num_tyre_stints', ctypes.c_uint8),

        # Actual tyres used by this driver
        ('m_tyre_stints_actual', ctypes.c_uint8 * 8),

        # Visual tyres used by this driver
        ('m_tyre_stints_visual', ctypes.c_uint8 * 8),
    ]


class PacketFinalClassificationData(Packet):
    _id_ = 8
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Number of cars in the final classification
        ('m_num_cars', ctypes.c_uint8),

        # Classification data array
        ('m_classification_data', FinalClassificationData * 22),
    ]


class LobbyInfoData(Packet):
    _fields_ = [
        # Whether the vehicle is AI (1) or Human (0) controlled
        ('m_ai_controlled', ctypes.c_uint8),

        # Team id - see appendix (255 if no team currently selected)
        ('m_team_id', ctypes.c_uint8),

        # Nationality of the driver
        ('m_nationality', ctypes.c_uint8),

        # Name of participant in UTF-8 format – null terminated
        # Will be truncated with ... (U+2026) if too long
        ('m_name', ctypes.c_char * 48),

        # Car number of the player
        ('m_car_number', ctypes.c_uint8),

        # 0 = not ready, 1 = ready, 2 = spectating
        ('m_ready_status', ctypes.c_uint8),
    ]


class PacketLobbyInfoData(Packet):
    _id_ = 9
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Number of players in the lobby data
        ('m_num_players', ctypes.c_uint8),

        # Lobby info data array
        ('m_lobby_players', LobbyInfoData * 22),
    ]


class CarDamageData(Packet):
    _fields_ = [
        # Tyre wear (percentage)
        ('m_tyres_wear', ctypes.c_float * 4),

        # Tyre damage (percentage)
        ('m_tyres_damage', ctypes.c_uint8 * 4),

        # Brakes damage (percentage)
        ('m_brakes_damage', ctypes.c_uint8 * 4),

        # Front left wing damage (percentage)
        ('m_front_left_wing_damage', ctypes.c_uint8),

        # Front right wing damage (percentage)
        ('m_front_right_wing_damage', ctypes.c_uint8),

        # Rear wing damage (percentage)
        ('m_rear_wing_damage', ctypes.c_uint8),

        # Floor damage (percentage)
        ('m_floor_damage', ctypes.c_uint8),
        # Diffuser damage (percentage)
        ('m_diffuser_damage', ctypes.c_uint8),

        # Sidepod damage (percentage)
        ('m_sidepod_damage', ctypes.c_uint8),

        # Indicator for DRS fault, 0 = OK, 1 = fault
        ('m_drs_fault', ctypes.c_uint8),

        # Gear box damage (percentage)
        ('m_gear_box_damage', ctypes.c_uint8),

        # Engine damage (percentage)
        ('m_engine_damage', ctypes.c_uint8),

        # Engine wear MGU-H (percentage)
        ('m_engine_mguhwear', ctypes.c_uint8),

        # Engine wear ES (percentage)
        ('m_engine_eswear', ctypes.c_uint8),

        # Engine wear CE (percentage)
        ('m_engine_cewear', ctypes.c_uint8),

        # Engine wear ICE (percentage)
        ('m_engine_icewear', ctypes.c_uint8),

        # Engine wear MGU-K (percentage)
        ('m_engine_mgukwear', ctypes.c_uint8),

        # Engine wear TC (percentage)
        ('m_engine_tcwear', ctypes.c_uint8),
    ]


class PacketCarDamageData(Packet):
    _id_ = 10
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Car damage data array
        ('m_car_damage_data', CarDamageData * 22),
    ]


class LapHistoryData(Packet):
    _fields_ = [
        # Lap time in milliseconds
        ('m_lap_time_in_ms', ctypes.c_uint32),

        # Sector 1 time in milliseconds
        ('m_sector1_time_in_ms', ctypes.c_uint16),

        # Sector 2 time in milliseconds
        ('m_sector2_time_in_ms', ctypes.c_uint16),

        # Sector 3 time in milliseconds
        ('m_sector3_time_in_ms', ctypes.c_uint16),

        # 0x01 bit set-lap valid,      0x02 bit set-sector 1 valid
        # 0x04 bit set-sector 2 valid, 0x08 bit set-sector 3 valid
        ('m_lap_valid_bit_flags', ctypes.c_uint8),
    ]


class TyreStintHistoryData(Packet):
    _fields_ = [
        # Lap the tyre usage ends on (255 of current tyre)
        ('m_end_lap', ctypes.c_uint8),

        # Actual tyres used by this driver
        ('m_tyre_actual_compound', ctypes.c_uint8),

        # Visual tyres used by this driver
        ('m_tyre_visual_compound', ctypes.c_uint8),
    ]


class PacketSessionHistoryData(Packet):
    _id_ = 11
    _fields_ = [
        # Header
        ('m_header', PacketHeader),

        # Index of the car this lap data relates to
        ('m_car_idx', ctypes.c_uint8),

        # Num laps in the data (including current partial lap)
        ('m_num_laps', ctypes.c_uint8),

        # Number of tyre stints in the data
        ('m_num_tyre_stints', ctypes.c_uint8),

        # Lap the best lap time was achieved on
        ('m_best_lap_time_lap_num', ctypes.c_uint8),

        # Lap the best Sector 1 time was achieved on
        ('m_best_sector1_lap_num', ctypes.c_uint8),

        # Lap the best Sector 2 time was achieved on
        ('m_best_sector2_lap_num', ctypes.c_uint8),

        # Lap the best Sector 3 time was achieved on
        ('m_best_sector3_lap_num', ctypes.c_uint8),

        # 100 laps of data max
        ('m_lap_history_data', LapHistoryData * 100),

        # Tyre stints history array
        ('m_tyre_stints_history_data', TyreStintHistoryData * 8),
    ]
