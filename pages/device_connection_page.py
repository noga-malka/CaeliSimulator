import dash
from dash import html

from components.create_new_profile_button import create_new_profile_button
from components.add_profile_form import add_profile_form
from components.navigation_bar import navigation_bar
from components.title import title
from pages.consts import PageRoutes

dash.register_page(
    __name__,
    path=PageRoutes.ADD_PROFILE,
    title='Add Profile'
)

layout = html.Div([
    title,
    html.Div([navigation_bar, create_new_profile_button, add_profile_form],
             className='flex', style={'height': '100vh'})])
