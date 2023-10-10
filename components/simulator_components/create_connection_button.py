from dash import callback, Output, State, Input

from assets.icons import ControlButtonIcons
from components.simulator_components.consts import ButtonIds, ConnectionModal
from components.simulator_components.utilities import create_control_button

connect_to_simulator_modal_button = create_control_button('Connect To Simulator', ButtonIds.CONNECT_TO_SIMULATOR,
                                                          ControlButtonIcons.CONNECT_TO_SIMULATOR)


@callback(
    Output(ConnectionModal.ID, 'is_open'),
    State(ConnectionModal.ID, 'is_open'),
    Input(ConnectionModal.CONNECT_DEVICE, 'n_clicks'),
    Input(ButtonIds.CONNECT_TO_SIMULATOR, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open
