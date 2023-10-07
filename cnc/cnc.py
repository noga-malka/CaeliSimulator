import sys

from cnc.consts import Commands
from cnc.no_connection_open_exception import NoConnectionOpenException
from connections.base_connection import BaseConnection


class Cnc:
    def __init__(self):
        self.connection: BaseConnection = None

    def update_connection(self, new_connection: BaseConnection):
        self.connection = new_connection

    @staticmethod
    def _build_packet_header() -> bytes:
        return bytes.fromhex('aa55aa')

    @staticmethod
    def _build_packet_footer() -> bytes:
        return bytes.fromhex('0000')

    def build_command_packet(self, command_type: Commands, payload: bytes = None) -> bytes:
        packet_buffer = [self._build_packet_header(), command_type.value]
        if payload is not None:
            payload_length = len(payload).to_bytes(2, sys.byteorder)
            packet_buffer += [payload_length, payload]
        packet_buffer.append(self._build_packet_footer())
        return b''.join(packet_buffer)

    def send_command(self, command_type: Commands, payload: bytes = None):
        if not self.connection.is_connected:
            raise NoConnectionOpenException(command_type.name)
        packet = self.build_command_packet(command_type, payload)
        self.connection.send(packet)
