from cnc.packets.base_packet import BasePacket


class NoPayloadPacket(BasePacket):
    def build_payload(self):
        return None
