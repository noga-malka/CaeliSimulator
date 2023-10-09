import dash_bootstrap_components
from dash import dcc
from dash import callback, Output, State, Input

from components.input_card import create_card
from components.modal import create_modal
from components.simulator_components.consts import BluetoothModal
from connections.bluetooth_connection import BluetoothConnection


def build_bluetooth_devices_dropdown():
    return create_card('Select Device', [
        dcc.Loading(
            dcc.Dropdown([], id=BluetoothModal.DEVICE_DROPDOWN, searchable=True,
                         style={'width': '230px', 'margin-right': '5px'}),
        ),
        dash_bootstrap_components.Button('Sync Devices', id=BluetoothModal.SYNC_DEVICES)
    ])


bluetooth_modal = create_modal('Connect to Bluetooth Device', BluetoothModal.ID, [
    build_bluetooth_devices_dropdown(),
    dash_bootstrap_components.Button('Connect', id=BluetoothModal.CONNECT_DEVICE)
])


@callback(Output(BluetoothModal.DEVICE_DROPDOWN, 'options'),
          Input(BluetoothModal.SYNC_DEVICES, 'n_clicks'))
def sync_bluetooth_devices(sync_button_clicked):
    connection = BluetoothConnection()
    connection.discover()
    return connection.discovered_devices
