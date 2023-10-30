import dash_bootstrap_components
from dash import html, Input, Output, callback

from components.simulator_components.consts import LiveData, ProgressBar
from models.profile import Profile
from utilities import validate_arguments


def create_profile_node(profile: Profile):
    return html.Div([
        dash_bootstrap_components.Progress(id=ProgressBar.ID, color='success',
                                           className='progress-container progress-timer'),
        html.Div([
        ], id=ProgressBar.STEPS, className='flex-center align progress-container',
            style={'justify-content': 'space-between', 'height': '100px'})],
        className='flex-center align')


test_case_progress_bar = create_profile_node('')


@callback(Output(ProgressBar.ID, 'value'),
          Output(ProgressBar.STEPS, 'children'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_progress_bar(interval: int):
    validate_arguments(interval)
    steps = [
        html.Div('test', className='flex-center align circle active'),
        html.Div('test', className='flex-center align circle current'),
        html.Div('test', className='flex-center align circle'),
    ]
    return ProgressBar.STEP_PERCENTAGE_WIDTH + interval / 2, steps
