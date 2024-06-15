import random
import time

from connections.base_connection import BaseConnection


class DemoConnection(BaseConnection):

    def discover(self):
        return {'test': 'test'}

    def connect(self, device: str):
        self.set_device('connected')

    def close(self):
        pass

    def send(self, data: bytes):
        print('Send: ', data)

    @staticmethod
    def _random():
        return str(random.randint(0, 10))

    def receive(self) -> str:
        time.sleep(0.2)
        message = [
            'Crueso_data',
            'TachB1',
            self._random(),
            'TachB2',
            self._random(),
            'Pressure1',
            self._random(),
            'Pressure2',
            self._random(),
        ]
        return '\t'.join(message)
