from abc import abstractmethod, ABC
from typing import Any


class BasePacketParser(ABC):
    def __init__(self, saved_data: Any):
        self.saved_data = saved_data

    @abstractmethod
    def save(self, packet: list[str]):
        ...
