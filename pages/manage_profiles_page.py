import dash
from dash import html

from components.create_new_profile_button import create_new_profile_button
from components.add_profile_form import add_profile_form
from components.navigation_bar import navigation_bar
from components.placeholder import placeholder
from components.profile_grid import profiles_grid
from components.title import title
from pages.consts import PageRoutes, PageTitles

dash.register_page(
    __name__,
    path=PageRoutes.MANAGE_PROFILES,
    title=PageTitles.MANAGE_PROFILES
)

layout = html.Div([
    title,
    placeholder,
    html.Div([navigation_bar,
              html.Div([profiles_grid, create_new_profile_button], className='flex',
                       style={'flex-direction': 'column', 'align-items': 'center', 'width': '100%',
                              'margin-top': '10px'}),
              add_profile_form],
             className='flex', style={'height': '100vh'})])
