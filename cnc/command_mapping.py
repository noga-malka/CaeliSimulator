from cnc.consts import Commands
from cnc.packets.no_payload_packet import NoPayloadPacket
from components.simulator_components.consts import ButtonIds

COMMAND_PER_BUTTON = {
    ButtonIds.Simulator.ON: NoPayloadPacket(Commands.ON),
    ButtonIds.Simulator.HOMING: NoPayloadPacket(Commands.HOMING),
    ButtonIds.Simulator.STOP: NoPayloadPacket(Commands.STOP),
    ButtonIds.Simulator.OFF: NoPayloadPacket(Commands.OFF),
}
