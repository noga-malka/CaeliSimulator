import dash_bootstrap_components
from dash import callback, Input, Output, ALL, callback_context

from assets.icons import TestCaseIcons
from components.consts import Placeholder
from components.general_components.grid import create_grid_card, create_grid
from components.test_case_components.consts import TestCaseGrid
from database.database_manager import DatabaseManager
from models.test_case import TestCase
from utilities import validate_arguments


def generate_test_case_details(test_case: TestCase) -> list:
    profiles_flow = []
    for profile_name, profile_run_time in test_case.profile_names:
        profiles_flow += [
            TestCaseIcons.DOWN_ARROW,
            dash_bootstrap_components.Badge(f'"{profile_name}" for {profile_run_time}s', pill=True)
        ]
    return profiles_flow


test_case_grid = create_grid(TestCaseGrid.ID)


@callback(Output(TestCaseGrid.ID, 'children'),
          Input(Placeholder.ID, Placeholder.Fields.TITLE),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS))
def update_test_case_grid(*inputs: list):
    cards = []
    for test_case in DatabaseManager().test_case_manager.get_instances():
        cards.append(create_grid_card(test_case.name, generate_test_case_details(test_case), 'test_case_manager', True))
    return cards


@callback(Output(Placeholder.ID, Placeholder.Fields.TITLE),
          Input({'index': ALL, 'type': 'test_case_manager'}, 'n_clicks'),
          prevent_initial_call=True)
def delete_profile(button_clicked: list[int]):
    validate_arguments(*button_clicked)
    card_id_to_remove = callback_context.triggered_id['index']
    DatabaseManager().test_case_manager.remove(card_id_to_remove)
