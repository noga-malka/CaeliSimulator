import dash_bootstrap_components
from dash import html


def create_card(title: str, content: list):
    return html.Div([
        html.Label(title),
        html.Hr(),
        html.Div(content, className='flex-center padding margin')
    ], style={'height': 'fit-content'})


def generate_number_input(input_id: str, minimum: int, maximum: int):
    return dash_bootstrap_components.Input(id=input_id,
                                           min=minimum,
                                           max=maximum,
                                           type='number',
                                           className='full-width',
                                           value=minimum)


def build_number_input_card(card_title: str, input_id: str, minimum: int, maximum: int):
    return create_card(card_title, [
        dash_bootstrap_components.Input(id=input_id,
                                        min=minimum,
                                        max=maximum,
                                        type='number',
                                        className='full-width',
                                        value=minimum)
    ])


def build_string_input_card(card_title: str, input_id: str):
    return create_card(card_title, [
        dash_bootstrap_components.Input(id=input_id, className='full-width')
    ])
