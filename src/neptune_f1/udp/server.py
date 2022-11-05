import json
import socketserver
import time
from dataclasses import dataclass


@dataclass
class ServerConfig:
    host: str = "192.168.0.25"
    port: int = 20777


class ServerRequestHandler(socketserver.DatagramRequestHandler):
    @property
    def _ack_message(self) -> dict:
        return {"type": "connect", "time": time.time(), "connection": True}

    def _send_ack(self) -> None:
        self.wfile.write(json.dumps(self._ack_message).encode())

    def handle(self) -> None:
        print(f"Received packet from '{self.client_address[0]}'")

        data = self.rfile.readline().strip()

        with open("session_data/packets-{}.bytes".format(str(time.time()).replace(".", "")), "w") as handler:
            handler.write("".join(f"\\x{x:02x}" for x in data) + "\n")

        self._send_ack()


class Server(socketserver.UDPServer):
    def __init__(self, config: ServerConfig = None):
        if not config:
            config = ServerConfig()
        self._config = config

        super().__init__(
            server_address=(self._config.host, self._config.port), RequestHandlerClass=ServerRequestHandler
        )


def main():
    with Server() as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
