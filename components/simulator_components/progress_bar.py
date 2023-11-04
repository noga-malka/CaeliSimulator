import dash_bootstrap_components
from dash import html, Input, Output, callback

from components.simulator_components.consts import LiveData, ProgressBar
from utilities import validate_arguments

test_case_progress_bar = html.Div(
    [
        dash_bootstrap_components.Progress(id=ProgressBar.ID, color='success',
                                           className='progress-container progress-timer'),
        html.Div([], id=ProgressBar.STEPS, className='flex-center align progress-container',
                 style={'justify-content': 'space-between', 'height': '100px'})],
    className='flex-center align')


def build_test_case_progress(profiles: list):
    print(profiles)
    profile_steps = []
    for profile_name, _ in profiles:
        profile_steps.append(html.Div(profile_name, className='flex-center align circle'))
    return profile_steps + [html.Div()]


@callback(Output(ProgressBar.STEPS, 'children'),
          Input(ProgressBar.CURRENT_TEST_CASE, 'data'))
def update_progress_bar(profiles: list):
    validate_arguments(profiles)
    return build_test_case_progress(profiles)


@callback(Output(ProgressBar.ID, 'value'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_progress_bar(interval: int):
    validate_arguments(interval)
    return ProgressBar.STEP_PERCENTAGE_WIDTH + interval / 2
