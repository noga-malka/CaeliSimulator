import pandas
import plotly.express as px
from dash import html, dcc, callback, Output, Input

from components.simulator_components.consts import LiveData
from simulator_data_manager.consts import PacketHeaders
from simulator_data_manager.simulator_data_manager import SimulatorDataManager


def create_live_data_card(title, content):
    return html.Div([
        html.Label(title, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        content,
    ], className='grid-card')


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


def build_text(data: pandas.Series):
    return html.Div(data.iloc[-1], className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})


def build_content(data: pandas.Series, column_name: str):
    if column_name in LiveData.NUMERIC_VALUE_FIELDS:
        return build_text(data)
    return build_graph(data, column_name)


live_data = html.Div([
    html.Div(id=LiveData.ID, className='graph-grid flex-center'),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.ID, 'children'), Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    data = SimulatorDataManager().get_data(PacketHeaders.DATA)
    if data.empty:
        return []
    live_cards = []
    for column_name in data.columns:
        live_cards.append(create_live_data_card(column_name, build_content(data[column_name], column_name)))
    return live_cards
