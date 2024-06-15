import time

import serial
from serial.tools import list_ports

from connections.base_connection import BaseConnection
from connections.consts import UartConsts
from connections.device_disconnected_exception import DeviceDisconnectedException


class SerialConnection(BaseConnection):

    def discover(self) -> list:
        """
        find all USB connections to this computer

        :return: list of COM names
        """
        connected_usb_ports = filter(lambda port: "USB" in port[2], list_ports.comports())
        return [comport[0] for comport in connected_usb_ports]

    def connect(self, device: str):
        """
        connect the given device. If the connection fails, SerialException is raised and the device is disconnected
        :param device: comport of the device to connect to
        :return: True if the connection was successful, else False
        """
        self.disconnect()  # in case a previous connection exists
        try:
            self.set_device(serial.Serial(device, UartConsts.BAUDRATE, timeout=UartConsts.TIMEOUT))
        except serial.SerialException:
            self.disconnect()

    def close(self):
        self._device.close()

    def send(self, data: bytes):
        self._device.write(data)

    def receive(self) -> str:
        try:
            # if there is no data to read, wait
            while not self._device.inWaiting():
                time.sleep(0.01)
            return self._device.readline().decode().strip()
        except (serial.SerialException, AttributeError, TypeError):
            # the serial connection is closed
            raise DeviceDisconnectedException(self.__class__.__name__)
