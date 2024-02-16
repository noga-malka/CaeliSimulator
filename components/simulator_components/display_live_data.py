import dash
import pandas
from dash import html, dcc, callback, Output, Input, State, ALL, MATCH

from components.consts import Placeholder
from components.data_display_components.configurable_card import generate_configurable_card
from components.data_display_components.consts import CardIdType, DisplayDataContainer
from components.data_display_components.display_content import DISPLAY_TYPES
from components.data_display_components.drag_container import generate_draggable_children_div
from components.simulator_components.consts import LiveData
from database.database_manager import DatabaseManager
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

live_data = html.Div([
    generate_draggable_children_div(DisplayDataContainer.ID, []),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(DisplayDataContainer.ID, 'children'),
          Input(Placeholder.ID, Placeholder.Fields.CHILDREN))
def update_select_profile_dropdown_options(setup):
    return [generate_configurable_card(**card.__dict__) for card in DatabaseManager().display_manager.get_instances()]


@callback(Output({'index': ALL, 'type': CardIdType.CONTENT}, 'children'),
          State({'index': ALL, 'type': CardIdType.DISPLAY}, 'value'),
          State({'index': ALL, 'type': CardIdType.INPUTS}, 'value'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(cards_display, cards_input, interval):
    layout = []
    crueso_data = SimulatorDataManager().get_data(PacketHeaders.CRUESO)
    simulator_data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    data = pandas.concat([crueso_data, simulator_data], axis=1)
    for index in range(len(cards_input)):
        card_content = []
        if cards_input[index]:
            try:
                card_content = DISPLAY_TYPES[cards_display[index]](cards_input[index], data[cards_input[index]])
            except KeyError:
                pass
        layout.append(card_content)
    return layout


@callback(Output({'index': ALL, 'type': CardIdType.INPUTS}, 'options'),
          State({'index': ALL, 'type': CardIdType.INPUTS}, 'options'),
          Input(LiveData.INTERVAL, 'n_intervals'))
def update_input_dropdown(options: list, interval: int):
    crueso_data = SimulatorDataManager().get_data(PacketHeaders.CRUESO)
    simulator_data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    data = pandas.concat([crueso_data, simulator_data], axis=1)
    if len(options) == 0 or options[0] != list(data.columns):
        return [data.columns] * len(options)
    return dash.no_update


@callback(Output({'index': MATCH, 'type': CardIdType.CARD}, 'style'),
          Input({'index': MATCH, 'type': CardIdType.SIZE}, 'value'),
          prevent_initial_call=True)
def update_card_size(target_size: str):
    return {'flex': f'0 0 {target_size}'}
