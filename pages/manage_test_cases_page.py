import dash
from dash import html

from components.test_case_components.create_new_test_case_button import create_new_test_case_button
from components.test_case_components.create_new_test_case_form import add_test_case_form
from components.test_case_components.test_case_grid import test_case_grid
from pages.consts import PageRoutes, PageTitles

dash.register_page(__name__, path=PageRoutes.TEST_CASE_MANAGER, title=PageTitles.TEST_CASE_MANAGER)

layout = html.Div([
    test_case_grid, create_new_test_case_button, add_test_case_form
], className='flex-column', style={'align-items': 'center', 'margin-top': '10px'})
