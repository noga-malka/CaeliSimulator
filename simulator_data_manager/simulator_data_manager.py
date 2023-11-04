from typing import Any

from simulator_data_manager.read_data_thread import ReadDataThread
from singleton import Singleton


class SimulatorDataManager(Singleton):
    """
    Manager for received data from the simulator
    A singleton class to support multiple imports
    """

    def initiate(self):
        self._read_data_thread = ReadDataThread()
        self._read_data_thread.start()

    def get_data(self, packet_type: str) -> Any:
        """
        :param packet_type: key inside self._packet_parsers
        :return: saved data of the right packet parser
        """
        return self._read_data_thread.get_data(packet_type)

    def get_event(self, packet_type: str):
        """
        :param packet_type: key inside self._packet_parsers
        :return: Event object of the right packet parser
        """
        return self._read_data_thread.get_event(packet_type)

    def clear_saved_data(self):
        """
        clear all parsers' saved data
        """
        self._read_data_thread.clear_saved_data()
