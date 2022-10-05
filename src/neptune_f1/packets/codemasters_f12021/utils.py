import ctypes
import json

__all__ = ["Packet", "PacketDataBunch"]


def to_json(*args, **kwargs):
    kwargs.setdefault("indent", 2)

    kwargs["sort_keys"] = True
    kwargs["ensure_ascii"] = False
    kwargs["separators"] = (",", ": ")

    return json.dumps(*args, **kwargs)


def format_array_type(value):
    results = []

    for item in value:
        if isinstance(item, Packet):
            results.append(item.to_dict())
        else:
            results.append(item)

    return results


def format_type(value):
    """A type helper to format values"""
    class_name = type(value).__name__

    if class_name == "float":
        return round(value, 3)

    if class_name == "bytes":
        return value.decode()

    if isinstance(value, ctypes.Array):
        return format_array_type(value)

    if hasattr(value, "to_dict"):
        return value.to_dict()

    return value


class PacketDataBunch:
    def get_value(self, field):
        """Returns the field's value and formats the types value"""
        return format_type(getattr(self, field))

    def pack(self):
        """Packs the current data structure into a compressed binary

        Returns:
            (bytes):
                - The packed binary

        """
        return bytes(self)

    @classmethod
    def size(cls):
        return ctypes.sizeof(cls)

    @classmethod
    def unpack(cls, buffer):
        """Attempts to unpack the binary structure into a python structure

        Args:
            buffer (bytes):
                - The encoded buffer to decode

        """
        return cls.from_buffer_copy(buffer)

    def to_dict(self):
        """Returns a ``dict`` with key-values derived from _fields_"""
        return {k: self.get_value(k) for k, _ in self._fields_}

    def to_json(self):
        """Returns a ``str`` of sorted JSON derived from _fields_"""
        return to_json(self.to_dict())

    def __repr__(self):
        return self.to_json()


class Packet(ctypes.LittleEndianStructure, PacketDataBunch):
    _pack_ = 1
    _id_ = -1
    _version_ = 1
    _format_ = 2021

    @classmethod
    def get_identifier(cls) -> None | int:
        return cls._id_

    @classmethod
    def get_version(cls) -> int:
        return cls._version_

    @classmethod
    def get_format(cls) -> int:
        return cls._format_
