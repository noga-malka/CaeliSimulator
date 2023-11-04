import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DataframePacketParser(BasePacketParser):
    def __init__(self):
        super(DataframePacketParser, self).__init__(pandas.DataFrame())

    def save(self, content: dict):
        content = {key: int(value) for key, value in content.items()}
        new_data = pandas.concat([self._saved_data, pandas.DataFrame(content, index=[0])], ignore_index=True)
        if len(new_data) > 100:
            new_data = new_data.iloc[1:, :]
        self._saved_data = new_data
