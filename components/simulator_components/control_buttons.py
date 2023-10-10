import dash_bootstrap_components
from dash import html

from assets.icons import ControlButtonIcons
from components.simulator_components.connection_form import bluetooth_modal
from components.simulator_components.consts import ButtonIds, ButtonGroupIds, ConnectionStatus
from components.simulator_components.create_connection_button import connect_to_simulator_modal_button
from components.simulator_components.utilities import create_control_button

control_buttons = html.Div([
    html.Div('', className='connection-status', id=ConnectionStatus.ID),
    dash_bootstrap_components.ButtonGroup([
        connect_to_simulator_modal_button,
        create_control_button('Disconnect From Simulator', ButtonIds.DISCONNECT_FROM_SIMULATOR,
                              ControlButtonIcons.DISCONNECT_FROM_SIMULATOR),
        create_control_button('Select Test Case', ButtonIds.TEST_CASE, ControlButtonIcons.SELECT_TEST_CASE)
    ], id=ButtonGroupIds.SETUP_SIMULATOR),
    dash_bootstrap_components.ButtonGroup([
        create_control_button('On', ButtonIds.Simulator.ON, ControlButtonIcons.ON),
        create_control_button('Run', ButtonIds.Simulator.RUN, ControlButtonIcons.RUN),
        create_control_button('Homing', ButtonIds.Simulator.HOMING, ControlButtonIcons.HOMING),
        create_control_button('Pause', ButtonIds.Simulator.PAUSE, ControlButtonIcons.PAUSE),
        create_control_button('Off', ButtonIds.Simulator.OFF, ControlButtonIcons.OFF),
    ], id=ButtonGroupIds.SIMULATOR_CONTROLS),
    bluetooth_modal,
], className='bg-secondary flex', style={'justify-content': 'center', 'flex-direction': 'column'})
