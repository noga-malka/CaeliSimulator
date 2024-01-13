import dash_bootstrap_components
from dash import State, Output, Input, html
from dash_extensions.enrich import DashLogger, callback

from assets.icons import ControlButtonIcons
from cnc.simulator_cnc import SimulatorCnc
from components.consts import Placeholder
from components.general_components.modal import create_modal
from components.simulator_components.inputs.consts import SimulatorConsts
from components.simulator_components.inputs.utilities import build_connection_devices_dropdown, connection_status_change
from components.simulator_components.utilities import create_icon_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import ui_logger, validate_arguments

simulator_connection_modal = create_modal('Connect to Simulator',
                                          SimulatorConsts.MODAL_ID,
                                          build_connection_devices_dropdown(SimulatorConsts.OPTIONS_DROPDOWN,
                                                                            SimulatorConsts.SYNC_OPTIONS,
                                                                            SimulatorConsts.CONNECT_DEVICE))

simulator_connection_buttons = [html.Div('', className='connection-status', id=SimulatorConsts.STATUS_BAR),
                                dash_bootstrap_components.ButtonGroup([
                                    create_icon_button('Connect To Simulator',
                                                       SimulatorConsts.OPEN_CONNECT_MODAL,
                                                       ControlButtonIcons.CONNECT_TO_SIMULATOR),
                                    create_icon_button('Disconnect From Simulator',
                                                       SimulatorConsts.DISCONNECT_CONNECTION,
                                                       ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
                                ], className='flex')]


@callback(
    Output(SimulatorConsts.MODAL_ID, 'is_open'),
    State(SimulatorConsts.MODAL_ID, 'is_open'),
    Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
    Input(SimulatorConsts.OPEN_CONNECT_MODAL, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(SimulatorConsts.OPTIONS_DROPDOWN, 'options'),
          Input(SimulatorConsts.SYNC_OPTIONS, 'n_clicks'))
def sync_devices(sync_button_clicked: int):
    return SimulatorCnc().connection.discover()


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          State(SimulatorConsts.OPTIONS_DROPDOWN, 'value'),
          Input(SimulatorConsts.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, button_clicked: int, dash_logger: DashLogger):
    cnc = SimulatorCnc()
    if not device:
        return ui_logger(dash_logger, 'Device must be selected')
    cnc.connection.connect(device)


@callback(Output(Placeholder.ID, Placeholder.Fields.KEY),
          Input(SimulatorConsts.DISCONNECT_CONNECTION, 'n_clicks'),
          prevent_initial_call=True)
def disconnect_device(disconnect_button: int):
    validate_arguments(disconnect_button)
    SimulatorCnc().connection.disconnect()


@callback(Output(SimulatorConsts.STATUS_BAR, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          Input(Placeholder.ID, Placeholder.Fields.KEY))
def update_status_bar(*button_clicks: list[int]):
    SimulatorDataManager().simulator_thread.clear_saved_data()
    return connection_status_change(SimulatorCnc())
