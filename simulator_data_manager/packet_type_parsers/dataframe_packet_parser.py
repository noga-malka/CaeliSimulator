from abc import ABC, abstractmethod

import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DataframePacketParser(BasePacketParser, ABC):
    def __init__(self, maximum_row_number: int):
        super(DataframePacketParser, self).__init__(pandas.DataFrame())
        self.maximum_row_number = maximum_row_number

    @abstractmethod
    def parse_received_content(self, content: dict) -> dict:
        ...

    def save(self, content: dict):
        """
        insert the converted dictionary to the last row in self._saved_data

        :param content: dictionary to add to dataframe
        """
        content = self.parse_received_content(content)
        self._saved_data = pandas.concat([self._saved_data, pandas.DataFrame(content, index=[0])], ignore_index=True)

    def get_saved_data(self) -> pandas.DataFrame:
        return self._saved_data[-self.maximum_row_number:].reset_index(drop=True)
