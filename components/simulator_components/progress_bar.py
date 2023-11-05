import dash_bootstrap_components
from dash import html, Input, Output, callback, State

from components.simulator_components.consts import LiveData, ProgressBar
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.packet_type_parsers.consts import SimulatorKeys
from simulator_data_manager.simulator_data_manager import SimulatorDataManager
from utilities import validate_arguments

test_case_progress_bar = html.Div(
    [
        dash_bootstrap_components.Progress(id=ProgressBar.ID, color='success',
                                           className='progress-container progress-timer'),
        html.Div([], id=ProgressBar.STEPS, className='flex-center align progress-container',
                 style={'justify-content': 'space-between', 'height': '100px'})],
    className='flex-center align')


def build_test_case_progress(profiles: list):
    profile_steps = []
    for profile_name, _ in profiles:
        profile_steps.append(html.Div(profile_name, className='flex-center align circle'))
    return profile_steps + [html.Div()]


def calculate_progress(profiles: list) -> int:
    data = SimulatorDataManager().get_data(PacketHeaders.DATA).iloc[-1]
    current_profile = data[SimulatorKeys.CURRENT_PROFILE]
    if current_profile == len(profiles):
        return 100
    profile_total_time = profiles[current_profile][1]
    profile_run_time = min(data[SimulatorKeys.PROFILE_RUN_TIME], profile_total_time)
    profile_length = (100 - ProgressBar.STEP_PERCENTAGE_WIDTH * len(profiles)) / len(profiles)
    percentage = profile_run_time / profile_total_time * profile_length
    base_length = (profile_length + ProgressBar.STEP_PERCENTAGE_WIDTH) * current_profile
    return base_length + ProgressBar.STEP_PERCENTAGE_WIDTH + percentage


@callback(Output(ProgressBar.STEPS, 'children'),
          Input(ProgressBar.CURRENT_TEST_CASE, 'data'))
def update_progress_bar(profiles: list):
    validate_arguments(profiles)
    return build_test_case_progress(profiles)


@callback(Output(ProgressBar.ID, 'value'),
          State(ProgressBar.CURRENT_TEST_CASE, 'data'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_progress_bar(profiles: list, interval: int):
    validate_arguments(profiles)
    return calculate_progress(profiles)
