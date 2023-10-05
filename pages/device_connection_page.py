import dash
from dash import html

from components.add_profile_form import add_profile_form
from components.input_card import build_input_card_component
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
    html.Div([navigation_bar, add_profile_form],
             className='flex', style={'height': '100vh'})])
