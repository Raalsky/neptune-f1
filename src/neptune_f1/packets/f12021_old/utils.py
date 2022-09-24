import ctypes
import json


def to_json(*args, **kwargs):
    kwargs.setdefault("indent", 2)

    kwargs["sort_keys"] = True
    kwargs["ensure_ascii"] = False
    kwargs["separators"] = (",", ": ")

    return json.dumps(*args, **kwargs)


class PacketMixin:
    def get_value(self: ctypes.Structure, field):
        """Returns the field's value and formats the types value"""
        return self._format_type(getattr(self, field))

    def pack(self: ctypes.Structure):
        """Packs the current data structure into a compressed binary

        Returns:
            (bytes):
                - The packed binary

        """
        return bytes(self)

    @classmethod
    def size(cls: ctypes.Structure):
        return ctypes.sizeof(cls)

    @classmethod
    def unpack(cls: ctypes.Structure, buffer):
        """Attempts to unpack the binary structure into a python structure

        Args:
            buffer (bytes):
                - The encoded buffer to decode

        """
        return cls.from_buffer_copy(buffer)

    def to_dict(self: ctypes.Structure):
        """Returns a ``dict`` with key-values derived from _fields_"""
        return {k: self.get_value(k) for k, _ in self._fields_}

    def to_json(self: ctypes.Structure):
        """Returns a ``str`` of sorted JSON derived from _fields_"""
        return to_json(self.to_dict())

    def _format_type(self: ctypes.Structure, value):
        """A type helper to format values"""
        class_name = type(value).__name__

        if class_name == "float":
            return round(value, 3)

        if class_name == "bytes":
            # return value.decode()
            return list(map(int, value))

        if isinstance(value, ctypes.Array):
            return self._format_array_type(value)

        if hasattr(value, "to_dict"):
            return value.to_dict()

        return value

    def _format_array_type(self: ctypes.Structure, value):
        results = []

        for item in value:
            if isinstance(item, Packet):
                results.append(item.to_dict())
            else:
                results.append(item)

        return results

    def __repr__(self: ctypes.Structure):
        return self.to_json()


class Packet(ctypes.LittleEndianStructure, PacketMixin):
    """The base packet class for API version 2021"""

    _pack_ = 1
    _id_ = None
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
