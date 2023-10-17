import time
from threading import Thread

from cnc.cnc import Cnc
from simulator_data_manager.packet_type import PacketType


class ReadDataThread(Thread):
    def __init__(self):
        super().__init__()
        self._cnc = Cnc()

    def run(self) -> None:
        while True:
            time.sleep(0.001)
            if self._cnc.connection and self._cnc.connection.is_connected:
                packet_type, payload = self._cnc.parse_incoming_packet()
                PacketType[packet_type].value.save(payload)
