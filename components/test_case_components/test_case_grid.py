import dash_bootstrap_components
from dash import html, callback, Input, Output

from assets.icons import TestCaseIcons
from components.test_case_components.consts import TestCaseGrid, TestCaseForm
from database.database_manager import DatabaseManager
from models.test_case import TestCase


def generate_test_case_details(test_case: TestCase):
    profiles_flow = list()
    for profile_name, profile_run_time in test_case.profile_names:
        profiles_flow += [
            TestCaseIcons.DOWN_ARROW,
            dash_bootstrap_components.Badge(f'"{profile_name}" for {profile_run_time}s',
                                            pill=True,
                                            className='margin')
        ]
    return profiles_flow


def generate_test_case_card(test_case: TestCase):
    return html.Div([
        html.Label(test_case.name, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        html.Div(generate_test_case_details(test_case), className='flex-column', style={'align-items': 'center'}),
    ], className='grid-card')


test_case_grid = html.Div([], className='grid', id=TestCaseGrid.ID)


@callback(Output(TestCaseGrid.ID, 'children'),
          Input(TestCaseForm.SAVE_TEST_CASE_BUTTON, 'n_clicks'))
def update_profile_list(new_profile_button: int):
    return [generate_test_case_card(test_case) for test_case in DatabaseManager().test_case_manager.get_instances()]
