import time

import dash_bootstrap_components
from dash import callback, Output, Input, State
from dash import dcc

from cnc.cnc import Cnc
from cnc.consts import Commands
from cnc.packets.command_packet import CommandPacket
from cnc.packets.sync_test_case_packet import SyncTestCasePacket
from components.consts import Placeholder
from components.input_card import create_card
from components.modal import create_modal
from components.simulator_components.consts import SelectTestCaseModal, ButtonIds
from database.database_manager import DatabaseManager
from simulator_data_manager.packet_type import PacketType


def build_devices_dropdown():
    return create_card('Select Test Case', [
        dcc.Dropdown([], id=SelectTestCaseModal.TEST_CASE_DROPDOWN, searchable=True,
                     style={'width': '230px', 'margin-right': '5px'}),
    ])


test_case_modal = create_modal('Select Test Case', SelectTestCaseModal.ID, [
    build_devices_dropdown(),
    dash_bootstrap_components.Button('Send', id=SelectTestCaseModal.SEND_TEST_CASE)
])


@callback(
    Output(SelectTestCaseModal.ID, 'is_open'),
    State(SelectTestCaseModal.ID, 'is_open'),
    Input(SelectTestCaseModal.SEND_TEST_CASE, 'n_clicks'),
    Input(ButtonIds.Simulator.RUN, 'n_clicks'),
    prevent_initial_call=True)
def toggle_modal(is_open: bool, *buttons_clicked):
    return not is_open


@callback(Output(Placeholder.ID, Placeholder.Fields.CLASS_NAME),
          State(SelectTestCaseModal.TEST_CASE_DROPDOWN, 'value'),
          Input(SelectTestCaseModal.SEND_TEST_CASE, 'n_clicks'),
          prevent_initial_call=True)
def send_test_case_to_simulator(test_case_name: str, send_button: int):
    if test_case_name:
        test_case = DatabaseManager().test_case_manager.test_cases[test_case_name]
        PacketType.BreathParams.value.event.clear()
        Cnc().send_command(SyncTestCasePacket(test_case))
        PacketType.BreathParams.value.event.wait()
        Cnc().send_command(CommandPacket(Commands.RUN))


@callback(Output(SelectTestCaseModal.TEST_CASE_DROPDOWN, 'options'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS))
def update_test_cases_dropdown(*args):
    return [test_case_name for test_case_name in DatabaseManager().test_case_manager.test_cases]
