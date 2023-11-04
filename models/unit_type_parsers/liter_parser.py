from models.unit_type_parsers.base_parser import BaseParser


class LiterParser(BaseParser):
    def __init__(self):
        super(LiterParser, self).__init__('Liter')

    def convert_to_bytes(self, value: int) -> bytes:
        return self._integer_to_bytes(value)
