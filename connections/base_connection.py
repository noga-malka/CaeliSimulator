from abc import ABC, abstractmethod

from singleton import Singleton


class BaseConnection(Singleton, ABC):
    """
    basic interface for other connections
    """

    @abstractmethod
    def connect(self, device: str) -> bool:
        ...

    @abstractmethod
    def send(self, data: bytes):
        ...

    @abstractmethod
    def receive(self) -> bytes:
        ...

    @abstractmethod
    def receive_message(self) -> str:
        ...

    @property
    def is_connected(self):
        return self.device is not None

    def disconnect(self):
        if self.is_connected:
            self.device.disconnect()
        self.device = None

    def __del__(self):
        self.disconnect()
