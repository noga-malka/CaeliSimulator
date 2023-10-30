import dash
from dash import html

from components.simulator_components.display_live_data import live_data
from components.simulator_components.progress_bar import test_case_progress_bar
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
    test_case_progress_bar,
    live_data,
])
