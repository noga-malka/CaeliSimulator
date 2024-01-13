import dash_bootstrap_components
from dash import State, Output, Input, html
from dash_extensions.enrich import DashLogger, callback

from assets.icons import ControlButtonIcons
from cnc.crueso_cnc import CruesoCnc
from components.consts import Placeholder
from components.general_components.modal import create_modal
from components.simulator_components.inputs.consts import CruesoConsts
from components.simulator_components.inputs.utilities import build_connection_devices_dropdown, connection_status_change
from components.simulator_components.utilities import create_icon_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import ui_logger, validate_arguments

crueso_connection_modal = create_modal('Connect to Crueso',
                                       CruesoConsts.MODAL_ID,
                                       build_connection_devices_dropdown(CruesoConsts.OPTIONS_DROPDOWN,
                                                                         CruesoConsts.SYNC_OPTIONS,
                                                                         CruesoConsts.CONNECT_DEVICE))

crueso_connection_buttons = [html.Div('', className='connection-status', id=CruesoConsts.STATUS_BAR),
                             dash_bootstrap_components.ButtonGroup([
                                 create_icon_button('Connect To Crueso',
                                                    CruesoConsts.OPEN_CONNECT_MODAL,
                                                    ControlButtonIcons.CONNECT_TO_SIMULATOR),
                                 create_icon_button('Disconnect From Crueso',
                                                    CruesoConsts.DISCONNECT_CONNECTION,
                                                    ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
                             ], className='flex')]


@callback(
    Output(CruesoConsts.MODAL_ID, 'is_open'),
    State(CruesoConsts.MODAL_ID, 'is_open'),
    Input(Placeholder.ID, Placeholder.Fields.DRAGGABLE),
    Input(CruesoConsts.OPEN_CONNECT_MODAL, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(CruesoConsts.OPTIONS_DROPDOWN, 'options'),
          Input(CruesoConsts.SYNC_OPTIONS, 'n_clicks'))
def sync_devices(sync_button_clicked: int):
    return CruesoCnc().connection.discover()


@callback(Output(Placeholder.ID, Placeholder.Fields.DRAGGABLE),
          State(CruesoConsts.OPTIONS_DROPDOWN, 'value'),
          Input(CruesoConsts.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, button_clicked: int, dash_logger: DashLogger):
    cnc = CruesoCnc()
    if not device:
        return ui_logger(dash_logger, 'Device must be selected')
    cnc.connection.connect(device)


@callback(Output(Placeholder.ID, Placeholder.Fields.HIDDEN),
          Input(CruesoConsts.DISCONNECT_CONNECTION, 'n_clicks'),
          prevent_initial_call=True)
def disconnect_device(disconnect_button: int):
    validate_arguments(disconnect_button)
    CruesoCnc().connection.disconnect()


@callback(Output(CruesoConsts.STATUS_BAR, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.DRAGGABLE),
          Input(Placeholder.ID, Placeholder.Fields.HIDDEN))
def update_status_bar(*button_clicks: list[int]):
    SimulatorDataManager().crueso_thread.clear_saved_data()
    return connection_status_change(CruesoCnc())
