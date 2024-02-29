import dash
from dash import html, dcc, callback, Output, Input, State, MATCH

from components.consts import Placeholder
from components.data_display_components.configurable_card import generate_configurable_card
from components.data_display_components.consts import CardIdType, DisplayDataContainer
from components.data_display_components.display_content import DISPLAY_TYPES
from components.simulator_components.consts import LiveData
from database.database_manager import DatabaseManager
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

live_data = html.Div([
    html.Div([], DisplayDataContainer.ID, className='flex-wrap'),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(DisplayDataContainer.ID, 'children'),
          Input(Placeholder.ID, Placeholder.Fields.CHILDREN))
def update_select_profile_dropdown_options(setup):
    return [generate_configurable_card(**card.__dict__) for card in DatabaseManager().display_manager.get_instances()]


@callback(Output({'index': MATCH, 'type': CardIdType.CONTENT}, 'children'),
          State({'index': MATCH, 'type': CardIdType.DISPLAY}, 'value'),
          State({'index': MATCH, 'type': CardIdType.INPUTS}, 'value'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(cards_display, cards_inputs, interval):
    if cards_inputs:
        data = SimulatorDataManager().get_live_dataframe()
        try:
            return DISPLAY_TYPES[cards_display](cards_inputs, data[cards_inputs])
        except KeyError:
            pass
    return dash.no_update


@callback(Output({'index': MATCH, 'type': CardIdType.INPUTS}, 'options'),
          State({'index': MATCH, 'type': CardIdType.INPUTS}, 'value'),
          Input({'index': MATCH, 'type': CardIdType.UPDATE_INPUTS}, 'n_clicks'))
def update_input_dropdown(card_inputs: list, click: int):
    data = SimulatorDataManager().get_live_dataframe()
    options = set.union(set(card_inputs), data.columns)
    return [dict(label=option, value=option, disabled=option not in data.columns) for option in options]


@callback(Output({'index': MATCH, 'type': CardIdType.CARD}, 'style'),
          Input({'index': MATCH, 'type': CardIdType.SIZE}, 'value'),
          prevent_initial_call=True)
def update_card_size(target_size: str):
    return {'flex': f'0 0 {target_size}'}
