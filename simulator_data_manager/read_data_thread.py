import time
from threading import Thread

from cnc.cnc import Cnc
from connections.device_disconnected_exception import DeviceDisconnectedException
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser
from simulator_data_manager.packet_type_parsers.data_packet_parser import DataframePacketParser
from simulator_data_manager.packet_type_parsers.dictionary_packet_parser import DictionaryPacketParser
from simulator_data_manager.packet_type_parsers.profile_packet_parser import ProfilePacketParser


class ReadDataThread(Thread):
    def __init__(self):
        super().__init__()
        self._cnc = Cnc()
        self._parsers: dict[str, BasePacketParser] = {
            PacketHeaders.DATA: DataframePacketParser(),
            PacketHeaders.BREATH_PARAMS: ProfilePacketParser(),
            PacketHeaders.ACTIVE_BREATH_PARAMS: DictionaryPacketParser(),
        }

    def clear_saved_data(self):
        time.sleep(0.1)
        for parser in self._parsers.values():
            parser.clear()

    def get_data(self, packet_type: str):
        return self._parsers[packet_type].saved_data

    def get_event(self, packet_type: str):
        return self._parsers[packet_type].event

    def run(self) -> None:
        while True:
            time.sleep(0.001)
            if self._cnc.is_connected:
                try:
                    packet_type, payload = self._cnc.parse_incoming_packet()
                    if packet_type in self._parsers:
                        self._parsers[packet_type].save(payload)
                    else:
                        print(f'Unknown packet type: {packet_type}, payload: {payload}')
                except DeviceDisconnectedException:
                    self._cnc.connection.disconnect()
