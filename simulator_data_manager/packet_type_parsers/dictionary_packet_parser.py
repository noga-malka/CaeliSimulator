from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DictionaryPacketParser(BasePacketParser):
    def __init__(self):
        super(DictionaryPacketParser, self).__init__({})

    def save(self, content: dict):
        """
        save the dictionary received from the simulator without changes

        :param content: dictionary of values to save
        """
        self._saved_data = content
