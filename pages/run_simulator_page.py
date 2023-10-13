import dash
from dash import html

from components.simulator_components.simulator_buttons import simulator_buttons
from pages.consts import PageRoutes, PageTitles
from pages.default_page import generate_default_layout

dash.register_page(
    __name__,
    path=PageRoutes.RUN_SIMULATOR,
    title=PageTitles.RUN_SIMULATOR
)

layout = generate_default_layout(
    html.Div([
        html.Div([
            simulator_buttons,
        ], className='bg-secondary flex', style={'justify-content': 'center', 'flex-direction': 'column'}),
    ])
)
