from typing import Any

import dash_bootstrap_components
from dash import html

from components.input_card import build_number_input_card


class ProfileField:
    def __init__(self, name: str, unit_type: str, display_name: str, icons: list, minimum: int = 0,
                 maximum: int = 10000):
        self.name = name
        self.unit_type = unit_type
        self.display_name = display_name
        self.icons = icons
        self.minimum = minimum
        self.maximum = maximum

    def generate_description(self):
        return f'{self.display_name} [{self.unit_type}]'

    @staticmethod
    def convert_to_bytes(value) -> bytes:
        return int(value).to_bytes(2, 'big')

    def generate_input_component(self):
        return build_number_input_card(self.generate_description(), self.name, self.minimum, self.maximum)

    def generate_detailed_component(self, profile_name: str, value: Any):
        description = self.generate_description()
        return html.Div([
            dash_bootstrap_components.Tooltip(description, target=profile_name + description,
                                              placement='top'),
            html.Div(self.icons, style={'margin-right': '5px'}, className='flex', id=profile_name + description),
            value
        ], className='flex', style={'align-items': 'center', 'justify-content': 'space-between'})
