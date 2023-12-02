import time
from threading import Thread, Event
from typing import Any

from cnc.cnc import Cnc
from connections.device_disconnected_exception import DeviceDisconnectedException
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser
from simulator_data_manager.packet_type_parsers.breath_parameters_packet_parser import BreathParametersPacketParser
from simulator_data_manager.packet_type_parsers.dictionary_packet_parser import DictionaryPacketParser
from simulator_data_manager.packet_type_parsers.numeric_dataframe_packet_parser import NumericDataframePacketParser


class ReadDataThread(Thread):
    """
    Thread that saves the received data from the simulator
    """

    def __init__(self):
        super().__init__()
        self._cnc = Cnc()
        # maps between the packet header and the  parser to use to save the packet's data
        self._packet_parsers: dict[str, BasePacketParser] = {
            PacketHeaders.DATA: NumericDataframePacketParser(1000),
            PacketHeaders.BREATH_PARAMETERS: BreathParametersPacketParser(),
            PacketHeaders.ACTIVE_BREATH_PARAMETERS: DictionaryPacketParser(),
        }

    def clear_saved_data(self):
        """
        clear all parsers' saved data
        """
        time.sleep(0.1)
        for parser in self._packet_parsers.values():
            parser.clear_saved_data()

    def get_data(self, packet_type: str) -> Any:
        """
        :param packet_type: key inside self._packet_parsers
        :return: saved data of the right packet parser
        """
        return self._packet_parsers[packet_type].get_saved_data()

    def get_event(self, packet_type: str) -> Event:
        """
        :param packet_type: key inside self._packet_parsers
        :return: Event object of the right packet parser
        """
        return self._packet_parsers[packet_type].get_event()

    def _save_incoming_packet(self):
        """
        extract the next packet from CNC
        if there is a valid packet parser, save the new packet, else log the unknown packet
        :raises: DeviceDisconnectedException if CNC connection is closed
        """
        packet_type, payload = self._cnc.parse_incoming_packet()
        try:
            if packet_type in self._packet_parsers:
                self._packet_parsers[packet_type].save(payload)
            else:
                print(f'Unknown packet type: {packet_type}, payload: {payload}')
        except AttributeError:
            print(f'Attribute Error: {packet_type}, payload: {payload}')

    def run(self) -> None:
        while True:
            time.sleep(0.001)
            if self._cnc.is_connected:
                try:
                    self._save_incoming_packet()
                except DeviceDisconnectedException:
                    self._cnc.connection.disconnect()
