import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DataframePacketParser(BasePacketParser):
    def __init__(self):
        super(DataframePacketParser, self).__init__(pandas.DataFrame())

    def save(self, packet: list[str]):
        self.saved_data = self.saved_data.append(packet, ignore_index=True)
