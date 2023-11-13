import pandas
from dash import dcc
from plotly import express

from components.simulator_components.live_data.base_live_data import BaseLiveData


class GraphLiveData(BaseLiveData):
    def create_component(self, title: str, value: pandas.Series):
        figure = express.line(value, y=title)
        figure.update_layout(showlegend=False)
        return dcc.Graph(figure=figure,
                         style={'height': '300px'},
                         config={
                             'displayModeBar': False,
                             'showAxisRangeEntryBoxes': False,
                             'showTips': False,
                         })
