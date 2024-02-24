import time

from dash import callback, Output, Input

from components.consts import Placeholder
from components.general_components.add_button import create_bottom_grid_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

download_data_button = create_bottom_grid_button('download', 'subway:download-3')


@callback(
    Output(Placeholder.ID, Placeholder.Fields.ROLE),
    Input('download', 'n_clicks'),
    prevent_initial_call=True)
def download_data(buttons_clicked):
    data = SimulatorDataManager().get_live_dataframe()
    if not data.empty:
        data.to_csv(f'output\\{time.strftime("%Y-%m-%d_%H-%M-%S")}.csv')
