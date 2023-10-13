import dash_bootstrap_components
from dash import html, callback, Input, Output, ALL, callback_context
from dash_iconify import DashIconify

from assets import icons
from assets.icons import TestCaseIcons
from cnc.cnc import Cnc
from cnc.packets.sync_test_case_packet import SyncTestCasePacket
from components.consts import Placeholder
from components.simulator_components.consts import SelectTestCaseModal
from components.test_case_components.consts import TestCaseGrid, TestCaseForm
from database.database_manager import DatabaseManager
from models.test_case import TestCase
from utilities import validate_arguments


def generate_test_case_details(test_case: TestCase):
    profiles_flow = list()
    for profile_name in test_case.profile_names:
        profiles_flow += [
            TestCaseIcons.DOWN_ARROW,
            dash_bootstrap_components.Badge(profile_name, pill=True, style={'margin': '5px'})
        ]
    return profiles_flow


def generate_test_case_card(test_case: TestCase):
    return html.Div([
        html.Label(test_case.name, className='flex',
                   style={'justify-content': 'center', 'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(style={'margin': '5px', 'width': '100%'}),
        html.Div(generate_test_case_details(test_case),
                 style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
        dash_bootstrap_components.Button('Send',
                                         id={'id': TestCaseGrid.SEND_TEST_CASE_BUTTON, 'type': test_case.name})
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content', 'border': '1px solid',
              'border-radius': '10px', 'display': 'flex', 'flex-direction': 'column'})


test_case_grid = html.Div([],
                          style={'display': 'grid', 'grid-gap': '10px',
                                 'grid-template-columns': '200px 200px 200px 200px',
                                 'height': 'fit-content'}, id=TestCaseGrid.ID)


@callback(Output(TestCaseGrid.ID, 'children'),
          Input(TestCaseForm.ADD_BUTTON, 'n_clicks'))
def update_profile_list(new_profile_button: int):
    return [generate_test_case_card(test_case) for test_case in DatabaseManager().test_case_manager.test_cases.values()]


@callback(Output(Placeholder.ID, Placeholder.Fields.CONTENT_EDITABLE),
          Input({'id': TestCaseGrid.SEND_TEST_CASE_BUTTON, 'type': ALL}, 'n_clicks'),
          prevent_initial_call=True)
def send_test_case(send_buttons_clicked: list[int]):
    validate_arguments(*send_buttons_clicked)
    test_case_name = callback_context.triggered_id['type']
    test_case = DatabaseManager().test_case_manager.test_cases[test_case_name]
    Cnc().send_command(SyncTestCasePacket(test_case))
