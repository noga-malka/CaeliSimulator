import dash_bootstrap_components
import pandas
from dash import html

from components.general_components.grid import create_grid_card
from components.simulator_components.consts import LiveData


def build_text(value: int):
    return [html.Div(value, className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})]


def build_text_cards(data: pandas.DataFrame):
    cards = []
    for column_name in data.columns:
        if column_name in LiveData.NUMERIC_VALUE_FIELDS:
            column_card = create_grid_card(column_name, build_text(data[column_name].iloc[-1]))
            cards.append(dash_bootstrap_components.Col(column_card))
    return cards
