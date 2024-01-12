from abc import ABC, abstractmethod

import pandas
from dash import html

from components.general_components.grid import create_grid_card


class BaseLiveData(ABC):
    @abstractmethod
    def create_component(self, title: str, value: pandas.Series):
        ...

    def create_column(self, title: str, value: pandas.Series):
        return html.Div(create_grid_card(title, self.create_component(title, value)), style={'flex': '1 1 0px'})
