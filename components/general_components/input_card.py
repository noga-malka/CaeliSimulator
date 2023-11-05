import dash_bootstrap_components
from dash import html


def create_card(title: str, content: list) -> html.Div:
    return html.Div([
        html.Label(title),
        html.Hr(),
        html.Div(content, className='flex-center padding margin')
    ], style={'height': 'fit-content'})


def build_number_input_card(card_title: str, input_id: str, minimum: float, maximum: float) -> html.Div:
    """
    create an input card that accept numbers

    :param card_title: title to display at top
    :param input_id: the input component id
    :param minimum: minimum value allowed to enter
    :param maximum: maximum value allowed to enter
    :return: card div component
    """
    return create_card(card_title, [
        dash_bootstrap_components.Input(id=input_id,
                                        min=minimum,
                                        max=maximum,
                                        type='number',
                                        className='full-width',
                                        value=minimum,
                                        required=True)
    ])


def build_string_input_card(card_title: str, input_id: str) -> html.Div:
    """
    create an input card that accept strings

    :param card_title: title to display at top
    :param input_id: the input component id
    :return: card div component
    """
    return create_card(card_title, [
        dash_bootstrap_components.Input(id=input_id,
                                        className='full-width',
                                        required=True)
    ])
