from models.unit_type_parsers.base_parser import BaseParser


class SecondsParser(BaseParser):
    def __init__(self):
        super(SecondsParser, self).__init__('S')

    def convert_to_bytes(self, value: float) -> bytes:
        return self._integer_to_bytes(int(value * 1000))
