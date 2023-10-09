from dash import callback, Output, Input, State, html
from dash_iconify import DashIconify

from components.profile_components.consts import ProfileForm

plus_icon = DashIconify(icon='subway:add', width=45, id=ProfileForm.CREATE_NEW_BUTTON, color='green')
create_new_profile_button = html.Div(plus_icon, id=ProfileForm.CREATE_NEW_BUTTON,
                                     style={'height': 'fit-content', 'border-radius': '100%'})


@callback(
    Output(ProfileForm.ID, 'is_open'),
    State(ProfileForm.ID, 'is_open'),
    Input(ProfileForm.CREATE_NEW_BUTTON, 'n_clicks'),
    Input(ProfileForm.ADD_BUTTON, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open