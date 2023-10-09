import dash_bootstrap_components
from dash import html


def create_card(title: str, content: list):
    return html.Div([
        html.Label(title),
        html.Hr(),
        html.Div(content, className='flex center')
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content'})


def generate_number_input(input_id: str, minimum: int, maximum: int):
    return dash_bootstrap_components.Input(id=input_id,
                                           min=minimum,
                                           max=maximum,
                                           type='number',
                                           style={'width': '100%'},
                                           value=minimum)


def build_number_input_card(card_title: str, input_id: str, minimum: int, maximum: int):
    return create_card(card_title, [
        dash_bootstrap_components.Input(id=input_id,
                                        min=minimum,
                                        max=maximum,
                                        type='number',
                                        style={'width': '100%'},
                                        value=minimum)
    ])


def build_string_input_card(card_title: str, input_id: str):
    return create_card(card_title, [
        dash_bootstrap_components.Input(id=input_id, style={'width': '100%'})
    ])
