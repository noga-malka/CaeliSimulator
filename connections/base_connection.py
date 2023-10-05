from abc import ABC, abstractmethod


class BaseConnection(ABC):
    """
    basic interface for other connections
    """
    def __init__(self):
        self.device = None
        self.is_connected = False

    @abstractmethod
    def connect(self, **kwargs):
        ...

    @abstractmethod
    def send(self, data: bytes):
        ...

    @abstractmethod
    def receive(self) -> bytes:
        ...

    def close(self):
        if self.device:
            self.device.close()
        self.device = None

    def __del__(self):
        self.close()
