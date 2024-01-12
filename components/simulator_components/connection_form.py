import dash_bootstrap_components
from dash import Output, State, Input
from dash import dcc
from dash_extensions.enrich import callback, DashLogger

from cnc.simulator_cnc import SimulatorCnc
from components.consts import Placeholder
from components.general_components.input_card import create_card
from components.general_components.modal import create_modal
from components.simulator_components.consts import ConnectionModal, ConnectionStatus
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import ui_logger


def build_devices_dropdown():
    return create_card('Select Device', [
        dcc.Loading(
            dcc.Dropdown([], id=ConnectionModal.DEVICE_DROPDOWN, searchable=True,
                         style={'width': '230px', 'margin-right': '5px'}),
        ),
        dash_bootstrap_components.Button('Sync Devices', id=ConnectionModal.SYNC_DEVICES)
    ])


connection_modal = create_modal('Connect to Simulator', ConnectionModal.ID, [
    build_devices_dropdown(),
    dash_bootstrap_components.Button('Connect', id=ConnectionModal.CONNECT_DEVICE)
])


@callback(Output(ConnectionModal.DEVICE_DROPDOWN, 'options'),
          Input(ConnectionModal.SYNC_DEVICES, 'n_clicks'))
def sync_devices(sync_button_clicked: int):
    return SimulatorCnc().connection.discover()


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          State(ConnectionModal.DEVICE_DROPDOWN, 'value'),
          Input(ConnectionModal.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, button_clicked: int, dash_logger: DashLogger):
    cnc = SimulatorCnc()
    if not device:
        return ui_logger(dash_logger, 'Device must be selected')
    cnc.connection.connect(device)


@callback(Output(ConnectionStatus.ID, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          Input(Placeholder.ID, Placeholder.Fields.KEY))
def connect_selected_device(*button_clicks: list[int]):
    SimulatorDataManager().clear_saved_data()
    class_name = 'connection-status'
    is_connected_class_name = ''
    if SimulatorCnc().is_connected:
        is_connected_class_name = 'connected'
    return f'{class_name} {is_connected_class_name}'
