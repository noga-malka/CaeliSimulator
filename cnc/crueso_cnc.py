from cnc.cnc import Cnc
from connections.bluetooth_connection import BluetoothConnection


class CruesoCnc(Cnc):
    def initiate(self):
        self.connection = BluetoothConnection()
