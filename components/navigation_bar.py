import dash_bootstrap_components
from dash import html
from dash_iconify import DashIconify

from assets import icons
from pages.consts import PageRoutes


def create_navigation_link(icon_name: str, title: str, navigation_link: str):
    icon = DashIconify(icon=icon_name, width=40, style={'margin-right': '8px'})
    link_content = html.Div([icon, html.Div(title)], style={'display': 'inline-flex'})
    return dash_bootstrap_components.NavLink(link_content, href=navigation_link)


navigation_bar = dash_bootstrap_components.Nav([
    create_navigation_link(icons.BLUETOOTH, 'Connect to Bluetooth', PageRoutes.BLUETOOTH),
    create_navigation_link(icons.SERIAL, 'Connect to Serial', PageRoutes.SERIAL),
    create_navigation_link(icons.ADD_PROFILE, 'Add Profile', PageRoutes.ADD_PROFILE),
    create_navigation_link(icons.SYNC_PROFILES, 'Sync Profiles to Simulator', PageRoutes.SYNC_PROFILES),
], vertical=True, pills=True, className='sidebar')
