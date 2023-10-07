import dash_bootstrap_components
from dash import html, callback, Output, Input, State

from components.consts import ProfileForm, Placeholder
from components.input_card import build_number_input_card_component, build_string_input_card_component
from database.database_manager import DatabaseManager

from models.profile import Profile

add_profile_form = html.Div([
    dash_bootstrap_components.Modal([
        dash_bootstrap_components.ModalHeader(html.H3('Add Profile')),
        dash_bootstrap_components.ModalBody([
            build_string_input_card_component('Profile Name', ProfileForm.Inputs.PROFILE_NAME),
            html.Div([
                build_number_input_card_component('Set Inspirium Time', ProfileForm.Inputs.INSPIRIUM_TIME, 0, 100),
                build_number_input_card_component('Set Inspirium Hold Time', ProfileForm.Inputs.INSPIRIUM_HOLD_TIME, 0,
                                                  100),
            ], className='flex'),
            html.Div([
                build_number_input_card_component('Set Expirium Time', ProfileForm.Inputs.EXPIRIUM_TIME, 0, 100),
                build_number_input_card_component('Set Expirium Hold Time', ProfileForm.Inputs.EXSPIRIUM_HOLD_TIME, 0,
                                                  100),
            ], className='flex'),
            html.Div([
                build_number_input_card_component('Set Tidal Volume', ProfileForm.Inputs.TIDAL_VOLUME, 0, 100),
                build_number_input_card_component('Set Profile Time Span', ProfileForm.Inputs.TIME_SPAN, 0, 100),
            ], className='flex'),
            dash_bootstrap_components.Button('Save', ProfileForm.ADD_BUTTON)
        ], style={'align-items': 'center', 'flex-direction': 'column'}, className='flex')]
        , id=ProfileForm.ID)
])


@callback(Output(Placeholder.ID, 'children'),
          State(ProfileForm.Inputs.PROFILE_NAME, 'value'),
          State(ProfileForm.Inputs.INSPIRIUM_TIME, 'value'),
          State(ProfileForm.Inputs.INSPIRIUM_HOLD_TIME, 'value'),
          State(ProfileForm.Inputs.EXPIRIUM_TIME, 'value'),
          State(ProfileForm.Inputs.EXSPIRIUM_HOLD_TIME, 'value'),
          State(ProfileForm.Inputs.TIDAL_VOLUME, 'value'),
          State(ProfileForm.Inputs.TIME_SPAN, 'value'),
          Input(ProfileForm.ADD_BUTTON, 'n_clicks'),
          prevent_initial_call=True)
def add_new_profile(name: str,
                    inspirium_time: int,
                    inspirium_hold_time: int,
                    expirium_time: int,
                    expirium_hold_time: int,
                    tidal_volume: int,
                    time_span: int,
                    button_clicked: int):
    new_profile = Profile(name=name,
                          inspirium_time=inspirium_time,
                          inspirium_hold_time=inspirium_hold_time,
                          expirium_time=expirium_time,
                          expirium_hold_time=expirium_hold_time,
                          tidal_volume=tidal_volume,
                          time_span=time_span)
    DatabaseManager().profile_manager.add(new_profile)
