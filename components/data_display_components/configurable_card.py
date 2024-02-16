import dash_bootstrap_components
from dash import html, dcc, callback, Output, Input, ALL

from assets.icons import ControlButtonIcons
from components.consts import Placeholder
from components.data_display_components.consts import Size, CardIdType, Display, Inputs
from database.database_manager import DatabaseManager
from models.display import DisplayCard


def generate_id(card_id: str, component_type: str):
    return {'index': card_id, 'type': component_type}


def generate_configurable_card(card_id: str,
                               title: str = None,
                               size: str = Size.FULL,
                               display_type: str = Display.GRAPH,
                               inputs: list[str] = None,
                               typing: str = None):
    """
    generate a card with empty content and multiple inputs to control the result content

    :param card_id: unique card id to identify all sub components
    :param title: title to display
    :param size: percentage of the card
    :param display_type: type of visualization
    :param inputs: column names to extract data from
    :param typing: type of input
    :return: Card component with default values
    """
    return dash_bootstrap_components.Card([
        dash_bootstrap_components.CardHeader([
            dcc.Input(placeholder='Card Title', value=title, id=generate_id(card_id, CardIdType.TITLE),
                      style={'width': '200px', 'border': 'none', 'font-size': 'xx-large',
                             'background-color': 'inherit'}),
            html.Div(ControlButtonIcons.CLOSE, id=generate_id(card_id, CardIdType.DELETE)),
        ], className='flex', style={'justifyContent': 'space-between'}),
        html.Div([
            dcc.Dropdown(Size.ALL, size, id=generate_id(card_id, CardIdType.SIZE),
                         clearable=False, searchable=False, style={'width': '72px'}),
            dcc.Dropdown(Display.ALL, display_type, id=generate_id(card_id, CardIdType.DISPLAY),
                         clearable=False, searchable=False, style={'width': '77px'}),
            dcc.Dropdown([{'label': option, 'value': option, 'disabled': True} for option in Inputs.STATIC_OPTIONS],
                         id=generate_id(card_id, CardIdType.INPUTS), value=inputs,
                         multi=True, clearable=False, searchable=False, style={'width': '150px'}),

            dcc.Input(placeholder=CardIdType.TYPING, value=typing, id=generate_id(card_id, CardIdType.TYPING),
                      className='input', style={'width': '72px'}),
        ], className='align flex-wrap'),
        dash_bootstrap_components.CardBody([], id=generate_id(card_id, CardIdType.CONTENT)),
    ], id=generate_id(card_id, CardIdType.CARD), style={'flex': f'0 0 {size}'})


@callback(
    Output(Placeholder.ID, Placeholder.Fields.LOADING_STATE),
    Input({'index': ALL, 'type': CardIdType.CARD}, 'id'),
    Input({'index': ALL, 'type': CardIdType.TITLE}, 'value'),
    Input({'index': ALL, 'type': CardIdType.SIZE}, 'value'),
    Input({'index': ALL, 'type': CardIdType.DISPLAY}, 'value'),
    Input({'index': ALL, 'type': CardIdType.INPUTS}, 'value'),
    Input({'index': ALL, 'type': CardIdType.TYPING}, 'value'),
    prevent_initial_call=True
)
def update_database(all_cards: list, *configurations: list[list]):
    cards = zip([card['index'] for card in all_cards], *configurations)
    for card in cards:
        DatabaseManager().display_manager.add(DisplayCard(*card))
