from dash import callback, Output, State, Input

from assets.icons import ControlButtonIcons
from components.simulator_components.consts import ButtonIds, BluetoothModal
from components.simulator_components.utilities import create_control_button

bluetooth_modal_button = create_control_button('Connect To Bluetooth', ButtonIds.BLUETOOTH,
                                               ControlButtonIcons.BLUETOOTH)


@callback(
    Output(BluetoothModal.ID, 'is_open'),
    State(BluetoothModal.ID, 'is_open'),
    Input(ButtonIds.BLUETOOTH, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open
