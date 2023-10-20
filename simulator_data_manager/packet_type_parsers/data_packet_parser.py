from typing import Union

import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DataframePacketParser(BasePacketParser):
    def __init__(self):
        super(DataframePacketParser, self).__init__(pandas.DataFrame())

    def save(self, content: dict):
        self.saved_data = self.saved_data.append(content, ignore_index=True)

    def get_live_data(self):
        return dict(self.saved_data.iloc[-1])
