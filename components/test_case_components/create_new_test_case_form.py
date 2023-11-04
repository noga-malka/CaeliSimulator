import dash_bootstrap_components
from dash import html, dcc, callback, Output, Input, State

from assets.icons import TestCaseIcons
from components.consts import Placeholder
from components.general_components.input_card import build_string_input_card, create_card
from components.general_components.modal import create_modal
from components.test_case_components.consts import TestCaseForm
from database.database_manager import DatabaseManager
from models.test_case import TestCase
from utilities import validate_arguments


def build_profile_dropdown():
    return create_card('Select Profiles', [dash_bootstrap_components.InputGroup([
        dash_bootstrap_components.Select([],
                                         id=TestCaseForm.Inputs.PROFILE_DROPDOWN,
                                         placeholder='Profile Name',
                                         required=True),
        dash_bootstrap_components.Input(id=TestCaseForm.PROFILE_TIME_RANGE,
                                        type='number',
                                        placeholder='Run Time',
                                        required=True),
        dash_bootstrap_components.Button('Add Profile', id=TestCaseForm.ADD_PROFILE_BUTTON)
    ])])


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


@callback(Output(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'options'),
          Input(Placeholder.ID, Placeholder.Fields.CHILDREN))
def update_profiles_dropdown(*args):
    return [profile_name for profile_name in DatabaseManager().profile_manager.get_names()]


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


@callback(Output(TestCaseForm.PROFILE_STORE, 'data'),
          State(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'value'),
          State(TestCaseForm.PROFILE_TIME_RANGE, 'value'),
          State(TestCaseForm.PROFILE_STORE, 'data'),
          Input(TestCaseForm.ADD_PROFILE_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_test_case(profile_name: str, time_range: int, profiles: list, button_clicked: int):
    validate_arguments(profile_name)
    validate_arguments(time_range)
    profiles.append((profile_name, time_range))
    return profiles


@callback(Output(TestCaseForm.PROFILE_STORE, 'data', allow_duplicate=True),
          Input(TestCaseForm.CLEAR_PROFILES_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_test_case(button_clicked: int):
    validate_arguments(button_clicked)
    return []
