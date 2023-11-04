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
