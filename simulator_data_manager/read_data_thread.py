import time
from threading import Thread

from cnc.cnc import Cnc
from connections.device_disconnected_exception import DeviceDisconnectedException
from simulator_data_manager.packet_type import PacketType


class ReadDataThread(Thread):
    def __init__(self):
        super().__init__()
        self._cnc = Cnc()

    def run(self) -> None:
        while True:
            time.sleep(0.001)
            if self._cnc.connection and self._cnc.connection.is_connected:
                try:
                    packet_type, payload = self._cnc.parse_incoming_packet()
                    if packet_type in PacketType.__dict__:
                        PacketType[packet_type].value.save(payload)
                    else:
                        print(f'Unknown packet type: {packet_type}, payload: {payload}')
                except DeviceDisconnectedException:
                    self._cnc.connection.disconnect()
