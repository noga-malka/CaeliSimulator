import pandas
from dash import html, dcc, callback, Output, Input

from components.simulator_components.consts import LiveData
from components.simulator_components.live_data.consts import DisplayOptions
from components.simulator_components.live_data.utilities import build_live_data_display_grid
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

live_data = html.Div([
    html.Div(id=LiveData.LIVE_DATA_GRID),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.LIVE_DATA_GRID, 'children'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    layout = []
    crueso_data = SimulatorDataManager().get_data(PacketHeaders.CRUESO)
    simulator_data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    data = pandas.concat([crueso_data, simulator_data], axis=1)
    if not data.empty:
        layout += build_live_data_display_grid(data, DisplayOptions.DISPLAY_TYPE_RESOLVER)
    return layout
