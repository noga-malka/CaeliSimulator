import dash_bootstrap_components
from dash import html, callback, Output, State, Input

from assets.icons import ControlButtonIcons
from cnc.cnc import Cnc
from components.consts import Placeholder
from components.simulator_components.connection_form import connection_modal
from components.simulator_components.consts import ButtonIds, ButtonGroupIds, ConnectionStatus, ConnectionModal
from components.simulator_components.select_test_case_form import test_case_modal
from components.simulator_components.utilities import create_control_button

control_buttons = html.Div([
    html.Div('', className='connection-status', id=ConnectionStatus.ID),
    dash_bootstrap_components.ButtonGroup([
        create_control_button('Connect To Simulator', ButtonIds.CONNECT_TO_SIMULATOR,
                              ControlButtonIcons.CONNECT_TO_SIMULATOR),
        create_control_button('Disconnect From Simulator', ButtonIds.DISCONNECT_FROM_SIMULATOR,
                              ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
        create_control_button('Select Test Case', ButtonIds.TEST_CASE, ControlButtonIcons.SELECT_TEST_CASE)
    ], id=ButtonGroupIds.SETUP_SIMULATOR),
    test_case_modal,
    connection_modal,
], className='bg-secondary flex', style={'justify-content': 'center', 'flex-direction': 'column'})


@callback(
    Output(ConnectionModal.ID, 'is_open'),
    State(ConnectionModal.ID, 'is_open'),
    Input(ConnectionModal.CONNECT_DEVICE, 'n_clicks'),
    Input(ButtonIds.CONNECT_TO_SIMULATOR, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(Placeholder.ID, Placeholder.Fields.KEY),
          Input(ButtonIds.DISCONNECT_FROM_SIMULATOR, 'n_clicks'),
          prevent_initial_call=True)
def connect_selected_device(disconnect_button: int):
    Cnc().connection.disconnect()
