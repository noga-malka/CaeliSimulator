import dash
from dash import html

from components.navigation_bar import navigation_bar
from components.title import title
from pages.consts import PageRoutes

dash.register_page(
    __name__,
    path=PageRoutes.CONNECT,
    title='Connection'
)

layout = html.Div([
    title,
    html.Div([navigation_bar, html.Div('content')],
             className='flex', style={'height': '100vh'})])
