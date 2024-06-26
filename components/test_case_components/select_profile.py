import dash_bootstrap_components
from dash import callback, Output, Input, State

from components.consts import Placeholder
from components.general_components.input_card import create_card
from components.test_case_components.consts import TestCaseForm
from database.database_manager import DatabaseManager
from utilities import validate_arguments


def build_profile_dropdown():
    return create_card('Select Profiles',
                       [dash_bootstrap_components.InputGroup([
                           dash_bootstrap_components.Select([],
                                                            id=TestCaseForm.Inputs.PROFILE_DROPDOWN,
                                                            placeholder='Profile Name'),
                           dash_bootstrap_components.Input(id=TestCaseForm.PROFILE_TIME_RANGE,
                                                           type='number',
                                                           placeholder='Seconds',
                                                           min=0),
                           dash_bootstrap_components.Button('Add', id=TestCaseForm.ADD_PROFILE_BUTTON,
                                                            type='button'),
                           dash_bootstrap_components.Button('Clear', id=TestCaseForm.CLEAR_PROFILES_BUTTON,
                                                            type="button")
                       ])])


@callback(Output(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'options'),
          Input(Placeholder.ID, Placeholder.Fields.CHILDREN))
def update_select_profile_dropdown_options(profile_added):
    return DatabaseManager().profile_manager.get_names()


@callback(Output(TestCaseForm.PROFILE_STORE, 'data'),
          State(TestCaseForm.Inputs.PROFILE_DROPDOWN, 'value'),
          State(TestCaseForm.PROFILE_TIME_RANGE, 'value'),
          State(TestCaseForm.PROFILE_STORE, 'data'),
          Input(TestCaseForm.ADD_PROFILE_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_profile_to_test_case(profile_name: str, time_range: int, profiles: list, button_clicked: int):
    validate_arguments(profile_name)
    validate_arguments(time_range)
    if time_range > 0:
        profiles.append((profile_name, time_range))
    return profiles
