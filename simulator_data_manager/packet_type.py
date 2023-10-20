from enum import Enum

from simulator_data_manager.packet_type_parsers.data_packet_parser import DataframePacketParser
from simulator_data_manager.packet_type_parsers.dictionary_packet_parser import DictionaryPacketParser
from simulator_data_manager.packet_type_parsers.profile_packet_parser import ProfilePacketParser


class PacketType(Enum):
    Data = DataframePacketParser()
    BreathParams = ProfilePacketParser()
    ActiveBreathParams = DictionaryPacketParser()
