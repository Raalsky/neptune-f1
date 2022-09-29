import sys

from telemetry.packets.parser import Parser


def main(filepath):
    for packet in Parser.from_file(filepath=filepath):
        print(type(packet).__name__)


if __name__ == "__main__":
    main(filepath=sys.argv[1])
