import dash_bootstrap_components
from dash import html

from components.simulator_components.consts import ButtonGroupIds, ConnectionStatus
from components.simulator_components.inputs.simulator import simulator_connection_modal, simulator_connect_button, \
    simulator_disconnect_button

control_buttons = html.Div([
    html.Div('', className='connection-status', id=ConnectionStatus.ID),
    dash_bootstrap_components.ButtonGroup([
        simulator_connect_button,
        simulator_disconnect_button,
    ], id=ButtonGroupIds.SETUP_SIMULATOR),
    simulator_connection_modal,
], className='bg-secondary flex-center flex-column')
