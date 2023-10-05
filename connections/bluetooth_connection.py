import socket

import bluetooth

from connections.base_connection import BaseConnection
from connections.consts import BluetoothConsts
from connections.device_disconnected_exception import DeviceDisconnectedException


class BluetoothConnection(BaseConnection):
    def __init__(self):
        self._received_data_buffer = BluetoothConsts.NO_DATA_RECEIVED
        self.discovered_devices = self.discover()
        super(BluetoothConnection, self).__init__()

    @staticmethod
    def discover() -> dict:
        """
        discover all near bluetooth devices
        :return: { device name:str , mac:str}
        """
        return {device_name: mac for (mac, device_name) in bluetooth.discover_devices(lookup_names=True)}

    def connect(self, device: str) -> bool:
        """
        connect the given device
        :param device: mac address of the device to connect to
        :return: True if the connection was successful, else False
        """
        self.disconnect()  # in case a previous connection exists

        try:
            self._received_data_buffer = BluetoothConsts.NO_DATA_RECEIVED
            self.device = self._connect_device(device)

        except OSError:
            return False

        return True

    def _connect_device(self, mac_address: str) -> socket.socket:
        """
        build a socket connection to the given mac_address
        :raises OSError if failed
        :param mac_address: device to connect to
        :return: the bluetooth connection
        """
        new_device = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        new_device.connect((self.discovered_devices.get(mac_address, ''), 1))
        return new_device

    def send(self, data: bytes):
        self.device.send(data)

    def receive(self) -> bytes:
        return self.device.recv(BluetoothConsts.RECEIVE_BUFFER_SIZE)

    def _receive_until_end_of_line(self):
        """
        receive data from bluetooth device until a LINE_SEPARATOR character arrives
        update self._received_data_buffer with the new data in order to connect split lines

        :raises DeviceDisconnectedException if there is no data to read from device, and it disconnected
        """
        while BluetoothConsts.LINE_SEPARATOR not in self._received_data_buffer:
            data = self.receive()
            if data == BluetoothConsts.NO_DATA_RECEIVED:
                raise DeviceDisconnectedException(self.__class__.__name__)
            self._received_data_buffer += data

    def receive_message(self) -> str:
        self._receive_until_end_of_line()
        line_end_index = self._received_data_buffer.find(BluetoothConsts.LINE_SEPARATOR)
        message, self._received_data_buffer = self._received_data_buffer.split(line_end_index, 1)
        return message.decode()
