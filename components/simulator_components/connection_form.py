import logging

import dash_bootstrap_components
from dash import Output, State, Input
from dash import dcc
from dash_extensions.enrich import callback, DashLogger

from cnc.cnc import Cnc
from components.consts import Placeholder
from components.general_components.input_card import create_card
from components.general_components.modal import create_modal
from components.simulator_components.consts import ConnectionModal, ConnectionStatus
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import dash_logging


def build_devices_dropdown():
    return create_card('Select Device', [
        dcc.Loading(
            dcc.Dropdown([], id=ConnectionModal.DEVICE_DROPDOWN, searchable=True,
                         style={'width': '230px', 'margin-right': '5px'}),
        ),
        dash_bootstrap_components.Button('Sync Devices', id=ConnectionModal.SYNC_DEVICES)
    ])


connection_modal = create_modal('Connect to Simulator', ConnectionModal.ID, [
    create_card('Select Connection Type', [
        dcc.Dropdown(list(Cnc().connection_options.keys()),
                     id=ConnectionModal.CONNECTION_TYPE_DROPDOWN, searchable=True,
                     style={'width': '230px', 'margin-right': '5px'}),
    ]),
    build_devices_dropdown(),
    dash_bootstrap_components.Button('Connect', id=ConnectionModal.CONNECT_DEVICE)
])


@callback(Output(ConnectionModal.DEVICE_DROPDOWN, 'options'),
          Input(ConnectionModal.CONNECTION_TYPE_DROPDOWN, 'value'),
          Input(ConnectionModal.SYNC_DEVICES, 'n_clicks'),
          prevent_initial_call=True)
def sync_devices(connection_type: str, sync_button_clicked: int):
    connection_options = Cnc().connection_options
    if connection_type in connection_options:
        return connection_options[connection_type].discover()
    return []


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          State(ConnectionModal.DEVICE_DROPDOWN, 'value'),
          State(ConnectionModal.CONNECTION_TYPE_DROPDOWN, 'value'),
          Input(ConnectionModal.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, connection_type: str, button_clicked: int, dash_logger: DashLogger):
    cnc = Cnc()
    if connection_type not in cnc.connection_options:
        return dash_logging(dash_logger, 'Connection type must be selected', logging.ERROR)
    if not device:
        return dash_logging(dash_logger, 'Device must be selected', logging.ERROR)
    cnc.set_connection(cnc.connection_options[connection_type])
    print(cnc.connection_options[connection_type], device)
    cnc.connection.connect(device)


@callback(Output(ConnectionStatus.ID, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          Input(Placeholder.ID, Placeholder.Fields.KEY))
def connect_selected_device(*button_clicks: list[int]):
    SimulatorDataManager().clear_saved_data()
    class_name = 'connection-status'
    is_connected_class_name = ''
    if Cnc().is_connected:
        is_connected_class_name = 'connected'
    return f'{class_name} {is_connected_class_name}'
