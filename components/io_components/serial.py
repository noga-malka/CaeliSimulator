import dash_bootstrap_components
from dash import State, Output, Input, html
from dash_extensions.enrich import DashLogger, callback

from assets.icons import ControlButtonIcons
from cnc.serial_cnc import SerialCnc
from components.consts import Placeholder
from components.general_components.modal import create_modal
from components.io_components.consts import SerialConsts
from components.io_components.utilities import build_connection_devices_dropdown
from components.simulator_components.utilities import create_icon_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import ui_logger, validate_arguments

serial_connection_modal = create_modal('Connect to Serial',
                                       SerialConsts.MODAL_ID,
                                       build_connection_devices_dropdown(SerialConsts.OPTIONS_DROPDOWN,
                                                                         SerialConsts.SYNC_OPTIONS,
                                                                         SerialConsts.CONNECT_DEVICE))

serial_connection_buttons = [html.Div('', className='connection-status', id=SerialConsts.STATUS_BAR),
                             dash_bootstrap_components.ButtonGroup([
                                 create_icon_button('Connect To Serial',
                                                    SerialConsts.OPEN_CONNECT_MODAL,
                                                    ControlButtonIcons.CONNECT_TO_SIMULATOR),
                                 create_icon_button('Disconnect From Serial',
                                                    SerialConsts.DISCONNECT_CONNECTION,
                                                    ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
                             ], className='flex')]


@callback(
    Output(SerialConsts.MODAL_ID, 'is_open'),
    State(SerialConsts.MODAL_ID, 'is_open'),
    Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
    Input(SerialConsts.OPEN_CONNECT_MODAL, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(SerialConsts.OPTIONS_DROPDOWN, 'options'),
          Input(SerialConsts.SYNC_OPTIONS, 'n_clicks'))
def sync_devices(sync_button_clicked: int):
    return SerialCnc().connection.discover()


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          State(SerialConsts.OPTIONS_DROPDOWN, 'value'),
          Input(SerialConsts.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, button_clicked: int, dash_logger: DashLogger):
    if not device:
        return ui_logger(dash_logger, 'Device must be selected')
    SerialCnc().connection.connect(device)


@callback(Output(Placeholder.ID, Placeholder.Fields.KEY),
          Input(SerialConsts.DISCONNECT_CONNECTION, 'n_clicks'),
          prevent_initial_call=True)
def disconnect_device(disconnect_button: int):
    validate_arguments(disconnect_button)
    SerialCnc().connection.disconnect()


@callback(Output(SerialConsts.STATUS_BAR, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          Input(Placeholder.ID, Placeholder.Fields.KEY))
def update_status_bar(*button_clicks: list[int]):
    SimulatorDataManager().simulator_thread.clear_saved_data()
    if SerialCnc().is_connected:
        return 'connection-status connected'
    return 'connection-status'
