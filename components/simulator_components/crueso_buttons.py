import dash_bootstrap_components
import dash_daq
from dash import html, Output, Input, State
from dash_extensions.enrich import callback, DashLogger

from cnc.consts import Commands
from cnc.crueso_cnc import CruesoCnc
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.set_single_value_packet import SetSingleValuePacket
from components.consts import Placeholder
from components.simulator_components.consts import ButtonIds
from utilities import validate_arguments, ui_logger

crueso_buttons = dash_bootstrap_components.ButtonGroup([
    html.Div([
        html.Label('Blower 1 Speed', style={'width': '15%'}, className='margin'),
        dash_daq.Slider(id=ButtonIds.Crueso.BLOWER_SPEED_VALUE, min=0, max=255, value=0,
                        handleLabel={"showCurrentValue": True, "label": " "}),
    ]
        , className='flex-center full-width align')
], className='flex', style={'height': '100%'})


@callback(Output(Placeholder.ID, Placeholder.Fields.LANG),
          Input(ButtonIds.Crueso.BLOWER_SPEED_VALUE, 'value'),
          prevent_initial_call=True, log=True)
def set_blower_speed(blower_speed: int, dash_logger: DashLogger):
    validate_arguments(blower_speed)
    try:
        CruesoCnc().send_packet(SetSingleValuePacket(Commands.SET_BLOWER_1_SPEED, blower_speed))
    except NoConnectionOpenException as exception:
        return ui_logger(dash_logger, exception)
