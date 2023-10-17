import dash
from dash import html

from components.navigation_bar import navigation_bar
from components.title import title

dash.register_page(
    __name__,
    path='/',
    title='Home'
)

layout = html.Div([
    title,
    navigation_bar], className='full_height')
