from abc import ABC, abstractmethod
from typing import Union, Any

from singleton import Singleton


class BaseConnection(Singleton, ABC):
    """
    basic interface for other connections
    """

    def initiate(self):
        self._device = None
        self.discovered_devices = None

    def set_device(self, device: Any):
        """
        :param device: connected device
        """
        self._device = device

    def update_discovered_devices(self):
        self.discovered_devices = self.discover()

    def disconnect(self):
        """
        if the connection is open, close it and reset self._device
        """
        if self.is_connected:
            self.close()
        self.set_device(None)

    @property
    def is_connected(self) -> bool:
        return self._device is not None

    @abstractmethod
    def discover(self) -> Union[list, dict]:
        ...

    @abstractmethod
    def connect(self, device: str):
        ...

    @abstractmethod
    def send(self, data: bytes):
        ...

    @abstractmethod
    def receive(self) -> str:
        ...

    @abstractmethod
    def close(self):
        ...

    def __del__(self):
        self.disconnect()
