import dash_bootstrap_components
from dash import html


def generate_number_input_component(input_id: str, minimum: int, maximum: int):
    return dash_bootstrap_components.Input(input_id,
                                           min=minimum,
                                           max=maximum,
                                           type='number',
                                           style={'width': '100%'},
                                           value=0)


def build_input_card_component(card_title: str, input_id: str, minimum: int, maximum: int):
    return html.Div([
        html.Label(card_title),
        html.Hr(),
        html.Div([
            generate_number_input_component(input_id, minimum, maximum),
        ], className='flex center')
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content'})
