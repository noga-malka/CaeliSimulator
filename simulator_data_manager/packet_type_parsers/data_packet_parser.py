import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DataframePacketParser(BasePacketParser):
    def __init__(self):
        super(DataframePacketParser, self).__init__(pandas.DataFrame())

    def save(self, content: dict):
        content = {key: int(value) for key, value in content.items()}
        new_data = self.saved_data.append(content, ignore_index=True)
        if len(new_data) > 100:
            new_data = new_data.iloc[1:, :]
        self.saved_data = new_data

    def get_live_data(self):
        return dict(self.saved_data.iloc[-1])
