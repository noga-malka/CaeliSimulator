from cnc.cnc import Cnc
from connections.serial_connection import SerialConnection


class SerialCnc(Cnc):
    def initiate(self):
        self.connection = SerialConnection()
