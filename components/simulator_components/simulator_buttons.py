import dash_bootstrap_components
from dash import Output, Input, callback_context, State, no_update
from dash_extensions.enrich import callback, DashLogger

from assets.icons import ControlButtonIcons
from cnc.command_mapping import COMMAND_PER_BUTTON
from cnc.consts import Commands
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.command_packet import CommandPacket
from cnc.simulator_cnc import SimulatorCnc
from components.consts import Placeholder
from components.simulator_components.consts import ButtonGroupIds, ButtonIds
from components.simulator_components.utilities import create_control_button
from utilities import validate_arguments, ui_logger

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
          prevent_initial_call=True, log=True)
def activate_simulator_buttons(*buttons, dash_logger: DashLogger):
    validate_arguments(*buttons)
    command_packet = COMMAND_PER_BUTTON[callback_context.triggered_id]
    try:
        SimulatorCnc().send_packet(command_packet)
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)


@callback(Output(ButtonIds.Simulator.PauseResume.ID, 'children'),
          State(ButtonIds.Simulator.PauseResume.ID, 'children'),
          Input(ButtonIds.Simulator.PauseResume.ID, 'n_clicks'),
          prevent_initial_call=True, log=True)
def activate_simulator_buttons(button_content, button_clicked, dash_logger: DashLogger):
    if not button_clicked:
        return no_update
    if button_content[1] == 'Pause':
        command = Commands.PAUSE_SESSION
        button = ButtonIds.Simulator.PauseResume.RESUME_BUTTON
    else:
        command = Commands.RESUME_SESSION
        button = ButtonIds.Simulator.PauseResume.PAUSE_BUTTON
    try:
        SimulatorCnc().send_packet(CommandPacket(command))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)
    return button
