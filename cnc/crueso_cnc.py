from cnc.cnc import Cnc
from connections.bluetooth_connection import BluetoothConnection
from singleton import Singleton


class CruesoCnc(Cnc, Singleton):
    def initiate(self):
        self.connection = BluetoothConnection()
