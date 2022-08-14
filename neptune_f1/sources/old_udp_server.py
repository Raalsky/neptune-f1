import json
import random
import socket
import time


def main():
    localIP = "192.168.0.24"
    localPort = 20777
    bufferSize = 1024 * 16

    _socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    _socket.bind((localIP, localPort))
    print("UDP server up and listening")

    with open(f"../data/sample_10hz.{random.randint(1, 1000)}.bin", "wb+") as handler:
        while True:
            try:
                message, address = _socket.recvfrom(bufferSize)

                handler.write(message)

                # ACK
                _socket.sendto(
                    json.dumps({"type": "connect", "time": time.time(), "connection": True}).encode(), address
                )
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    main()
