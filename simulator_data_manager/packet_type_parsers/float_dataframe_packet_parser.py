from simulator_data_manager.packet_type_parsers.dataframe_packet_parser import DataframePacketParser


class FloatDataframePacketParser(DataframePacketParser):

    def parse_received_content(self, content: dict) -> dict:
        """
        convert the content values to floats

        :param content: dictionary to add to dataframe
        """
        return {key: float(value) for key, value in content.items()}
