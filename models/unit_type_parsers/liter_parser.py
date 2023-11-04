import math

from models.unit_type_parsers.base_parser import BaseParser
from utilities import int_to_bytes


class LiterParser(BaseParser):
    def __init__(self):
        super(LiterParser, self).__init__('Liter')

    def convert_to_bytes(self, value: float) -> bytes:
        # convert liter to millimeter
        millimeter = int((value * 100) / math.pi)
        return int_to_bytes(millimeter)
