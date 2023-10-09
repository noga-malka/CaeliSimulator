import dash_bootstrap_components
from dash_iconify import DashIconify


def create_control_button(title: str, button_id: str, icon: DashIconify):
    return dash_bootstrap_components.Button([icon, title], id=button_id, outline=True, color='primary',
                                            className='control-buttons')

