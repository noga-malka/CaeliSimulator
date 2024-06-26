import dash
from dash import html

from components.profile_components.add_profile_form import add_profile_form
from components.profile_components.create_new_profile_button import create_new_profile_button
from components.profile_components.profile_grid import profiles_grid
from pages.consts import PageRoutes, PageTitles

dash.register_page(__name__, path=PageRoutes.PROFILE_MANAGER, title=PageTitles.PROFILE_MANAGER)

layout = html.Div([
    profiles_grid, create_new_profile_button, add_profile_form
], className='flex-column', style={'align-items': 'center', 'margin-top': '10px'})
