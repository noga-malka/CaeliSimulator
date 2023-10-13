import sys

from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.base_packet import BasePacket
from connections.base_connection import BaseConnection
from singleton import Singleton
from utilities import log_function


class Cnc(Singleton):
    def initiate(self):
        self.connection: BaseConnection = None

    def set_connection(self, connection: BaseConnection):
        self.connection = connection

    @staticmethod
    def _build_packet_header() -> bytes:
        return bytes.fromhex('aa55aa')

    @staticmethod
    def _build_packet_footer() -> bytes:
        return bytes.fromhex('0000')

    def _build_command_packet(self, packet: BasePacket) -> bytes:
        packet_buffer = [self._build_packet_header(), packet.command_type.value]
        payload = packet.build_payload()
        if payload is not None:
            payload_length = len(payload).to_bytes(2, sys.byteorder)
            packet_buffer += [payload_length, payload]
        packet_buffer.append(self._build_packet_footer())
        return b''.join(packet_buffer)

    @log_function
    def send_command(self, packet: BasePacket):
        if not self.connection.is_connected:
            raise NoConnectionOpenException(packet.command_type.name)
        packet = self._build_command_packet(packet)
        self.connection.send(packet)

    def parse_incoming_packet(self):
        packet = self.connection.receive_message()
        packet_type, *packet_content = packet.split('\t')
        return packet_type, self._parse_packet_content(packet_content)

    @staticmethod
    def _parse_packet_content(packet_content: list[str]):
        parsed_content = dict()
        for field_name_index in range(0, len(packet_content), 2):
            parsed_content[packet_content[field_name_index]] = packet_content[field_name_index + 1]
        return parsed_content
