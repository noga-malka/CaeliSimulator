from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate

from components.simulator_components.consts import LiveData
from simulator_data_manager.packet_type import PacketType


def create_live_data_card(title, value):
    return html.Div([
        html.Label(title, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        html.Div(value, style={'font-size': 'larger'})
    ], className='grid-card')


live_data = html.Div([
    html.Div(id=LiveData.ID, className='grid flex-center'),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.ID, 'children'), Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    data = PacketType.Data.value.saved_data
    if not data:
        raise PreventUpdate
    return [create_live_data_card(title, content) for title, content in data.items()]
