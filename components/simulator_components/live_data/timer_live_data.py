import pandas
from dash import html

from components.simulator_components.live_data.base_live_data import BaseLiveData


class TimerLiveData(BaseLiveData):
    @staticmethod
    def _convert_to_timer(seconds: int):
        return '{:0>2}:{:0>2}'.format(int((seconds / 60) % 60), seconds % 60)

    def create_component(self, title: str, value: pandas.Series):
        return html.Div(self._convert_to_timer(value.iloc[-1]), className='flex-center',
                        style={'font-size': '30px', 'font-weight': 'bold'})
