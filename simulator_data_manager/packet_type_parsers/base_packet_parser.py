from abc import abstractmethod, ABC
from threading import Event
from typing import Any, Union


class BasePacketParser(ABC):
    def __init__(self, saved_data: Any):
        self.saved_data = saved_data
        self.event = Event()

    @abstractmethod
    def save(self, content: Union[str, dict]):
        ...
