import dash_bootstrap_components
from dash import dcc

from components.general_components.input_card import create_card


def build_connection_devices_dropdown(devices_id: str, sync_button_id: str, connect_button_id: str):
    return [
        create_card('Select Device', [
            dcc.Loading(
                dcc.Dropdown([], id=devices_id, searchable=True,
                             style={'width': '230px', 'margin-right': '5px'}),
            ),
            dash_bootstrap_components.Button('Sync Devices', id=sync_button_id)
        ]),
        dash_bootstrap_components.Button('Connect', id=connect_button_id)
    ]
