from dash import callback, Output, Input

from components.consts import Placeholder
from components.general_components.add_button import create_bottom_grid_button
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

reset_data_button = create_bottom_grid_button('reset_data', 'ic:round-delete')


@callback(
    Output(Placeholder.ID, Placeholder.Fields.CONTENT_EDITABLE),
    Input('reset_data', 'n_clicks'),
    prevent_initial_call=True)
def reset_data(buttons_clicked):
    SimulatorDataManager().crueso_thread.clear_saved_data()
    SimulatorDataManager().simulator_thread.clear_saved_data()
