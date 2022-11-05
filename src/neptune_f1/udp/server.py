import json
import socketserver
import time
from dataclasses import dataclass


@dataclass
class ServerConfig:
    host: str = "localhost"
    port: int = 20777


class ServerRequestHandler(socketserver.DatagramRequestHandler):
    def setup(self) -> None:
        pass

    @property
    def _ack_message(self) -> dict:
        return {"type": "connect", "time": time.time(), "connection": True}

    def _send_ack(self) -> None:
        self.wfile.write(json.dumps(self._ack_message).encode())

    def handle(self) -> None:
        data = self.rfile.readline().strip()

        print(f"{self.client_address[0]} wrote:")
        print(data)

        self._send_ack()

    def finish(self) -> None:
        pass


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
