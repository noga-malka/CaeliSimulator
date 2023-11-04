from typing import Union

from cnc.consts import ProtocolConsts, Connections
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.base_packet import BasePacket
from connections.base_connection import BaseConnection
from connections.bluetooth_connection import BluetoothConnection
from connections.demo_connection import DemoConnection
from connections.serial_connection import SerialConnection
from singleton import Singleton
from utilities import log_function, int_to_bytes


class Cnc(Singleton):
    def initiate(self):
        self.connection: BaseConnection = None
        self.connection_options: dict[str, BaseConnection] = {
            Connections.BLUETOOTH: BluetoothConnection(),
            Connections.SERIAL: SerialConnection(),
            Connections.DEMO: DemoConnection()
        }

    def set_connection(self, connection: BaseConnection):
        self.connection = connection

    @property
    def is_connected(self):
        return self.connection is not None and self.connection.is_connected

    @staticmethod
    def _parse_payload(packet: BasePacket) -> list[bytes]:
        """
        extrac the packet's payload
        if it's empty, there is no payload to send so return empty list, else return the payload's length and content

        :param packet: BasePacket object to build its payload
        :return: list of the payload length and data
        """
        payload = packet.build_payload()
        if payload is not None:
            payload_length = int_to_bytes(len(payload), byte_count=1)
            return [payload_length, payload]
        return []

    def _convert_packet_to_bytes(self, packet: BasePacket) -> bytes:
        """
        create a bytes packet with header, command type, payload and footer from the given BasePacket object

        :param packet: packet to convert
        :return: bytes array of the packet
        """
        packet_buffer = [ProtocolConsts.HEADER,
                         packet.command_type.value,
                         *self._parse_payload(packet),
                         ProtocolConsts.FOOTER]
        return b''.join(packet_buffer)

    @log_function
    def send_packet(self, packet: BasePacket):
        """
        for a given packet, convert it to bytes and send them to self.connection.

        :param packet: BasePacket object to send
        :raises: NoConnectionOpenException if self.connection is not connected
        """
        if not self.is_connected:
            raise NoConnectionOpenException(packet.command_type.name)
        packet = self._convert_packet_to_bytes(packet)
        self.connection.send(packet)

    def parse_incoming_packet(self) -> tuple[str, Union[str, dict]]:
        """
        receive the next packet
        split the payload with ProtocolConsts.SEPARATOR
        the extra payload is parsed to be either a string or a dictionary

        :return: the packet type string, and the packet's payload
        """
        packet = self.connection.receive()
        packet_type, *packet_content = packet.split(ProtocolConsts.SEPARATOR)
        return packet_type, self._parse_packet_content(packet_content)

    @staticmethod
    def _parse_packet_content(packet_content: list[str]) -> Union[str, dict]:
        """
        :param packet_content: list of the packet's payload
        :return: dictionary or a string representation of the payload
        """
        try:
            content_iterator = iter(packet_content)
            # this line convert an even list to dictionary with even index as keys and odd index as values
            # example:
            #   [1,2,3,4,5,6] => {1:2, 3:4, 5:6}
            return {field_name: next(content_iterator) for field_name in content_iterator}
        except StopIteration:
            # the payload is not even therefore cannot be converted to dictionary.
            # in this case we return the payload as string
            return ProtocolConsts.SEPARATOR.join(packet_content)
