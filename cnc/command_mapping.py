from cnc.consts import Commands
from cnc.packets.command_packet import CommandPacket
from components.simulator_components.consts import ButtonIds

COMMAND_PER_BUTTON = {
    ButtonIds.Simulator.ON: CommandPacket(Commands.ON),
    ButtonIds.Simulator.HOMING: CommandPacket(Commands.HOMING),
    ButtonIds.Simulator.STOP: CommandPacket(Commands.STOP),
    ButtonIds.Simulator.OFF: CommandPacket(Commands.OFF),
}
