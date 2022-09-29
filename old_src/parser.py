import pathlib
import typing

from neptune_f1.packets.codemasters_f12021.utils import Packet

from .factory import PacketFactory


class Parser:
    @classmethod
    def from_file(cls, filepath: pathlib.Path | str) -> typing.Generator[None, Packet, None]:
        with open(filepath, "rb") as handler:
            while packet := PacketFactory.from_handler(handler):
                yield packet
