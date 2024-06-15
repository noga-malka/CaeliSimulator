import dash_bootstrap_components
from dash import Output, Input, State
from dash import dcc
from dash_extensions.enrich import callback, DashLogger

from cnc.consts import Commands
from cnc.no_connection_open_exception import NoConnectionOpenException
from cnc.packets.no_payload_packet import NoPayloadPacket
from cnc.packets.sync_test_case_packet import SyncTestCasePacket
from cnc.serial_cnc import SerialCnc
from components.consts import Placeholder
from components.general_components.input_card import create_card
from components.general_components.modal import create_modal
from components.simulator_components.consts import SelectTestCaseModal, ButtonIds, ProgressBar
from database.database_manager import DatabaseManager
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import ui_logger


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


@callback(Output(ProgressBar.CURRENT_TEST_CASE, 'data'),
          State(SelectTestCaseModal.TEST_CASE_DROPDOWN, 'value'),
          Input(SelectTestCaseModal.SEND_TEST_CASE, 'n_clicks'),
          prevent_initial_call=True, log=True)
def send_test_case_to_simulator(test_case_name: str, send_button: int, dash_logger: DashLogger):
    if test_case_name:
        breath_packet_event = SimulatorDataManager().get_event(PacketHeaders.BREATH_PARAMETERS)
        breath_packet_event.clear()
        test_case = DatabaseManager().test_case_manager.get(test_case_name)
        try:
            SerialCnc().send_packet(SyncTestCasePacket(test_case))
            breath_packet_event.wait(timeout=3)
            if breath_packet_event.is_set():
                SerialCnc().send_packet(NoPayloadPacket(Commands.RUN))
                return test_case.profile_names
            else:
                return ui_logger(dash_logger, 'Can not load test case. No BreathParams command received from device')
        except NoConnectionOpenException as exception:
            return ui_logger(dash_logger, exception)


@callback(Output(SelectTestCaseModal.TEST_CASE_DROPDOWN, 'options'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS))
def update_test_cases_dropdown(*args):
    return [test_case_name for test_case_name in DatabaseManager().test_case_manager.get_names()]
