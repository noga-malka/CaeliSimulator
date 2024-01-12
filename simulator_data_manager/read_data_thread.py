import time
from threading import Thread

from cnc.cnc import Cnc
from connections.device_disconnected_exception import DeviceDisconnectedException
from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class ReadDataThread(Thread):
    """
    Thread that saves the received data from the simulator
    """

    def __init__(self, cnc_module: Cnc, packet_parsers: dict[str, BasePacketParser]):
        super().__init__()
        self._cnc = cnc_module
        # maps between the packet header and the  parser to use to save the packet's data
        self.packet_parsers = packet_parsers

    def clear_saved_data(self):
        """
        clear all parsers' saved data
        """
        time.sleep(0.1)
        for parser in self.packet_parsers.values():
            parser.clear_saved_data()

    def _save_incoming_packet(self):
        """
        extract the next packet from CNC
        if there is a valid packet parser, save the new packet, else log the unknown packet
        :raises: DeviceDisconnectedException if CNC connection is closed
        """
        packet_type, payload = self._cnc.parse_incoming_packet()
        if packet_type in self.packet_parsers:
            self.packet_parsers[packet_type].save(payload)
        else:
            print(f'Unknown packet type: {packet_type}, payload: {payload}')

    def run(self) -> None:
        while True:
            time.sleep(0.001)
            if self._cnc.is_connected:
                try:
                    self._save_incoming_packet()
                except DeviceDisconnectedException:
                    self._cnc.connection.disconnect()
