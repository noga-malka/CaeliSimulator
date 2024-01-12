from typing import Any

from cnc.crueso_cnc import CruesoCnc
from cnc.simulator_cnc import SimulatorCnc
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.packet_type_parsers.breath_parameters_packet_parser import BreathParametersPacketParser
from simulator_data_manager.packet_type_parsers.dictionary_packet_parser import DictionaryPacketParser
from simulator_data_manager.packet_type_parsers.float_dataframe_packet_parser import FloatDataframePacketParser
from simulator_data_manager.packet_type_parsers.integer_dataframe_packet_parser import IntegerDataframePacketParser
from simulator_data_manager.read_data_thread import ReadDataThread
from singleton import Singleton


class SimulatorDataManager(Singleton):
    """
    Manager for received data from the simulator
    A singleton class to support multiple imports
    """

    def initiate(self):
        self.simulator_thread = ReadDataThread(SimulatorCnc(),
                                               {
                                                   PacketHeaders.DATA: IntegerDataframePacketParser(100),
                                                   PacketHeaders.BREATH_PARAMETERS: BreathParametersPacketParser(),
                                                   PacketHeaders.ACTIVE_BREATH_PARAMETERS: DictionaryPacketParser(),
                                               })
        self.simulator_thread.start()
        self.crueso_thread = ReadDataThread(CruesoCnc(),
                                            {
                                                PacketHeaders.CRUESO: FloatDataframePacketParser(100),
                                            })
        self.crueso_thread.start()

        self._all_packet_parsers = self.simulator_thread.packet_parsers | self.crueso_thread.packet_parsers

    def get_data(self, packet_type: str) -> Any:
        """
        :param packet_type: key inside self._packet_parsers
        :return: saved data of the right packet parser
        """
        return self._all_packet_parsers[packet_type].get_saved_data()

    def get_event(self, packet_type: str):
        """
        :param packet_type: key inside self._packet_parsers
        :return: Event object of the right packet parser
        """
        return self._all_packet_parsers[packet_type].get_event()
