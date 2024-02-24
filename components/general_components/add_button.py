from dash import html
from dash_iconify import DashIconify


def create_bottom_grid_button(button_id: str, icon: str = 'subway:add') -> html.Div:
    """
    create a green round button

    :param button_id: button id to use
    :param icon: the icon string to create
    :return: icon button component
    """
    plus_icon = DashIconify(icon=icon, width=45, id=button_id, color='green')
    return html.Div(plus_icon, id=button_id, style={'height': 'fit-content', 'borderRadius': '100%'},
                    className='flex-center')
