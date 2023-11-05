import dash_bootstrap_components
from dash import callback, Input, Output

from assets.icons import TestCaseIcons
from components.general_components.grid import create_grid_card, create_grid
from components.test_case_components.consts import TestCaseGrid, TestCaseForm
from database.database_manager import DatabaseManager
from models.test_case import TestCase


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
          Input(TestCaseForm.SUBMIT_FORM, 'n_submit'))
def update_test_case_grid(button_clicked: int):
    cards = []
    for test_case in DatabaseManager().test_case_manager.get_instances():
        cards.append(create_grid_card(test_case.name, generate_test_case_details(test_case), True))
    return cards
