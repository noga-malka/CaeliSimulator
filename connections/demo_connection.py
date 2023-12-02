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
            'Data',
            'Breath Volume', '0',
            'Breathing State', '46',
            'Profile RunTime', '63',
            'Current Profile', '0',
            'Total RunTime', '131',
            'Total Intervals', '0',
            'Critical Flag', '0',
            'Simulator Status', '2'
        ]
        return '\t'.join(message)
