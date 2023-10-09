from dash import callback, Output, Input, State, html
from dash_iconify import DashIconify

from components.profile_components.consts import ProfileForm
from components.test_case_components.consts import TestCaseForm

plus_icon = DashIconify(icon='subway:add', width=45, id=TestCaseForm.CREATE_NEW_BUTTON, color='green')
create_new_test_case_button = html.Div(plus_icon, id=TestCaseForm.CREATE_NEW_BUTTON,
                                       style={'height': 'fit-content', 'border-radius': '100%'})


@callback(
    Output(TestCaseForm.ID, 'is_open'),
    State(TestCaseForm.ID, 'is_open'),
    Input(TestCaseForm.CREATE_NEW_BUTTON, 'n_clicks'),
    Input(TestCaseForm.ADD_BUTTON, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open
