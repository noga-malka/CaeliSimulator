import plotly.express as px
from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate

from components.simulator_components.consts import LiveData
from simulator_data_manager.packet_type import PacketType


def create_live_data_card(title, content):
    return html.Div([
        html.Label(title, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        content,
    ], className='grid-card')


def build_graph(figure):
    return dcc.Graph(figure=figure,
                     style={'height': '300px'},
                     config={
                         'displayModeBar': False,
                         'showAxisRangeEntryBoxes': False,
                         'showTips': False,
                     })


live_data = html.Div([
    html.Div(id=LiveData.ID, className='graph-grid flex-center'),
    dcc.Interval(id=LiveData.INTERVAL, interval=1000)
])


@callback(Output(LiveData.ID, 'children'), Input(LiveData.INTERVAL, 'n_intervals'))
def update_live_data(interval):
    data = PacketType.Data.value.saved_data
    if data.empty:
        raise PreventUpdate
    live_cards = []
    for column_name in data.columns:
        figure = px.line(data[column_name], y=column_name)
        figure.update_layout(showlegend=False)
        live_cards.append(create_live_data_card(column_name, build_graph(figure)))
    return live_cards
