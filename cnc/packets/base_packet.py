from abc import ABC, abstractmethod

from cnc.consts import Commands


class BasePacket(ABC):
    def __init__(self, command_type: Commands):
        self.command_type = command_type

    @abstractmethod
    def build_payload(self):
        ...

    def __str__(self):
        return f'{self.__class__.__name__} {self.command_type}'
