from abc import ABC, abstractmethod

import dash_bootstrap_components
import pandas

from components.general_components.grid import create_grid_card


class BaseLiveData(ABC):
    @abstractmethod
    def create_component(self, title: str, value: pandas.Series):
        ...

    def create_column(self, title: str, value: pandas.Series):
        return dash_bootstrap_components.Col(create_grid_card(title, self.create_component(title, value)))
