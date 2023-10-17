from simulator_data_manager.read_data_thread import ReadDataThread
from singleton import Singleton


class SimulatorDataManager(Singleton):
    def initiate(self):
        self.read_data_thread = ReadDataThread()
        self.read_data_thread.start()
