import dash_bootstrap_components
from dash import html, dcc, callback, Output, Input, State
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify

from assets.icons import RIGHT_ARROW
from components.consts import Placeholder
from components.input_card import build_string_input_card
from components.test_case_components.consts import TestCaseForm
from database.database_manager import DatabaseManager
from models.test_case import TestCase


def build_profile_dropdown():
    options = [profile_name for profile_name in DatabaseManager().profile_manager.profiles]
    return html.Div([
        html.Label('Select Profiles'),
        html.Hr(),
        html.Div([
            dcc.Dropdown(options, id=TestCaseForm.Inputs.PROFILE_DROPDOWN, searchable=True, style={'width': '230px'}),
            html.Div([], id=TestCaseForm.SELECTED_PROFILES, style={'margin-top': '10px', 'justify-content': 'center'},
                     className='flex')
        ], style={'justify-content': 'center', 'align-items': 'center', 'flex-direction': 'column'}, className='flex')
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content'})


add_test_case_form = html.Div([
    dash_bootstrap_components.Modal([
        dash_bootstrap_components.ModalHeader(html.H3('Add Test Case')),
        dash_bootstrap_components.ModalBody([
            build_string_input_card('Test Case Name', TestCaseForm.Inputs.TEST_CASE_NAME),
            build_profile_dropdown(),
            dash_bootstrap_components.Button('Save', TestCaseForm.ADD_BUTTON)
        ], style={'align-items': 'center', 'flex-direction': 'column'}, className='flex')]
        , id=TestCaseForm.ID, is_open=True)
])


def get_already_selected_profiles(selected_profiles_children: dict):
    props = selected_profiles_children.get('props')
    if props:
        children = props.get('children')
        if children:
            return children
    return []


@callback(Output(TestCaseForm.SELECTED_PROFILES, 'children'),
          State(TestCaseForm.SELECTED_PROFILES, 'children'),
          Input(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'value'),
          prevent_initial_call=True)
def update_selected_profiles(already_selected: list, profile_to_add: str):
    if not profile_to_add:
        raise PreventUpdate
    arrow_icon = DashIconify(icon=RIGHT_ARROW, width=25)
    new_badge = dash_bootstrap_components.Badge(profile_to_add, color='green', pill=True, style={'font-size': '15px'})
    if already_selected:
        return already_selected + [arrow_icon, new_badge]
    return [new_badge]


def extract_profile_names(selected_profiles_children: list) -> list:
    profile_names = list()
    for component in selected_profiles_children:
        profile_name = component.get('props', {}).get('children')
        if profile_name:
            profile_names.append(profile_name)
    return profile_names


@callback(Output(Placeholder.ID, 'n_clicks'),
          State(TestCaseForm.Inputs.TEST_CASE_NAME, 'value'),
          State(TestCaseForm.SELECTED_PROFILES, 'children'),
          Input(TestCaseForm.ADD_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_test_case(test_case_name: str, selected_profiles_children: list, button_clicked: int):
    profile_names = extract_profile_names(selected_profiles_children)
    new_test_case = TestCase(name=test_case_name, profile_names=profile_names)
    DatabaseManager().test_case_manager.add(new_test_case)
