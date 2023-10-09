import dash
from dash import html

from components.test_case_components.create_new_test_case_form import add_test_case_form
from components.test_case_components.test_case_grid import test_case_grid
from pages.consts import PageRoutes, PageTitles
from pages.default_page import generate_default_layout

dash.register_page(
    __name__,
    path=PageRoutes.MANAGE_TEST_CASES,
    title=PageTitles.MANAGE_TEST_CASES
)

layout = generate_default_layout(
    html.Div([
        test_case_grid,
        add_test_case_form,
    ])
)
