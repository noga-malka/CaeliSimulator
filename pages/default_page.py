from dash import html

from components.navigation_bar import navigation_bar
from components.placeholder import placeholder
from components.title import title


def generate_default_layout(layout):
    return html.Div([
        title,
        placeholder,
        html.Div([navigation_bar, layout],
                 className='flex', style={'height': '100vh'})])
