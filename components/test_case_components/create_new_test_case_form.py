import dash_bootstrap_components
from dash import html, dcc, callback, Output, Input, State

from assets.icons import TestCaseIcons
from components.consts import Placeholder
from components.general_components.input_card import build_string_input_card
from components.general_components.modal import create_modal
from components.test_case_components.consts import TestCaseForm
from components.test_case_components.select_profile import build_profile_dropdown
from database.database_manager import DatabaseManager
from models.test_case import TestCase
from utilities import validate_arguments

add_test_case_form = create_modal('Add Test Case', TestCaseForm.ID, [
    dcc.Store(id=TestCaseForm.PROFILE_STORE, data=[]),
    build_string_input_card('Test Case Name', TestCaseForm.Inputs.TEST_CASE_NAME),
    build_profile_dropdown(),
    html.Div([], id=TestCaseForm.SELECTED_PROFILES,
             style={'margin-bottom': '10px', 'justify-content': 'center'},
             className='flex'),
    html.Div([
        dash_bootstrap_components.Button('Save', TestCaseForm.SAVE_TEST_CASE_BUTTON, className='margin'),
        dash_bootstrap_components.Button('Clear', TestCaseForm.CLEAR_PROFILES_BUTTON, className='margin')
    ], className='flex')
])


@callback(Output(TestCaseForm.SELECTED_PROFILES, 'children'),
          Output(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'value'),
          Output(TestCaseForm.PROFILE_TIME_RANGE, 'value'),
          Input(TestCaseForm.PROFILE_STORE, 'data'),
          prevent_initial_call=True)
def update_selected_profiles(profile_list: list):
    badges = []
    for profile_name, _ in profile_list:
        badges += [
            TestCaseIcons.RIGHT_ARROW,
            dash_bootstrap_components.Badge(profile_name, color='green', pill=True, style={'font-size': '15px'})
        ]
    return badges, '', ''


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS),
          State(TestCaseForm.Inputs.TEST_CASE_NAME, 'value'),
          State(TestCaseForm.PROFILE_STORE, 'data'),
          Input(TestCaseForm.SAVE_TEST_CASE_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_test_case(test_case_name: str, profiles_list: list, button_clicked: int):
    validate_arguments(button_clicked)
    new_test_case = TestCase(name=test_case_name, profile_names=profiles_list)
    DatabaseManager().test_case_manager.add(new_test_case)


@callback(Output(TestCaseForm.PROFILE_STORE, 'data', allow_duplicate=True),
          Input(TestCaseForm.CLEAR_PROFILES_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def clear_selected_profiles(button_clicked: int):
    validate_arguments(button_clicked)
    return []
