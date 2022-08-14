from f1_2021.packets import Parser


class TestParser:
    def test_simple(self):
        packets = list(Parser.from_file("data/sample_packets/03_event.bin"))
        assert type(packets[0]).__name__ == "PacketEventData"
