import dash_bootstrap_components
from dash import callback, Output, State, Input
from dash import dcc

from cnc.cnc import Cnc
from components.consts import Placeholder
from components.input_card import create_card
from components.modal import create_modal
from components.simulator_components.consts import ConnectionModal, ConnectionStatus
from connections.bluetooth_connection import BluetoothConnection


def build_bluetooth_devices_dropdown():
    return create_card('Select Device', [
        dcc.Loading(
            dcc.Dropdown([], id=ConnectionModal.DEVICE_DROPDOWN, searchable=True,
                         style={'width': '230px', 'margin-right': '5px'}),
        ),
        dash_bootstrap_components.Button('Sync Devices', id=ConnectionModal.SYNC_DEVICES)
    ])


bluetooth_modal = create_modal('Connect to Bluetooth Device', ConnectionModal.ID, [
    build_bluetooth_devices_dropdown(),
    dash_bootstrap_components.Button('Connect', id=ConnectionModal.CONNECT_DEVICE)
])


@callback(Output(ConnectionModal.DEVICE_DROPDOWN, 'options'),
          Input(ConnectionModal.SYNC_DEVICES, 'n_clicks'))
def sync_bluetooth_devices(sync_button_clicked):
    connection = BluetoothConnection()
    connection.discover()
    return connection.discovered_devices


@callback(Output(Placeholder.ID, 'className'),
          State(ConnectionModal.DEVICE_DROPDOWN, 'value'),
          Input(ConnectionModal.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True)
def connect_selected_device(mac_address: str, button_clicked: int):
    cnc = Cnc()
    cnc.set_connection(BluetoothConnection())
    cnc.connection.connect(mac_address)
