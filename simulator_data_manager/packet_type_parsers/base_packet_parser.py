from abc import abstractmethod, ABC
from threading import Event
from typing import Any, Union


class BasePacketParser(ABC):
    def __init__(self, initial_value: Any):
        self._initial_value = initial_value
        self.saved_data = initial_value
        self.event = Event()

    @abstractmethod
    def save(self, content: Union[str, dict]):
        ...

    def clear(self):
        self.saved_data = self._initial_value
