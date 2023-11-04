from dash import html, callback, Output, Input

from components.profile_components.consts import ProfileGrid, ProfileForm
from database.database_manager import DatabaseManager
from models.consts import FieldsDisplay
from models.profile import Profile


def generate_profile_details(profile: Profile):
    return [
        FieldsDisplay.inspirium_time.generate_detailed_component(profile.name, profile.inspirium_time),
        FieldsDisplay.inspirium_hold_time.generate_detailed_component(profile.name, profile.inspirium_hold_time),
        FieldsDisplay.expirium_time.generate_detailed_component(profile.name, profile.expirium_time),
        FieldsDisplay.expirium_hold_time.generate_detailed_component(profile.name, profile.expirium_hold_time),
        FieldsDisplay.tidal_volume.generate_detailed_component(profile.name, profile.tidal_volume),
    ]


def generate_profile_card(profile: Profile):
    return html.Div([
        html.Label(profile.name, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        html.Div(generate_profile_details(profile))
    ], className='grid-card')


profiles_grid = html.Div([], className='grid', id=ProfileGrid.ID)


@callback(Output(ProfileGrid.ID, 'children'),
          Input(ProfileForm.ADD_BUTTON, 'n_clicks'))
def update_profile_list(new_profile_button: int):
    return [generate_profile_card(profile) for profile in DatabaseManager().profile_manager.get_instances()]
