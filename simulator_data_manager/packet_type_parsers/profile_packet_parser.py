from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class ProfilePacketParser(BasePacketParser):
    def __init__(self):
        super(ProfilePacketParser, self).__init__({})

    def save(self, content: dict):
        self.saved_data[content['Index']] = content
        self.event.set()
