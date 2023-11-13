from dash import html, dcc, callback, Output, Input

from components.simulator_components.consts import LiveData
from components.simulator_components.live_data.utilities import build_simulator_display_grid
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

live_data = html.Div([
    html.Div(id=LiveData.LIVE_DATA_GRID),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.LIVE_DATA_GRID, 'children'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    if data.empty:
        return [], []
    return build_simulator_display_grid(data)
