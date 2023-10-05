import dash_bootstrap_components
from dash import html
from assets import icons

navigation_bar = dash_bootstrap_components.Nav([
    dash_bootstrap_components.NavLink([icons.CONNECT, html.Div('Connect Device')], href=f'/connect'),
    dash_bootstrap_components.NavLink([icons.CONNECT, html.Div('Create Profile')], href=f'/profile'),
    dash_bootstrap_components.NavLink([icons.CONNECT, html.Div('Sync Profiles')], href=f'/sync'),
], vertical=True, pills=True, className='sidebar', style={'height': '100vh'})
