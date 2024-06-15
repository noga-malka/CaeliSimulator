from typing import Any

import pandas

from cnc.bluetooth_cnc import BluetoothCnc
from cnc.serial_cnc import SerialCnc
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
        self.packet_parsers = {
            PacketHeaders.BREATH_PARAMETERS: BreathParametersPacketParser(),
            PacketHeaders.ACTIVE_BREATH_PARAMETERS: DictionaryPacketParser(),
            PacketHeaders.SIMULATOR: IntegerDataframePacketParser(),
            PacketHeaders.CRUESO: FloatDataframePacketParser(),
            PacketHeaders.PRESSURE: FloatDataframePacketParser(),
        }
        self.simulator_thread = ReadDataThread(SerialCnc(), self.packet_parsers)
        self.simulator_thread.start()
        self.crueso_thread = ReadDataThread(BluetoothCnc(), self.packet_parsers)
        self.crueso_thread.start()

    def get_data(self, packet_type: str) -> Any:
        """
        :param packet_type: key inside self._packet_parsers
        :return: saved data of the right packet parser
        """
        return self.packet_parsers[packet_type].get_saved_data()

    def get_live_dataframe(self) -> pandas.DataFrame:
        crueso_data = self.get_data(PacketHeaders.CRUESO)
        pressure_data = self.get_data(PacketHeaders.PRESSURE)
        simulator_data = self.get_data(PacketHeaders.SIMULATOR)
        return pandas.concat([crueso_data, simulator_data, pressure_data], axis=1)

    def get_event(self, packet_type: str):
        """
        :param packet_type: key inside self._packet_parsers
        :return: Event object of the right packet parser
        """
        return self.packet_parsers[packet_type].get_event()
