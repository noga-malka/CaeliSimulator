import dash_bootstrap_components
from dash import html
from dash_iconify import DashIconify

from assets.icons import ControlButtonIcons
from components.simulator_components.bluetooth_connection_form import bluetooth_modal
from components.simulator_components.consts import ButtonIds, ButtonGroupIds
from components.simulator_components.create_bluetooth_connection_button import bluetooth_modal_button
from components.simulator_components.utilities import create_control_button

control_buttons = html.Div([
    dash_bootstrap_components.ButtonGroup([
        bluetooth_modal_button,
        create_control_button('Connect To Serial', ButtonIds.SERIAL, ControlButtonIcons.SERIAL),
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
