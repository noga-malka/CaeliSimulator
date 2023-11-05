from dash import callback, Output, Input, State

from components.general_components.add_button import create_add_button
from components.test_case_components.consts import TestCaseForm

create_new_test_case_button = create_add_button(button_id=TestCaseForm.CREATE_NEW_BUTTON)


@callback(
    Output(TestCaseForm.ID, 'is_open'),
    State(TestCaseForm.ID, 'is_open'),
    Input(TestCaseForm.CREATE_NEW_BUTTON, 'n_clicks'),
    Input(TestCaseForm.SUBMIT_FORM, 'n_submit'),
    prevent_initial_call=True)
def toggle_create_new_test_case_modal(is_open: bool, *buttons_clicked):
    return not is_open
