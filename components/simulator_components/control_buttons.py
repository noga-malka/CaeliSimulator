import dash_bootstrap_components
from dash import html, callback, Output, State, Input

from assets.icons import ControlButtonIcons
from cnc.simulator_cnc import SimulatorCnc
from components.consts import Placeholder
from components.simulator_components.connection_form import simulator_connection_modal
from components.simulator_components.consts import ButtonIds, ButtonGroupIds, ConnectionStatus, SimulatorModal
from components.simulator_components.utilities import create_control_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import validate_arguments

control_buttons = html.Div([
    html.Div('', className='connection-status', id=ConnectionStatus.ID),
    dash_bootstrap_components.ButtonGroup([
        create_control_button('Connect To Simulator', ButtonIds.CONNECT_TO_SIMULATOR,
                              ControlButtonIcons.CONNECT_TO_SIMULATOR),
        create_control_button('Disconnect From Simulator', ButtonIds.DISCONNECT_FROM_SIMULATOR,
                              ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
        create_control_button('Connect To Crueso', ButtonIds.CONNECT_TO_CRUESO,
                              ControlButtonIcons.CONNECT_TO_SIMULATOR),
        create_control_button('Disconnect From Crueso', ButtonIds.DISCONNECT_FROM_CRUESO,
                              ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
    ], id=ButtonGroupIds.SETUP_SIMULATOR),
    simulator_connection_modal,
], className='bg-secondary flex-center flex-column')


@callback(
    Output(SimulatorModal.ID, 'is_open'),
    State(SimulatorModal.ID, 'is_open'),
    Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
    Input(ButtonIds.CONNECT_TO_SIMULATOR, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(Placeholder.ID, Placeholder.Fields.KEY),
          Input(ButtonIds.DISCONNECT_FROM_SIMULATOR, 'n_clicks'),
          prevent_initial_call=True)
def connect_selected_device(disconnect_button: int):
    validate_arguments(disconnect_button)
    SimulatorCnc().connection.disconnect()
    SimulatorDataManager().clear_saved_data()
