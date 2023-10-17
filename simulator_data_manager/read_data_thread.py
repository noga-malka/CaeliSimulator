import time
from threading import Thread

from cnc.cnc import Cnc
from simulator_data_manager.packet_type import PacketType


class ReadDataThread(Thread):
    def __init__(self):
        super().__init__()
        self.cnc = Cnc()

    def run(self) -> None:
        while True:
            time.sleep(0.001)
            if self.cnc.connection and self.cnc.connection.is_connected:
                packet_type, payload = self.cnc.parse_incoming_packet()
                PacketType[packet_type].value.save(payload)
