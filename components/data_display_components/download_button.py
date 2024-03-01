import time

import dash
from dash import callback, Output, Input, html, dcc

from components.general_components.add_button import create_bottom_grid_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

download_data_button = html.Div([
    dcc.Download('download_file'),
    create_bottom_grid_button('download', 'subway:download-3'),
])


@callback(
    Output('download_file', 'data'),
    Input('download', 'n_clicks'),
    prevent_initial_call=True)
def download_data(buttons_clicked):
    data = SimulatorDataManager().get_live_dataframe()
    if not data.empty:
        return dict(filename=f'{time.strftime("%Y-%m-%d_%H-%M-%S")}.csv', content=data.to_csv())
    return dash.no_update
