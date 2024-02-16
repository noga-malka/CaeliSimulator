import pandas
from dash import html, dcc, callback, Output, Input, State, ALL

from components.data_display_components.configurable_card import generate_configurable_card
from components.data_display_components.consts import CardIdType
from components.data_display_components.display_content import DISPLAY_TYPES
from components.data_display_components.drag_container import generate_draggable_children_div
from components.simulator_components.consts import LiveData
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

live_data = html.Div([
    generate_draggable_children_div("drag_container", [
        generate_configurable_card("1"),
    ]),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


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
        title = cards_input[index] or ''
        input_columns = list(set(filter(lambda column: column in data.columns, title.split(','))))
        card_content = []
        if input_columns:
            card_content = DISPLAY_TYPES[cards_display[index]](title, data[input_columns])
        layout.append(card_content)
    return layout
