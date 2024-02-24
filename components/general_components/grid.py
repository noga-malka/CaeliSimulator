import dash_bootstrap_components
from dash import html

from assets.icons import ControlButtonIcons
from components.data_display_components.consts import CardIdType


def create_grid_card(title: str, content: list, should_center: bool = False) -> dash_bootstrap_components.Card:
    """
    create card inside a grid component

    :param title: title to display at top
    :param content: the cards content
    :param should_center: boolean value. if True center the content, else leave it spaced out
    :return: card component
    """
    content_style = 'align' if should_center else ''
    return dash_bootstrap_components.Card([
        dash_bootstrap_components.CardHeader(
            [html.H3(title, style={'margin': 0}),
             html.Div(ControlButtonIcons.CLOSE, id={'index': title, 'type': CardIdType.DELETE})],
            className='align', style={'justifyContent': 'space-between'}),
        dash_bootstrap_components.CardBody(content, className=f'flex-column {content_style}'),
    ], id=title)


def create_grid(grid_id: str) -> html.Div:
    """
    :param grid_id: unique id
    :return: div with grid styling and given id
    """
    return html.Div([], className='grid', id=grid_id)
