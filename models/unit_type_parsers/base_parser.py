from abc import ABC, abstractmethod
from typing import Any


class BaseParser(ABC):
    def __init__(self, unit_type: str):
        self.unit_type = unit_type

    @abstractmethod
    def convert_to_bytes(self, value: Any) -> bytes:
        ...
