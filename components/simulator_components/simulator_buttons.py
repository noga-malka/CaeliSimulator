import dash_bootstrap_components
from dash import callback, Output, Input, callback_context, State

from assets.icons import ControlButtonIcons
from cnc.cnc import Cnc
from cnc.command_mapping import COMMAND_PER_BUTTON
from cnc.consts import Commands
from cnc.packets.command_packet import CommandPacket
from components.consts import Placeholder
from components.simulator_components.consts import ButtonGroupIds, ButtonIds
from components.simulator_components.utilities import create_control_button
from utilities import validate_arguments

simulator_buttons = dash_bootstrap_components.ButtonGroup([
    create_control_button('On', ButtonIds.Simulator.ON, ControlButtonIcons.ON),
    create_control_button('Run', ButtonIds.Simulator.RUN, ControlButtonIcons.RUN),
    create_control_button('Pause', ButtonIds.Simulator.PauseResume.ID, ControlButtonIcons.PAUSE),
    create_control_button('Homing', ButtonIds.Simulator.HOMING, ControlButtonIcons.HOMING),
    create_control_button('Off', ButtonIds.Simulator.OFF, ControlButtonIcons.OFF),
    create_control_button('Emergency Stop', ButtonIds.Simulator.STOP, ControlButtonIcons.STOP, 'danger'),
], id=ButtonGroupIds.SIMULATOR_CONTROLS)


@callback(Output(Placeholder.ID, Placeholder.Fields.ACCESS_KEY),
          Input(ButtonIds.Simulator.ON, 'n_clicks'),
          Input(ButtonIds.Simulator.HOMING, 'n_clicks'),
          Input(ButtonIds.Simulator.STOP, 'n_clicks'),
          Input(ButtonIds.Simulator.OFF, 'n_clicks'),
          prevent_initial_call=True)
def activate_simulator_buttons(*buttons):
    validate_arguments(*buttons)
    command_packet = COMMAND_PER_BUTTON[callback_context.triggered_id]
    Cnc().send_command(command_packet)


@callback(Output(ButtonIds.Simulator.PauseResume.ID, 'children'),
          State(ButtonIds.Simulator.PauseResume.ID, 'children'),
          Input(ButtonIds.Simulator.PauseResume.ID, 'n_clicks'),
          prevent_initial_call=True)
def activate_simulator_buttons(button_content, button_clicked):
    if button_content[1] == 'Pause':
        Cnc().send_command(CommandPacket(Commands.PAUSE_SESSION))
        return ButtonIds.Simulator.PauseResume.RESUME_BUTTON
    else:
        Cnc().send_command(CommandPacket(Commands.RESUME_SESSION))
        return ButtonIds.Simulator.PauseResume.PAUSE_BUTTON
