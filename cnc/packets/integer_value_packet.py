from cnc.consts import Commands
from cnc.packets.base_packet import BasePacket
from utilities import int_to_bytes


class IntegerValuePacket(BasePacket):
    def __init__(self, command_type: Commands, target_value: int, byte_count: int = 1):
        super().__init__(command_type)
        self.target_value = target_value
        self.byte_count = byte_count

    def build_payload(self):
        return int_to_bytes(self.target_value, byte_count=self.byte_count)
