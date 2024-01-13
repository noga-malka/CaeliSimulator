import dash_bootstrap_components
from dash_iconify import DashIconify


def create_icon_button(title: str, button_id: str, icon: DashIconify, color: str = 'primary'):
    """
    :param title: the button's text
    :param button_id: unique id of the component
    :param icon: DashIconify object to add at the beginning of the button
    :param color: 's color
    :return: dash_bootstrap_components.Button component
    """
    return dash_bootstrap_components.Button([icon, title],
                                            id=button_id,
                                            outline=True,
                                            color=color,
                                            className='control-buttons')
