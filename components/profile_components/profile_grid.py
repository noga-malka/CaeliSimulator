from dash import callback, Output, Input

from components.general_components.grid import create_grid_card, create_grid
from components.profile_components.consts import ProfileGrid, ProfileForm
from database.database_manager import DatabaseManager
from models.consts import FieldsDisplay
from models.profile import Profile


def generate_profile_details(profile: Profile) -> list:
    return [
        FieldsDisplay.inspirium_time.generate_detailed_component(profile.name, profile.inspirium_time),
        FieldsDisplay.inspirium_hold_time.generate_detailed_component(profile.name, profile.inspirium_hold_time),
        FieldsDisplay.expirium_time.generate_detailed_component(profile.name, profile.expirium_time),
        FieldsDisplay.expirium_hold_time.generate_detailed_component(profile.name, profile.expirium_hold_time),
        FieldsDisplay.tidal_volume.generate_detailed_component(profile.name, profile.tidal_volume),
    ]


profiles_grid = create_grid(ProfileGrid.ID)


@callback(Output(ProfileGrid.ID, 'children'),
          Input(ProfileForm.SUBMIT_FORM, 'n_submit'))
def update_profile_grid(button_clicked: int):
    cards = []
    for profile in DatabaseManager().profile_manager.get_instances():
        cards.append(create_grid_card(profile.name, generate_profile_details(profile), False))
    return cards
