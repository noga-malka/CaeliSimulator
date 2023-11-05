import dash_bootstrap_components
import pandas
import plotly.express as px
from dash import dcc

from components.general_components.grid import create_grid_card
from components.simulator_components.consts import LiveData


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


def generate_graph_row(cards: list):
    return dash_bootstrap_components.Row([
        dash_bootstrap_components.Col(card) for card in cards
    ])


def build_graph_cards(data: pandas.DataFrame):
    cards_layout = []
    cards_row = []
    for column_name in data.columns:
        if column_name not in LiveData.NUMERIC_VALUE_FIELDS:
            cards_row.append(create_grid_card(column_name, [build_graph(data[column_name], column_name)]))
            if len(cards_row) == LiveData.GRAPH_NUMBER_IN_ROW:
                cards_layout.append(generate_graph_row(cards_row))
                cards_row = []
    if len(cards_row):
        cards_layout.append(generate_graph_row(cards_row))
    return cards_layout
