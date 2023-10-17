from enum import Enum

from simulator_data_manager.packet_type_parsers.data_packet_parser import DataframePacketParser


class PacketType(Enum):
    Data = DataframePacketParser()
