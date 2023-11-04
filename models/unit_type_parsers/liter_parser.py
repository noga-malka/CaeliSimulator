import math

from models.unit_type_parsers.base_parser import BaseParser


class LiterParser(BaseParser):
    def __init__(self):
        super(LiterParser, self).__init__('Liter')

    def convert_to_bytes(self, value: float) -> bytes:
        # convert liter to millimeter
        millimeter = int((value * 100) / math.pi)
        return self._integer_to_bytes(millimeter)
