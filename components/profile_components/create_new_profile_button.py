from dash import callback, Output, Input, State

from components.general_components.add_button import create_add_button
from components.profile_components.consts import ProfileForm

create_new_profile_button = create_add_button(button_id=ProfileForm.CREATE_NEW_BUTTON)


@callback(
    Output(ProfileForm.ID, 'is_open'),
    State(ProfileForm.ID, 'is_open'),
    Input(ProfileForm.CREATE_NEW_BUTTON, 'n_clicks'),
    Input(ProfileForm.SUBMIT_FORM, 'n_submit'),
    prevent_initial_call=True)
def toggle_create_new_profile_modal(is_open: bool, *buttons_clicked):
    return not is_open
