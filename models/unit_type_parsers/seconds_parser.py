from models.unit_type_parsers.base_parser import BaseParser
from utilities import int_to_bytes


class SecondsParser(BaseParser):
    def __init__(self):
        super(SecondsParser, self).__init__('S')

    def convert_to_bytes(self, value: float) -> bytes:
        # convert seconds to milliseconds
        milliseconds = int(value * 1000)
        return int_to_bytes(milliseconds)
