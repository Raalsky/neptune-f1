from neptune_f1.packets.codemasters_f12021.packet_car_damage_data import PacketCarDamageData
from neptune_f1.packets.codemasters_f12021.packet_car_setup_data import PacketCarSetupData
from neptune_f1.packets.codemasters_f12021.packet_car_status_data import PacketCarStatusData
from neptune_f1.packets.codemasters_f12021.packet_car_telemetry_data import PacketCarTelemetryData
from neptune_f1.packets.codemasters_f12021.packet_event_data import PacketEventData
from neptune_f1.packets.codemasters_f12021.packet_final_classification_data import PacketFinalClassificationData
from neptune_f1.packets.codemasters_f12021.packet_header import PacketHeader
from neptune_f1.packets.codemasters_f12021.packet_lap_data import PacketLapData
from neptune_f1.packets.codemasters_f12021.packet_lobby_info_data import PacketLobbyInfoData
from neptune_f1.packets.codemasters_f12021.packet_motion_data import PacketMotionData
from neptune_f1.packets.codemasters_f12021.packet_participant_data import PacketParticipantsData
from neptune_f1.packets.codemasters_f12021.packet_session_data import PacketSessionData
from neptune_f1.packets.codemasters_f12021.packet_session_history_data import PacketSessionHistoryData


def main():
    packet_motion_data = open("rjankowski_output/packet_motion_data.jsonl", "w")
    packet_session_data = open("rjankowski_output/packet_session_data.jsonl", "w")
    packet_lap_data = open("rjankowski_output/packet_lap_data.jsonl", "w")
    packet_event_data = open("rjankowski_output/packet_event_data.jsonl", "w")
    packet_participants_data = open("rjankowski_output/packet_participants_data.jsonl", "w")
    packet_car_setup_data = open("rjankowski_output/packet_car_setup_data.jsonl", "w")
    packet_car_telemetry_data = open("rjankowski_output/packet_car_telemetry_data.jsonl", "w")
    packet_car_status_data = open("rjankowski_output/packet_car_status_data.jsonl", "w")
    packet_final_classification_data = open("rjankowski_output/packet_final_classification_data.jsonl", "w")
    packet_lobby_info_data = open("rjankowski_output/packet_lobby_info_data.jsonl", "w")
    packet_car_damage_data = open("rjankowski_output/packet_car_damage_data.jsonl", "w")
    packet_session_history_data = open("rjankowski_output/packet_session_history_data.jsonl", "w")

    errors = 0

    with open("rjankowski_samples/sample.bytesl") as handler:
        data = handler.readlines()
        for index, line in enumerate(data):
            dd = bytes(list(map(lambda r: int(r, base=16), line.split("\\x")[1:])))

            try:
                header = PacketHeader.unpack(dd)

                if header.m_packet_id == 0:
                    www = PacketMotionData.unpack(dd)
                    packet_motion_data.write(str(www) + "\n")

                if header.m_packet_id == 1:
                    www = PacketSessionData.unpack(dd)
                    packet_session_data.write(str(www) + "\n")

                if header.m_packet_id == 2:
                    www = PacketLapData.unpack(dd)
                    packet_lap_data.write(str(www) + "\n")

                if header.m_packet_id == 3:
                    www = PacketEventData.unpack(dd)
                    packet_event_data.write(str(www) + "\n")

                if header.m_packet_id == 4:
                    www = PacketParticipantsData.unpack(dd)
                    packet_participants_data.write(str(www) + "\n")

                if header.m_packet_id == 5:
                    www = PacketCarSetupData.unpack(dd)
                    packet_car_setup_data.write(str(www) + "\n")

                if header.m_packet_id == 6:
                    www = PacketCarTelemetryData.unpack(dd)
                    packet_car_telemetry_data.write(str(www) + "\n")

                if header.m_packet_id == 7:
                    www = PacketCarStatusData.unpack(dd)
                    packet_car_status_data.write(str(www) + "\n")

                if header.m_packet_id == 8:
                    www = PacketFinalClassificationData.unpack(dd)
                    packet_final_classification_data.write(str(www) + "\n")

                if header.m_packet_id == 9:
                    www = PacketLobbyInfoData.unpack(dd)
                    packet_lobby_info_data.write(str(www) + "\n")

                if header.m_packet_id == 10:
                    www = PacketCarDamageData.unpack(dd)
                    packet_car_damage_data.write(str(www) + "\n")

                if header.m_packet_id == 11:
                    www = PacketSessionHistoryData.unpack(dd)
                    packet_session_history_data.write(str(www) + "\n")
            except ValueError:
                errors += 1
                continue

            if index % 1000 == 0:
                print(index)

    print("Errors: #", errors)

    packet_motion_data.close()
    packet_session_data.close()
    packet_lap_data.close()
    packet_event_data.close()
    packet_participants_data.close()
    packet_car_setup_data.close()
    packet_car_telemetry_data.close()
    packet_car_status_data.close()
    packet_final_classification_data.close()
    packet_lobby_info_data.close()
    packet_car_damage_data.close()
    packet_session_history_data.close()


if __name__ == "__main__":
    main()
