from cnc.cnc import Cnc
from connections.serial_connection import SerialConnection
from singleton import Singleton


class SimulatorCnc(Cnc, Singleton):
    def initiate(self):
        self.connection = SerialConnection()
