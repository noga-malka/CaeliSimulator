import dash
from dash import html

from components.simulator_components.display_live_data import live_data
from pages.consts import PageRoutes, PageTitles

dash.register_page(__name__, path=PageRoutes.RUN_SIMULATOR, title=PageTitles.RUN_SIMULATOR)

layout = html.Div([
    live_data,
])
