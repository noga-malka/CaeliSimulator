import pandas
from dash import html

from components.simulator_components.live_data.base_live_data import BaseLiveData


class TextLiveData(BaseLiveData):
    def create_component(self, title: str, value: pandas.Series):
        return html.Div(value.iloc[-1], className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})
