import dash_bootstrap_components
from dash import html
from dash_iconify import DashIconify

from assets.icons import ControlButtonIcons


def create_control_button(title: str, icon: DashIconify):
    return dash_bootstrap_components.Button([icon, title], outline=True, color='primary', className='control-buttons')


control_buttons = html.Div(
    dash_bootstrap_components.ButtonGroup([
        create_control_button('Connect To Bluetooth', ControlButtonIcons.BLUETOOTH),
        create_control_button('Connect To Serial', ControlButtonIcons.SERIAL),
        create_control_button('Select Test Case', ControlButtonIcons.SELECT_TEST_CASE),
        create_control_button('On', ControlButtonIcons.ON),
        create_control_button('Run', ControlButtonIcons.PLAY),
        create_control_button('Homing', ControlButtonIcons.HOMING),
        create_control_button('Pause', ControlButtonIcons.PAUSE),
        create_control_button('Off', ControlButtonIcons.OFF),
    ]), className='bg-secondary flex', style={'justify-content': 'center'})
