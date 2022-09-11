import pathlib
import typing

from telemetry.packets.f12021.utils import Packet
from telemetry.packets.factory import PacketFactory


class Parser:
    @classmethod
    def from_file(cls, filepath: pathlib.Path | str) -> typing.Generator[None, Packet, None]:
        with open(filepath, "rb") as handler:
            while packet := PacketFactory.from_handler(handler):
                yield packet
