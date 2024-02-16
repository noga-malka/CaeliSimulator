import dash_bootstrap_components
from dash import html, dcc

from components.data_display_components.consts import Size, CardIdType, Display


def generate_id(card_id: str, component_type: str):
    return {'index': card_id, 'type': component_type}


def generate_configurable_card(card_id: str):
    """
    generate a card with empty content and multiple inputs to control the result content

    :param card_id: unique card id to identify all sub components
    :return: Card component with default values
    """
    return dash_bootstrap_components.Card([
        dash_bootstrap_components.CardHeader(html.H4('display title', contentEditable="true")),
        dash_bootstrap_components.CardBody([
            html.Div([
                dcc.Dropdown(Size.ALL, Size.FULL, id=generate_id(card_id, CardIdType.SIZE),
                             clearable=False, searchable=False, style={'width': '72px'}),
                dcc.Dropdown(Display.ALL, Display.GRAPH, id=generate_id(card_id, CardIdType.DISPLAY),
                             clearable=False, searchable=False, style={'width': '77px'}),

                dcc.Input(placeholder=CardIdType.INPUTS, id=generate_id(card_id, CardIdType.INPUTS),
                          className='input', style={'width': '120px'}),
                dcc.Input(placeholder=CardIdType.TYPING, id=generate_id(card_id, CardIdType.TYPING),
                          className='input', style={'width': '72px'}),
            ], className='align'),
            html.Div(id=generate_id(card_id, CardIdType.CONTENT))
        ]),
    ], id=generate_id(card_id, CardIdType.CARD), style={'flex': '0 0 100%'})
