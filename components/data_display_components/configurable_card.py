import dash_bootstrap_components
from dash import html, dcc


def generate_id(card_id: str, component_type: str):
    return {'index': card_id, 'type': component_type}


def generate_configurable_card(card_id: str):
    return dash_bootstrap_components.Card([
        dash_bootstrap_components.CardHeader(html.H4('display title', contentEditable="true")),
        dash_bootstrap_components.CardBody([
            html.Div([
                dcc.Dropdown(['100%', '50%', '30%', '25%'], '100%', id=generate_id(card_id, 'size'),
                             clearable=False, searchable=False, style={'width': '72px'}),
                dcc.Dropdown(['Graph', 'Text', 'Timer'], 'Graph', id=generate_id(card_id, 'display'),
                             clearable=False, searchable=False, style={'width': '77px'}),
                html.Label('Inputs', contentEditable="true", id=generate_id(card_id, 'input'),
                           style={'border': '1px solid #ccc', 'border-radius': '4px', 'padding': '5px'}),
                html.Label('Typing', contentEditable="true", id=generate_id(card_id, 'typing'),
                           style={'border': '1px solid #ccc', 'border-radius': '4px', 'padding': '5px'}),
            ], className='align'),
            html.Div(id=generate_id(card_id, 'content'))
        ]),
    ], id=generate_id(card_id, 'card'), style={'flex': '0 0 100%'})
