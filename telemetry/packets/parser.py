import typing
import pathlib

from telemetry.packets.factory import PacketFactory
from telemetry.packets.f12021.utils import Packet


class Parser:
    @classmethod
    def from_file(cls, filepath: typing.Union[pathlib.Path, str]) -> typing.Generator[None, Packet, None]:
        with open(filepath, "rb") as handler:
            while packet := PacketFactory.from_handler(handler):
                yield packet
