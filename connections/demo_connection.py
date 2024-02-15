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
        time.sleep(0.5)
        message = [
            'Crueso',
            'TachB1',
            '1',
            'TachB2',
            '2',
            'Pressure1',
            '3',
            'Pressure2',
            '4',
        ]
        return '\t'.join(message)
