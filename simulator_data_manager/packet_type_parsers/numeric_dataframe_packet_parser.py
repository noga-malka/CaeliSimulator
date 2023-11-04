import pandas

from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser


class NumericDataframePacketParser(BasePacketParser):
    def __init__(self, maximum_row_number: int):
        super(NumericDataframePacketParser, self).__init__(pandas.DataFrame())
        self.maximum_row_number = maximum_row_number

    def _validate_length(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        """
        if the given dataframe is longer than self.maximum_row_number, remove the first row from dataframe

        :param dataframe: DataFrame object
        :return: the dataframe after length validation
        """
        if len(dataframe) > self.maximum_row_number:
            return dataframe.iloc[1:, :]
        return dataframe

    def save(self, content: dict):
        """
        convert the content values to integers and insert the converted dictionary to the last row in self._saved_data

        :param content: dictionary to add to dataframe
        """
        content = {key: int(value) for key, value in content.items()}
        new_data = pandas.concat([self._saved_data, pandas.DataFrame(content, index=[0])], ignore_index=True)
        self._saved_data = self._validate_length(new_data)
