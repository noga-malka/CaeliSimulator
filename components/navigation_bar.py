import dash_bootstrap_components
from dash import html
from dash_iconify import DashIconify

from assets import icons
from pages.consts import PageRoutes, PageTitles


def create_navigation_link(icon_name: str, title: str, navigation_link: str):
    icon = DashIconify(icon=icon_name, width=45, style={'margin-right': '8px'})
    link_content = html.Div([icon, html.Div(title)], style={'display': 'inline-flex'})
    return dash_bootstrap_components.NavLink(link_content, href=navigation_link)


navigation_bar = dash_bootstrap_components.Nav([
    create_navigation_link(icons.BLUETOOTH, PageTitles.BLUETOOTH, PageRoutes.BLUETOOTH),
    create_navigation_link(icons.SERIAL, PageTitles.SERIAL, PageRoutes.SERIAL),
    create_navigation_link(icons.MANAGE_PROFILES, PageTitles.MANAGE_PROFILES, PageRoutes.MANAGE_PROFILES),
    create_navigation_link(icons.MANAGE_TEST_CASES, PageTitles.MANAGE_TEST_CASES, PageRoutes.MANAGE_TEST_CASES),
    create_navigation_link(icons.RUN_SIMULATOR, PageTitles.RUN_SIMULATOR, PageRoutes.RUN_SIMULATOR),
], vertical=True, pills=True, className='sidebar')
