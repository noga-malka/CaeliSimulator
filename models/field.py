from typing import Any

import dash_bootstrap_components
from dash import html

from components.input_card import build_number_input_card
from models.unit_type_parsers.base_parser import BaseParser


class ProfileField:
    def __init__(self,
                 name: str,
                 unit_parser: BaseParser,
                 display_name: str,
                 icons: list,
                 minimum: float,
                 maximum: float):
        self.name = name
        self.unit_parser = unit_parser
        self.display_name = display_name
        self.icons = icons
        self.minimum = minimum
        self.maximum = maximum

    def generate_description(self):
        return f'{self.display_name} [{self.unit_parser.unit_type}]'

    def convert_to_bytes(self, value: Any) -> bytes:
        return self.unit_parser.convert_to_bytes(value)

    def generate_input_component(self):
        return build_number_input_card(self.generate_description(), self.name, self.minimum, self.maximum)

    def generate_detailed_component(self, profile_name: str, value: Any):
        description = self.generate_description()
        return html.Div([
            dash_bootstrap_components.Tooltip(description, target=profile_name + description,
                                              placement='top'),
            html.Div(self.icons, style={'margin-right': '5px'}, className='flex', id=profile_name + description),
            html.Div([
                value,
                html.Sub(self.unit_parser.unit_type)
            ]),
        ], className='flex', style={'align-items': 'center', 'justify-content': 'space-between'})
