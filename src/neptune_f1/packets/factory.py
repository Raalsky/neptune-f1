import typing

from neptune_f1.packets.f12021.packet_header import PacketHeader
from neptune_f1.packets.f12021.utils import Packet


class PacketFactory:
    @staticmethod
    def header_size() -> int:
        return PacketHeader.size()

    @staticmethod
    def packet_identifiers() -> typing.Mapping[tuple[int, int, int], Packet.__class__]:
        return {
            (
                # Packet format
                packet_cls.get_format(),
                # Packet type id
                packet_cls.get_identifier(),
                # Packet type version
                packet_cls.get_version(),
            ): packet_cls
            for packet_cls in Packet.__subclasses__()
            if packet_cls.get_identifier() is not None
        }

    @classmethod
    def from_handler(cls, handler) -> None | Packet:
        if raw_header_data := handler.read(PacketFactory.header_size()):
            packet_header_data = bytearray(raw_header_data)
            header = PacketHeader.unpack(packet_header_data)

            packet_type_id = header.m_packet_id
            packet_type_version = header.m_packet_version
            packet_format = header.m_packet_format

            packet_cls = PacketFactory.packet_identifiers().get((packet_format, packet_type_id, packet_type_version))

            assert (
                packet_cls
            ), f"Packet spec (format={packet_format}, id={packet_type_id}, version={packet_type_version}) unknown"

            raw_packet_data = handler.read(packet_cls.size() - PacketFactory.header_size())
            packet_data = bytearray(raw_packet_data)

            return packet_cls.unpack(packet_header_data + packet_data)
