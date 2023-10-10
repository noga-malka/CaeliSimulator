from enum import Enum

from connections.bluetooth_connection import BluetoothConnection
from connections.demo_connection import DemoConnection
from connections.serial_connection import SerialConnection


class Connections(Enum):
    BLUETOOTH = BluetoothConnection()
    SERIAL = SerialConnection()
    DEMO = DemoConnection()
