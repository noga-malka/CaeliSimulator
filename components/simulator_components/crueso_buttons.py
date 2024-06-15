import dash_bootstrap_components
import dash_daq
from dash import html, Output, Input, callback_context
from dash_extensions.enrich import callback, DashLogger

from assets.icons import ControlButtonIcons
from cnc.bluetooth_cnc import BluetoothCnc
from cnc.consts import Commands
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.integer_value_packet import IntegerValuePacket
from cnc.packets.no_payload_packet import NoPayloadPacket
from components.consts import Placeholder
from components.simulator_components.consts import ButtonIds
from components.simulator_components.utilities import create_icon_button
from utilities import validate_arguments, ui_logger

crueso_buttons = dash_bootstrap_components.ButtonGroup([
    create_icon_button('Calibrate', Commands.CALIBRATE.name, ControlButtonIcons.CALIBRATE),
    dash_bootstrap_components.Button([
        html.Label('Blower 1 Speed', className='margin'),
        dash_daq.Slider(id=ButtonIds.Crueso.FIRST_BLOWER_SPEED_VALUE, min=0, max=255, value=0, size=100,
                        handleLabel={"showCurrentValue": True, "label": " "}),
    ], className='flex-center align control-buttons', color='primary', outline=True),
    dash_bootstrap_components.Button([
        html.Label('Blower 2 Speed', className='margin'),
        dash_daq.Slider(id=ButtonIds.Crueso.SECOND_BLOWER_SPEED_VALUE, min=0, max=255, value=0, size=100,
                        handleLabel={"showCurrentValue": True, "label": " "}),
    ], className='flex-center align control-buttons', color='primary', outline=True),
], className='flex', style={'height': '100%'})


@callback(Output(Placeholder.ID, Placeholder.Fields.ACCESS_KEY),
          Input(Commands.CALIBRATE.name, 'n_clicks'),
          prevent_initial_call=True, log=True)
def command_button_clicked(*buttons, dash_logger: DashLogger):
    validate_arguments(*buttons)
    try:
        packet = NoPayloadPacket(Commands[callback_context.triggered_id])
        BluetoothCnc().send_packet(packet)
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)


@callback(Output(Placeholder.ID, Placeholder.Fields.LANG),
          Input(ButtonIds.Crueso.FIRST_BLOWER_SPEED_VALUE, 'value'),
          prevent_initial_call=True, log=True)
def set_first_blower_speed(blower_speed: int, dash_logger: DashLogger):
    validate_arguments(blower_speed)
    try:
        BluetoothCnc().send_packet(IntegerValuePacket(Commands.SET_BLOWER_1_SPEED, blower_speed))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)


@callback(Output(Placeholder.ID, Placeholder.Fields.SPELL_CHECK),
          Input(ButtonIds.Crueso.SECOND_BLOWER_SPEED_VALUE, 'value'),
          prevent_initial_call=True, log=True)
def set_second_blower_speed(blower_speed: int, dash_logger: DashLogger):
    validate_arguments(blower_speed)
    try:
        BluetoothCnc().send_packet(IntegerValuePacket(Commands.SET_BLOWER_2_SPEED, blower_speed))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)
