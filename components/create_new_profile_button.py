import dash_bootstrap_components
from dash import callback, Output, Input, State
from dash_iconify import DashIconify

from components.consts import ProfileForm

plus_icon = DashIconify(icon='typcn:plus', width=45, id=ProfileForm.CREATE_NEW_BUTTON)
create_new_profile_button = dash_bootstrap_components.Button(plus_icon,
                                                             ProfileForm.CREATE_NEW_BUTTON,
                                                             style={'height': 'fit-content', 'border-radius': '100%'})


@callback(
    Output(ProfileForm.ID, 'is_open'),
    Input(ProfileForm.CREATE_NEW_BUTTON, 'n_clicks'),
    State(ProfileForm.ID, 'is_open'),
    prevent_initial_call=True)
def toggle_modal(button_clicked: int, is_open: bool):
    return not is_open
