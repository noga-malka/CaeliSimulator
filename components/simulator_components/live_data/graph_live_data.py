import pandas
from dash import dcc
from plotly import express

from components.simulator_components.live_data.base_live_data import BaseLiveData
from simulator_data_manager.packet_type_parsers.consts import CruesoKeys

TYPING = {
    CruesoKeys.PRESSURE_1: 'mBar',
    CruesoKeys.PRESSURE_2: 'mBar',
    CruesoKeys.TACH_B_1: 'RPM',
    CruesoKeys.TACH_B_2: 'RPM',
}


class GraphLiveData(BaseLiveData):
    def create_component(self, title: str, value: pandas.Series):
        figure = express.line(value, y=title)
        yaxis_title = f'{title} [{TYPING[title]}]' if TYPING.get(title) else title
        figure.update_layout(showlegend=False, yaxis_title=yaxis_title)
        return dcc.Graph(figure=figure,
                         style={'height': '300px'},
                         config={
                             'displayModeBar': False,
                             'showAxisRangeEntryBoxes': False,
                             'showTips': False,
                         })
