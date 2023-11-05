import dash_bootstrap_components
from dash import callback, Output, Input, State

from components.consts import Placeholder
from components.general_components.input_card import build_string_input_card
from components.general_components.modal import create_modal
from components.profile_components.consts import ProfileForm
from database.database_manager import DatabaseManager
from models.consts import FieldsDisplay
from models.field import ProfileField
from models.profile import Profile
from utilities import validate_arguments


def generate_field_column(field_type: ProfileField):
    return dash_bootstrap_components.Col(field_type.generate_input_component())


add_profile_form = create_modal('Add Profile', ProfileForm.ID, [
    dash_bootstrap_components.Form([
        dash_bootstrap_components.Row([
            dash_bootstrap_components.Col(build_string_input_card('Profile Name', ProfileForm.Inputs.PROFILE_NAME)),
            generate_field_column(FieldsDisplay.tidal_volume)
        ]),
        dash_bootstrap_components.Row([
            generate_field_column(FieldsDisplay.inspirium_time),
            generate_field_column(FieldsDisplay.inspirium_hold_time),
        ]),
        dash_bootstrap_components.Row([
            generate_field_column(FieldsDisplay.expirium_time),
            generate_field_column(FieldsDisplay.expirium_hold_time),
        ]),
        dash_bootstrap_components.Row(
            dash_bootstrap_components.Col(dash_bootstrap_components.Button('Save'), className='flex-center')
        )
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
