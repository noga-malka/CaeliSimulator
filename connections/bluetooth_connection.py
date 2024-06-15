import socket

import bluetooth

from connections.base_connection import BaseConnection
from connections.consts import BluetoothConsts
from connections.device_disconnected_exception import DeviceDisconnectedException
from utilities import log_function


class BluetoothConnection(BaseConnection):
    def initiate(self):
        super(BluetoothConnection, self).initiate()
        self._received_data_buffer = BluetoothConsts.NO_DATA_RECEIVED

    def discover(self) -> dict:
        """
        discover all near bluetooth devices
        :return: { device name:str , mac:str}
        """
        return dict(bluetooth.discover_devices(lookup_names=True))

    @log_function
    def connect(self, device: str):
        """
        connect the given device. If the connection fails, OsError is raised and the device is disconnected
        :param device: mac address of the device to connect to
        """
        self.disconnect()  # in case a previous connection exists

        try:
            self._received_data_buffer = BluetoothConsts.NO_DATA_RECEIVED
            self.set_device(self._connect_device(device))

        except OSError:
            self.disconnect()

    @staticmethod
    def _connect_device(mac_address: str) -> socket.socket:
        """
        build a socket connection to the given mac_address
        :raises OSError if fails
        :param mac_address: device to connect to
        :return: the bluetooth connection
        """
        new_device = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        new_device.settimeout(5)
        new_device.connect((mac_address, 1))
        return new_device

    def close(self):
        self._device.close()

    @log_function
    def send(self, data: bytes):
        self._device.send(data)

    def _receive_until_end_of_line(self):
        """
        receive data from bluetooth device until a LINE_SEPARATOR character arrives
        update self._received_data_buffer with the new data in order to connect split lines

        :raises DeviceDisconnectedException if there is no data to read from device, and it disconnected
        """
        while BluetoothConsts.LINE_SEPARATOR not in self._received_data_buffer:
            try:
                data = self._device.recv(BluetoothConsts.RECEIVE_BUFFER_SIZE)
            except (ConnectionAbortedError, TimeoutError):
                # bluetooth connection was closed
                raise DeviceDisconnectedException(self.__class__.__name__)
            if data == BluetoothConsts.NO_DATA_RECEIVED:
                # no data found, the bluetooth connection is closed
                raise DeviceDisconnectedException(self.__class__.__name__)
            self._received_data_buffer += data

    def receive(self) -> str:
        self._receive_until_end_of_line()
        message, self._received_data_buffer = self._received_data_buffer.split(BluetoothConsts.LINE_SEPARATOR, 1)
        return message.decode()
