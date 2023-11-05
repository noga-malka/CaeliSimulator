import dash_bootstrap_components
from dash import html, callback, Output, Input, State

from components.consts import Placeholder
from components.general_components.input_card import build_string_input_card
from components.general_components.modal import create_modal
from components.profile_components.consts import ProfileForm
from database.database_manager import DatabaseManager
from models.consts import FieldsDisplay
from models.profile import Profile
from utilities import validate_arguments

add_profile_form = create_modal('Add Profile', ProfileForm.ID, [
    dash_bootstrap_components.Form([
        build_string_input_card('Profile Name', ProfileForm.Inputs.PROFILE_NAME),
        html.Div([
            FieldsDisplay.inspirium_time.generate_input_component(),
            FieldsDisplay.inspirium_hold_time.generate_input_component(),
        ], className='flex'),
        html.Div([
            FieldsDisplay.expirium_time.generate_input_component(),
            FieldsDisplay.expirium_hold_time.generate_input_component(),
        ], className='flex'),
        html.Div([
            FieldsDisplay.tidal_volume.generate_input_component(),
        ], className='flex'),
        dash_bootstrap_components.Button('Save')
    ], id=ProfileForm.SUBMIT_FORM)])


@callback(Output(Placeholder.ID, Placeholder.Fields.CHILDREN),
          State(ProfileForm.Inputs.PROFILE_NAME, 'value'),
          State(ProfileForm.Inputs.INSPIRIUM_TIME, 'value'),
          State(ProfileForm.Inputs.INSPIRIUM_HOLD_TIME, 'value'),
          State(ProfileForm.Inputs.EXPIRIUM_TIME, 'value'),
          State(ProfileForm.Inputs.EXSPIRIUM_HOLD_TIME, 'value'),
          State(ProfileForm.Inputs.TIDAL_VOLUME, 'value'),
          Input(ProfileForm.SUBMIT_FORM, 'n_submit'),
          prevent_initial_call=True)
def add_new_profile(name: str,
                    inspirium_time: int,
                    inspirium_hold_time: int,
                    expirium_time: int,
                    expirium_hold_time: int,
                    tidal_volume: int,
                    button_clicked: int):
    validate_arguments(button_clicked)
    new_profile = Profile(name=name,
                          inspirium_time=inspirium_time,
                          inspirium_hold_time=inspirium_hold_time,
                          expirium_time=expirium_time,
                          expirium_hold_time=expirium_hold_time,
                          tidal_volume=tidal_volume)
    DatabaseManager().profile_manager.add(new_profile)
