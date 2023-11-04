from abc import ABC, abstractmethod
from typing import Any


class BaseParser(ABC):
    def __init__(self, unit_type: str):
        self.unit_type = unit_type

    @staticmethod
    def _integer_to_bytes(numeric_value: int, bytes_number: int = 2) -> bytes:
        return numeric_value.to_bytes(bytes_number, 'big')

    @abstractmethod
    def convert_to_bytes(self, value: Any) -> bytes:
        ...
