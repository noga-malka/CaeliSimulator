from simulator_data_manager.read_data_thread import ReadDataThread
from singleton import Singleton


class SimulatorDataManager(Singleton):
    def initiate(self):
        self._read_data_thread = ReadDataThread()
        self._read_data_thread.start()

    def get_data(self, packet_type: str):
        return self._read_data_thread.get_data(packet_type)

    def get_event(self, packet_type: str):
        return self._read_data_thread.get_event(packet_type)

    def clear_saved_data(self):
        self._read_data_thread.clear_saved_data()
