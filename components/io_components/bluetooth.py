import dash_bootstrap_components
from dash import State, Output, Input, html
from dash_extensions.enrich import DashLogger, callback

from assets.icons import ControlButtonIcons
from cnc.bluetooth_cnc import BluetoothCnc
from components.consts import Placeholder
from components.general_components.modal import create_modal
from components.io_components.consts import BluetoothConsts
from components.io_components.utilities import build_connection_devices_dropdown
from components.simulator_components.utilities import create_icon_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import ui_logger, validate_arguments

bluetooth_connection_modal = create_modal('Connect to Bluetooth',
                                          BluetoothConsts.MODAL_ID,
                                          build_connection_devices_dropdown(BluetoothConsts.OPTIONS_DROPDOWN,
                                                                            BluetoothConsts.SYNC_OPTIONS,
                                                                            BluetoothConsts.CONNECT_DEVICE))

bluetooth_connection_buttons = [html.Div('', className='connection-status', id=BluetoothConsts.STATUS_BAR),
                                dash_bootstrap_components.ButtonGroup([
                                    create_icon_button('Connect To Bluetooth',
                                                       BluetoothConsts.OPEN_CONNECT_MODAL,
                                                       ControlButtonIcons.CONNECT_TO_SIMULATOR),
                                    create_icon_button('Disconnect From Bluetooth',
                                                       BluetoothConsts.DISCONNECT_CONNECTION,
                                                       ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
                                ], className='flex')]


@callback(
    Output(BluetoothConsts.MODAL_ID, 'is_open'),
    State(BluetoothConsts.MODAL_ID, 'is_open'),
    Input(Placeholder.ID, Placeholder.Fields.DRAGGABLE),
    Input(BluetoothConsts.OPEN_CONNECT_MODAL, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(BluetoothConsts.OPTIONS_DROPDOWN, 'options'),
          Input(BluetoothConsts.SYNC_OPTIONS, 'n_clicks'))
def sync_devices(sync_button_clicked: int):
    return BluetoothCnc().connection.discover()


@callback(Output(Placeholder.ID, Placeholder.Fields.DRAGGABLE),
          State(BluetoothConsts.OPTIONS_DROPDOWN, 'value'),
          Input(BluetoothConsts.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, button_clicked: int, dash_logger: DashLogger):
    cnc = BluetoothCnc()
    if not device:
        return ui_logger(dash_logger, 'Device must be selected')
    cnc.connection.connect(device)


@callback(Output(Placeholder.ID, Placeholder.Fields.HIDDEN),
          Input(BluetoothConsts.DISCONNECT_CONNECTION, 'n_clicks'),
          prevent_initial_call=True)
def disconnect_device(disconnect_button: int):
    validate_arguments(disconnect_button)
    BluetoothCnc().connection.disconnect()


@callback(Output(BluetoothConsts.STATUS_BAR, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.DRAGGABLE),
          Input(Placeholder.ID, Placeholder.Fields.HIDDEN))
def update_status_bar(*button_clicks: list[int]):
    SimulatorDataManager().crueso_thread.clear_saved_data()
    if BluetoothCnc().is_connected:
        return 'connection-status connected'
    return 'connection-status'
