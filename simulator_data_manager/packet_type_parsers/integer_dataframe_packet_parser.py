from simulator_data_manager.packet_type_parsers.dataframe_packet_parser import DataframePacketParser


class IntegerDataframePacketParser(DataframePacketParser):

    def parse_received_content(self, content: dict) -> dict:
        """
        convert the content values to integers

        :param content: dictionary to add to dataframe
        """
        return {key: int(value) for key, value in content.items()}
