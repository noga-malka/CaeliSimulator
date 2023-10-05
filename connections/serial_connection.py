import serial

from connections.base_connection import BaseConnection
from connections.consts import UartConsts
from connections.device_disconnected_exception import DeviceDisconnectedException


class SerialConnection(BaseConnection):
    def connect(self, device: str):
        """
        connect the given device
        :param device: comport of the device to connect to
        :return: True if the connection was successful, else False
        """
        self.disconnect()  # in case a previous connection exists
        try:
            self.device = serial.Serial(device, UartConsts.BAUDRATE, timeout=UartConsts.TIMEOUT)
        except serial.SerialException:
            return False
        return True

    def send(self, data: bytes):
        self.device.write(data)

    def receive(self) -> bytes:
        return self.device.readline()

    def receive_message(self) -> str:
        try:
            if self.device.inWaiting():
                # decode bytes to string and remove access spaces
                return self.receive().decode().strip()
        except (serial.SerialException, AttributeError):
            raise DeviceDisconnectedException(self.__class__.__name__)
        return ''
