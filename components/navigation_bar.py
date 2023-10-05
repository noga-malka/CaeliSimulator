import dash_bootstrap_components
from dash import html
from assets import icons
from pages.consts import PageRoutes

navigation_bar = dash_bootstrap_components.Nav([
    dash_bootstrap_components.NavLink([icons.CONNECT, html.Div('Connect Device')], href=PageRoutes.CONNECT),
    dash_bootstrap_components.NavLink([icons.CONNECT, html.Div('Create Profile')], href=PageRoutes.ADD_PROFILE),
    dash_bootstrap_components.NavLink([icons.CONNECT, html.Div('Sync Profiles')], href=PageRoutes.SYNC_PROFILES),
], vertical=True, pills=True, className='sidebar')
