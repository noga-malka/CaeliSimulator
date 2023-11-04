from simulator_data_manager.packet_type_parsers.base_packet_parser import BasePacketParser
from simulator_data_manager.packet_type_parsers.consts import SimulatorKeys


class BreathParametersPacketParser(BasePacketParser):
    def __init__(self):
        super(BreathParametersPacketParser, self).__init__({})

    def save(self, content: dict):
        """
        save the given profile by index
        activate the parser's event to indicate that there is a valid profile configured in the simulator

        :param content: dictionary of a single profile's breath parameters
        """
        self._saved_data[content[SimulatorKeys.INDEX]] = content
        self._event.set()
