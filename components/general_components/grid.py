from dash import html


def create_grid_card(title: str, content: list, should_center: bool = False) -> html.Div:
    """
    create card inside a grid component

    :param title: title to display at top
    :param content: the cards content
    :param should_center: boolean value. if True center the content, else leave it spaced out
    :return: card component
    """
    content_style = 'align' if should_center else ''
    return html.Div([
        html.Label(title, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        html.Div(content, className=f'flex-column {content_style}'),
    ], className='grid-card')


def create_grid(grid_id: str) -> html.Div:
    """
    :param grid_id: unique id
    :return: div with grid styling and given id
    """
    return html.Div([], className='grid', id=grid_id)
