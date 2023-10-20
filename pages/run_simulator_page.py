import dash
from dash import html

from components.simulator_components.select_test_case_form import test_case_modal
from components.simulator_components.simulator_buttons import simulator_buttons
from pages.consts import PageRoutes, PageTitles

dash.register_page(
    __name__,
    path=PageRoutes.RUN_SIMULATOR,
    title=PageTitles.RUN_SIMULATOR
)

layout = html.Div([
    html.Div([
        test_case_modal,
        simulator_buttons,
    ], className='bg-secondary flex-center flex-column'),
])
