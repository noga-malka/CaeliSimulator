import dash_bootstrap_components
from dash import html, dcc, callback, Output, Input, State
from dash.exceptions import PreventUpdate

from assets.icons import TestCaseIcons
from components.consts import Placeholder
from components.input_card import build_string_input_card, create_card
from components.modal import create_modal
from components.profile_components.consts import ProfileForm
from components.test_case_components.consts import TestCaseForm
from database.database_manager import DatabaseManager
from models.test_case import TestCase
from utilities import validate_arguments


def build_profile_dropdown():
    return create_card('Select Profiles', [
        dcc.Dropdown([], id=TestCaseForm.Inputs.PROFILE_DROPDOWN, searchable=True, style={'width': '230px'}),
    ])


add_test_case_form = create_modal('Add Test Case', TestCaseForm.ID, [
    build_string_input_card('Test Case Name', TestCaseForm.Inputs.TEST_CASE_NAME),
    build_profile_dropdown(),
    html.Div([], id=TestCaseForm.SELECTED_PROFILES,
             style={'margin-bottom': '10px', 'justify-content': 'center'},
             className='flex'),
    dash_bootstrap_components.Button('Save', TestCaseForm.ADD_BUTTON)

])


def get_already_selected_profiles(selected_profiles_children: dict):
    props = selected_profiles_children.get('props')
    if props:
        children = props.get('children')
        if children:
            return children
    return []


@callback(Output(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'options'),
          Input(Placeholder.ID, Placeholder.Fields.CHILDREN))
def update_profiles_dropdown(*args):
    return [profile_name for profile_name in DatabaseManager().profile_manager.profiles]


@callback(Output(TestCaseForm.SELECTED_PROFILES, 'children'),
          State(TestCaseForm.SELECTED_PROFILES, 'children'),
          Input(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'value'),
          prevent_initial_call=True)
def update_selected_profiles(already_selected: list, profile_to_add: str):
    validate_arguments(profile_to_add)
    new_badge = dash_bootstrap_components.Badge(profile_to_add, color='green', pill=True, style={'font-size': '15px'})
    if already_selected:
        return already_selected + [TestCaseIcons.RIGHT_ARROW, new_badge]
    return [new_badge]


def extract_profile_names(selected_profiles_children: list) -> list:
    profile_names = list()
    for component in selected_profiles_children:
        profile_name = component.get('props', {}).get('children')
        if profile_name:
            profile_names.append(profile_name)
    return profile_names


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS),
          State(TestCaseForm.Inputs.TEST_CASE_NAME, 'value'),
          State(TestCaseForm.SELECTED_PROFILES, 'children'),
          Input(TestCaseForm.ADD_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_test_case(test_case_name: str, selected_profiles_children: list, button_clicked: int):
    validate_arguments(button_clicked)
    profile_names = extract_profile_names(selected_profiles_children)
    new_test_case = TestCase(name=test_case_name, profile_names=profile_names)
    DatabaseManager().test_case_manager.add(new_test_case)
