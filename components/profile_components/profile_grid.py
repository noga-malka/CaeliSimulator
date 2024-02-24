from dash import callback, Output, Input, ALL, callback_context

from components.consts import Placeholder
from components.data_display_components.consts import CardIdType
from components.general_components.grid import create_grid_card, create_grid
from components.profile_components.consts import ProfileGrid
from database.database_manager import DatabaseManager
from models.consts import FieldsDisplay
from models.profile import Profile
from utilities import validate_arguments


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
          Input(Placeholder.ID, Placeholder.Fields.CHILDREN),
          Input(Placeholder.ID, Placeholder.Fields.TAB_INDEX))
def update_profile_grid(*button_clicked: int):
    cards = []
    for profile in DatabaseManager().profile_manager.get_instances():
        cards.append(create_grid_card(profile.name, generate_profile_details(profile), False))
    return cards


@callback(Output(Placeholder.ID, Placeholder.Fields.TAB_INDEX),
          Input({'index': ALL, 'type': CardIdType.DELETE}, 'n_clicks'),
          prevent_initial_call=True)
def delete_profile(button_clicked: list[int]):
    validate_arguments(*button_clicked)
    card_id_to_remove = callback_context.triggered_id['index']
    DatabaseManager().profile_manager.remove(card_id_to_remove)
