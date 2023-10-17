import dash_bootstrap_components
from dash import callback, Output, Input, callback_context

from assets.icons import ControlButtonIcons
from cnc.cnc import Cnc
from cnc.command_mapping import COMMAND_PER_BUTTON
from components.consts import Placeholder
from components.simulator_components.consts import ButtonGroupIds, ButtonIds
from components.simulator_components.utilities import create_control_button
from utilities import validate_arguments

simulator_buttons = dash_bootstrap_components.ButtonGroup([
    create_control_button('On', ButtonIds.Simulator.ON, ControlButtonIcons.ON),
    create_control_button('Run', ButtonIds.Simulator.RUN, ControlButtonIcons.RUN),
    create_control_button('Pause', ButtonIds.Simulator.PAUSE, ControlButtonIcons.PAUSE),
    create_control_button('Resume', ButtonIds.Simulator.RESUME, ControlButtonIcons.RESUME),
    create_control_button('Stop', ButtonIds.Simulator.STOP, ControlButtonIcons.STOP),
    create_control_button('Homing', ButtonIds.Simulator.HOMING, ControlButtonIcons.HOMING),
    create_control_button('Off', ButtonIds.Simulator.OFF, ControlButtonIcons.OFF),
], id=ButtonGroupIds.SIMULATOR_CONTROLS)


@callback(Output(Placeholder.ID, Placeholder.Fields.ACCESS_KEY),
          Input(ButtonIds.Simulator.ON, 'n_clicks'),
          Input(ButtonIds.Simulator.RUN, 'n_clicks'),
          Input(ButtonIds.Simulator.HOMING, 'n_clicks'),
          Input(ButtonIds.Simulator.PAUSE, 'n_clicks'),
          Input(ButtonIds.Simulator.RESUME, 'n_clicks'),
          Input(ButtonIds.Simulator.STOP, 'n_clicks'),
          Input(ButtonIds.Simulator.OFF, 'n_clicks'),
          prevent_initial_call=True)
def activate_simulator_buttons(*buttons):
    validate_arguments(*buttons)
    command_packet = COMMAND_PER_BUTTON[callback_context.triggered_id]
    Cnc().send_command(command_packet)
