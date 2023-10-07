import dash_bootstrap_components
from dash import html, callback, Input, Output

from components.consts import TestCaseGrid
from database.database_manager import DatabaseManager
from models.test_case import TestCase


def generate_test_case_details(test_case: TestCase):
    return [dash_bootstrap_components.Badge(profile_name, pill=True) for profile_name in test_case.profile_names]


def generate_test_case_card(test_case: TestCase):
    return html.Div([
        html.Label(test_case.name, className='flex',
                   style={'justify-content': 'center', 'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(style={'margin': '5px'}),
        html.Div(generate_test_case_details(test_case))
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content', 'border': '1px solid',
              'border-radius': '10px'})


test_case_grid = html.Div(
    [generate_test_case_card(test_case) for test_case in DatabaseManager().test_case_manager.test_cases.values()],
    style={'display': 'grid', 'grid-gap': '10px',
           'grid-template-columns': '200px 200px 200px 200px',
           'height': 'fit-content'}, id=TestCaseGrid.ID)
