import dash_bootstrap_components
from dash import callback, Output, State, Input
from dash import dcc

from cnc.cnc import Cnc
from components.consts import Placeholder
from components.input_card import create_card
from components.modal import create_modal
from components.simulator_components.consts import ConnectionModal, ConnectionStatus, ButtonIds
from connections.connections import Connections


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
        dcc.Dropdown([connection.name for connection in Connections],
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
    if connection_type in Connections.__members__:
        Connections[connection_type].value.discover()
        return Connections[connection_type].value.discovered_devices
    return []


@callback(Output(Placeholder.ID, Placeholder.Fields.CLASS_NAME),
          State(ConnectionModal.DEVICE_DROPDOWN, 'value'),
          State(ConnectionModal.CONNECTION_TYPE_DROPDOWN, 'value'),
          Input(ConnectionModal.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True)
def connect_selected_device(device: str, connection_type: str, button_clicked: int):
    if connection_type in Connections.__members__:
        cnc = Cnc()
        cnc.set_connection(Connections[connection_type].value)
        cnc.connection.connect(device)


@callback(Output(ConnectionStatus.ID, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.CLASS_NAME),
          Input(Placeholder.ID, Placeholder.Fields.DIR),
          prevent_initial_call=True)
def connect_selected_device(*button_clicks: list[int]):
    class_name = 'connection-status'
    is_connected_class_name = ''
    if Cnc().connection.is_connected:
        is_connected_class_name = 'connected'
    return f'{class_name} {is_connected_class_name}'
