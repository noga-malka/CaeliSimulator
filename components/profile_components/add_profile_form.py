import dash_bootstrap_components
from dash import html, callback, Output, Input, State

from components.consts import Placeholder
from components.modal import create_modal
from components.profile_components.consts import ProfileForm
from components.input_card import build_number_input_card, build_string_input_card
from database.database_manager import DatabaseManager

from models.profile import Profile

add_profile_form = create_modal('Add Profile', ProfileForm.ID, [
    build_string_input_card('Profile Name', ProfileForm.Inputs.PROFILE_NAME),
    html.Div([
        build_number_input_card('Set Inspirium Time', ProfileForm.Inputs.INSPIRIUM_TIME, 0, 100),
        build_number_input_card('Set Inspirium Hold Time', ProfileForm.Inputs.INSPIRIUM_HOLD_TIME, 0,
                                100),
    ], className='flex'),
    html.Div([
        build_number_input_card('Set Expirium Time', ProfileForm.Inputs.EXPIRIUM_TIME, 0, 100),
        build_number_input_card('Set Expirium Hold Time', ProfileForm.Inputs.EXSPIRIUM_HOLD_TIME, 0,
                                100),
    ], className='flex'),
    html.Div([
        build_number_input_card('Set Tidal Volume', ProfileForm.Inputs.TIDAL_VOLUME, 0, 100),
        build_number_input_card('Set Profile Time Span', ProfileForm.Inputs.TIME_SPAN, 0, 100),
    ], className='flex'),
    dash_bootstrap_components.Button('Save', ProfileForm.ADD_BUTTON)
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
