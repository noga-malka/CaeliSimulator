from dash import html

from components.navigation_bar import navigation_bar
from components.placeholder import placeholder
from components.simulator_components.control_buttons import control_buttons
from components.title import title


def generate_default_layout(layout):
    return html.Div([
        title,
        placeholder,
        html.Div([navigation_bar,
                  html.Div([control_buttons, layout], style={'width': '100%'})],
                 className='flex', style={'height': '100vh'})])
