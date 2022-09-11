import asyncio
import datetime

from aioudp import UDPServer


class MyUDPServer:
    def __init__(self, server, loop):
        self.server = server
        self.loop = loop
        # Subscribe for incoming udp packet event
        self.server.subscribe(self.on_datagram_received)
        asyncio.ensure_future(self.do_send(), loop=self.loop)

    async def on_datagram_received(self, data, addr):
        # Override virtual method and process incoming data
        print(datetime.datetime.now(), addr, data)

    async def do_send(self):
        while True:
            # Any payload
            payload = (
                b"d1:ad2:id20:k\xe7\x90\xcd\x0c_R\xfe\x82\xeb\xa8 x\x14\xb4-\x8e0\xe5\x086:target20:"
                b"\x11\x8e\xcc,\x89\xa4\x99\xf98E\x98\x7f!\xa7w\rz\x1b\x14de1:q9:find_node1:t2:#K1:y1:qe"
            )
            # Delay for prevent tasks concurency
            await asyncio.sleep(0.001)
            # Enqueue data for send
            self.server.send(payload, ("router.bittorrent.com", 6881))


async def main(loop):
    # Bandwidth speed is 100 bytes per second
    udp = UDPServer(download_speed=100, upload_speed=100)
    udp.run("0.0.0.0", 12346, loop=loop)

    MyUDPServer(server=udp, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
