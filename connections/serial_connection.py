import time

import serial
from serial.tools import list_ports

from connections.base_connection import BaseConnection
from connections.consts import UartConsts
from connections.device_disconnected_exception import DeviceDisconnectedException


class SerialConnection(BaseConnection):

    def initiate(self):
        self._device = None

    def discover(self):
        connected_usb_ports = filter(lambda port: "USB" in port[2], list_ports.comports())
        comport_names = [comport[0] for comport in connected_usb_ports]
        self.discovered_devices = comport_names

    def connect(self, device: str):
        """
        connect the given device
        :param device: comport of the device to connect to
        :return: True if the connection was successful, else False
        """
        self.disconnect()  # in case a previous connection exists
        try:
            self._device = serial.Serial(device, UartConsts.BAUDRATE, timeout=UartConsts.TIMEOUT)
        except serial.SerialException:
            self._device = None

    def disconnect(self):
        if self.is_connected:
            self._device.close()
        self._device = None

    def send(self, data: bytes):
        self._device.write(data)

    def receive(self) -> bytes:
        return self._device.readline()

    def receive_message(self) -> str:
        try:
            while not self._device.inWaiting():
                time.sleep(0.01)
            return self.receive().decode().strip()
        except (serial.SerialException, AttributeError):
            raise DeviceDisconnectedException(self.__class__.__name__)
