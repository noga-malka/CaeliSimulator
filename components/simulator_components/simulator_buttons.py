import dash_bootstrap_components
from dash import Output, Input, callback_context, State, no_update
from dash_extensions.enrich import callback, DashLogger

from assets.icons import ControlButtonIcons
from cnc.consts import Commands
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.no_payload_packet import NoPayloadPacket
from cnc.serial_cnc import SerialCnc
from components.consts import Placeholder
from components.simulator_components.consts import ButtonIds
from components.simulator_components.utilities import create_icon_button
from utilities import validate_arguments, ui_logger

simulator_buttons = dash_bootstrap_components.ButtonGroup([
    create_icon_button('On', Commands.ON.name, ControlButtonIcons.ON),
    create_icon_button('Run', ButtonIds.Simulator.RUN, ControlButtonIcons.RUN),
    create_icon_button('Pause', ButtonIds.Simulator.PauseResume.ID, ControlButtonIcons.PAUSE),
    create_icon_button('Homing', Commands.HOMING.name, ControlButtonIcons.HOMING),
    create_icon_button('Off', Commands.OFF.name, ControlButtonIcons.OFF),
    create_icon_button('Emergency Stop', Commands.STOP.name, ControlButtonIcons.STOP, 'danger'),
], className='flex')


@callback(Output(Placeholder.ID, Placeholder.Fields.ACCESS_KEY),
          Input(Commands.ON.name, 'n_clicks'),
          Input(Commands.HOMING.name, 'n_clicks'),
          Input(Commands.STOP.name, 'n_clicks'),
          Input(Commands.OFF.name, 'n_clicks'),
          prevent_initial_call=True, log=True)
def activate_simulator_buttons(*buttons, dash_logger: DashLogger):
    validate_arguments(*buttons)
    try:
        packet = NoPayloadPacket(Commands[callback_context.triggered_id])
        SerialCnc().send_packet(packet)
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
        SerialCnc().send_packet(NoPayloadPacket(command))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)
    return button
