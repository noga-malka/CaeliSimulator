import dash_bootstrap_components
from dash import html, dcc, callback, Output, Input

from components.simulator_components.consts import LiveData
from components.simulator_components.live_data.graph_cards import build_graph_cards
from components.simulator_components.live_data.text_cards import build_text_cards
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

live_data = html.Div([
    dash_bootstrap_components.Row(id=LiveData.TEXT_FIELDS),
    html.Div(id=LiveData.GRAPH_FIELDS),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.TEXT_FIELDS, 'children'),
          Output(LiveData.GRAPH_FIELDS, 'children'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    if data.empty:
        return [], []
    return build_text_cards(data), build_graph_cards(data)
