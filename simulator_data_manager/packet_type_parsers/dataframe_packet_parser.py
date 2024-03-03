from abc import ABC, abstractmethod

import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class DataframePacketParser(BasePacketParser, ABC):
    def __init__(self):
        super(DataframePacketParser, self).__init__(pandas.DataFrame())

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
