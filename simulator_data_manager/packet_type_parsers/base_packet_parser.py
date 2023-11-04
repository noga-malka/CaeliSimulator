from abc import abstractmethod, ABC
from threading import Event
from typing import Any, Union


class BasePacketParser(ABC):
    def __init__(self, initial_value: Any):
        self._initial_value = initial_value
        self._saved_data = initial_value
        self._event = Event()

    @abstractmethod
    def save(self, content: Union[str, dict]):
        ...

    def get_saved_data(self):
        return self._saved_data

    def get_event(self):
        return self._event

    def clear_saved_data(self):
        self._saved_data = self._initial_value
