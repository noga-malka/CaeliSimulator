from dash import html
from dash_iconify import DashIconify


def create_add_button(button_id: str) -> html.Div:
    """
    create a green round plus sign button

    :param button_id: button id to use
    :return: icon button component
    """
    plus_icon = DashIconify(icon='subway:add', width=45, id=button_id, color='green')
    return html.Div(plus_icon, id=button_id, style={'height': 'fit-content', 'border-radius': '100%'})
