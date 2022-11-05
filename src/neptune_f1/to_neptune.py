import json

from neptune_f1.metric_over_lap_period import MetricOverLapPeriod

# if full? then call observer
# then log to Neptune all lap data, maybe on timeout or full-filled state


# "Done" as a already emitted data to reject any new metric data
# List of Laps where every lap is a dict with MetricOverLapPeriod


def packet_motion_data():
    arr = []

    with open("rjankowski_output/packet_car_telemetry_data.jsonl") as handler:
        for line in handler.readlines():
            packet = json.loads(line)

            header = packet.get("m_header")
            car_telemetry_data = packet.get("m_car_telemetry_data")

            arr.append(
                {
                    "session_time": header.get("m_session_time"),
                    "frame_identifier": header.get("m_frame_identifier"),
                    "speed": car_telemetry_data[0].get("m_speed"),
                    "throttle": car_telemetry_data[0].get("m_throttle"),
                    "steer": car_telemetry_data[0].get("m_steer"),
                    "brake": car_telemetry_data[0].get("m_brake"),
                    "clutch": car_telemetry_data[0].get("m_clutch"),
                    "gear": car_telemetry_data[0].get("m_gear"),
                    "engine_rpm": car_telemetry_data[0].get("m_engine_temperature"),
                    "engine_temperature": car_telemetry_data[0].get("m_engine_temperature"),
                }
            )

    return sorted(arr, key=lambda x: x["session_time"])


def packet_lap_data():
    arr = []
    with open("rjankowski_output/packet_lap_data.jsonl") as handler:
        for line in handler.readlines():
            packet = json.loads(line)

            header = packet.get("m_header")
            lap_data = packet.get("m_lap_data")[0]

            arr.append(
                {
                    "session_time": header.get("m_session_time"),
                    "frame_identifier": header.get("m_frame_identifier"),
                    "lap": lap_data.get("m_current_lap_num"),
                    "car_position": lap_data.get("m_car_position"),
                    "grid_position": lap_data.get("m_grid_position"),
                    "lap_distance": lap_data.get("m_lap_distance"),
                }
            )
            break

    return sorted(arr, key=lambda x: x["session_time"])


def log_motion_metrics(run, lap_indices):
    packets = packet_motion_data()
    metrics = {
        "speed": MetricOverLapPeriod(name="Speed", lap_length=1500, resolution=10),
        "throttle": MetricOverLapPeriod(name="Throttle", lap_length=1500, resolution=10),
        "steer": MetricOverLapPeriod(name="Steer", lap_length=1500, resolution=10),
        "brake": MetricOverLapPeriod(name="Brake", lap_length=1500, resolution=10),
        "clutch": MetricOverLapPeriod(name="Clutch", lap_length=1500, resolution=10),
        "gear": MetricOverLapPeriod(name="Gear", lap_length=1500, resolution=10),
        "engine_temperature": MetricOverLapPeriod(name="Engine Temperature", lap_length=1500, resolution=10),
    }
    for packet in packets:
        for metric_name in metrics:
            metrics[metric_name].log(at_distance=packet["session_time"], value=packet[metric_name])

    for metric_name in metrics:
        run[metric_name].log(metrics[metric_name].result()[lap_indices].tolist())


def log_lap_metrics(run):
    packets = packet_lap_data()
    metrics = {
        "lap": MetricOverLapPeriod(name="Lap", lap_length=5000, resolution=10),
        # "car_position": MetricOverLapPeriod(name="Car Position", lap_length=5000, resolution=10),
        # "grid_position": MetricOverLapPeriod(name="Grid Position", lap_length=5000, resolution=10),
        # "lap_distance": MetricOverLapPeriod(name="Lap Distance", lap_length=5000, resolution=10),
    }
    for packet in packets:
        for metric_name in metrics:
            metrics[metric_name].log(at_distance=packet["session_time"], value=packet[metric_name])

    print(metrics["lap"].result()[:2], len(metrics["lap"].result()))

    # lap_indices = np.where(metrics['lap'].result() == 2)
    #
    # for metric_name in metrics:
    #     run[metric_name].log(
    #         metrics[metric_name].result().tolist()
    #     )
    #
    # return lap_indices


if __name__ == "__main__":
    # with neptune.init_run(
    #     capture_stdout=False,
    #     capture_stderr=False,
    #     capture_hardware_metrics=False,
    #     capture_traceback=False
    # ) as run:
    lap_indices = log_lap_metrics(None)
    # log_motion_metrics(run, lap_indices)
