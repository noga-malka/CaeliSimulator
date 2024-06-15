import dash_bootstrap_components
import dash_daq
from dash import html, Output, Input
from dash_extensions.enrich import callback, DashLogger

from cnc.consts import Commands
from cnc.crueso_cnc import CruesoCnc
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.single_byte_packet import SingleBytePacket
from components.consts import Placeholder
from components.simulator_components.consts import ButtonIds
from utilities import validate_arguments, ui_logger

crueso_buttons = dash_bootstrap_components.ButtonGroup([
    dash_bootstrap_components.Button([
        html.Label('Blower 1 Speed', className='margin'),
        dash_daq.Slider(id=ButtonIds.Crueso.FIRST_BLOWER_SPEED_VALUE, min=0, max=255, value=0, size=150,
                        handleLabel={"showCurrentValue": True, "label": " "}),
    ], className='flex-center full-width align control-buttons', color='primary', outline=True),
    dash_bootstrap_components.Button([
        html.Label('Blower 2 Speed', className='margin'),
        dash_daq.Slider(id=ButtonIds.Crueso.SECOND_BLOWER_SPEED_VALUE, min=0, max=255, value=0, size=150,
                        handleLabel={"showCurrentValue": True, "label": " "}),
    ], className='flex-center full-width align control-buttons', color='primary', outline=True),
], className='flex', style={'height': '100%'})


@callback(Output(Placeholder.ID, Placeholder.Fields.LANG),
          Input(ButtonIds.Crueso.FIRST_BLOWER_SPEED_VALUE, 'value'),
          prevent_initial_call=True, log=True)
def set_first_blower_speed(blower_speed: int, dash_logger: DashLogger):
    validate_arguments(blower_speed)
    try:
        CruesoCnc().send_packet(SingleBytePacket(Commands.SET_BLOWER_1_SPEED, blower_speed))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)


@callback(Output(Placeholder.ID, Placeholder.Fields.SPELL_CHECK),
          Input(ButtonIds.Crueso.SECOND_BLOWER_SPEED_VALUE, 'value'),
          prevent_initial_call=True, log=True)
def set_second_blower_speed(blower_speed: int, dash_logger: DashLogger):
    validate_arguments(blower_speed)
    try:
        CruesoCnc().send_packet(SingleBytePacket(Commands.SET_BLOWER_2_SPEED, blower_speed))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)
