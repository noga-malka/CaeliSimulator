import pandas
import plotly.express as px
from dash import html, dcc, callback, Output, Input

from components.general_components.grid import create_grid_card
from components.simulator_components.consts import LiveData
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager


def build_graph(data: pandas.Series, column_name: str):
    figure = px.line(data, y=column_name)
    figure.update_layout(showlegend=False)
    return dcc.Graph(figure=figure,
                     style={'height': '300px'},
                     config={
                         'displayModeBar': False,
                         'showAxisRangeEntryBoxes': False,
                         'showTips': False,
                     })


def build_graph_cards(data: pandas.DataFrame):
    cards = []
    for column_name in data.columns:
        if column_name not in LiveData.NUMERIC_VALUE_FIELDS:
            cards.append(create_grid_card(column_name, [build_graph(data[column_name], column_name)]))
    return cards


def build_text(value: int):
    return [html.Div(value, className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})]


def build_text_cards(data: pandas.DataFrame):
    cards = []
    for column_name in LiveData.NUMERIC_VALUE_FIELDS:
        if column_name in data.columns:
            cards.append(create_grid_card(column_name, build_text(data[column_name].iloc[-1])))
    return cards


live_data = html.Div([
    html.Div(id=LiveData.ID, className='graph-grid flex-center'),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.ID, 'children'), Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    if data.empty:
        return []
    return build_text_cards(data) + build_graph_cards(data)
