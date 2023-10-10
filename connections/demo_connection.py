import random

from connections.base_connection import BaseConnection


class DemoConnection(BaseConnection):
    def initiate(self):
        self.device = None

    def discover(self):
        """
        discover all near bluetooth devices
        :return: { device name:str , mac:str}
        """
        self.discovered_devices = {}

    def connect(self, device: str):
        """
        connect the given device
        :param device: mac address of the device to connect to
        :return: True if the connection was successful, else False
        """
        self.device = 'connected'

    def disconnect(self):
        self.device = None

    def send(self, data: bytes):
        print('Send: ', data)

    def receive(self) -> bytes:
        return b''

    @staticmethod
    def _random():
        return str(random.randint(0, 10))

    def receive_message(self) -> str:
        message = [
            'Data',
            'Profile Index',
            '1',
            'Profile Run Time',
            self._random(),
            'Total Interval',
            self._random(),
            'Total Run Time',
            self._random(),
            'Status',
            self._random(),
        ]
        return '\t'.join(message)