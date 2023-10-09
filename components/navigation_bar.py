import dash_bootstrap_components
from dash import html
from dash_iconify import DashIconify

from assets.icons import BigIcons
from pages.consts import PageRoutes, PageTitles


def create_navigation_link(icon: DashIconify, title: str, navigation_link: str):
    link_content = html.Div([icon, html.Div(title)], style={'display': 'inline-flex'})
    return dash_bootstrap_components.NavLink(link_content, href=navigation_link)


navigation_bar = dash_bootstrap_components.Nav([
    create_navigation_link(BigIcons.BLUETOOTH, PageTitles.BLUETOOTH, PageRoutes.BLUETOOTH),
    create_navigation_link(BigIcons.SERIAL, PageTitles.SERIAL, PageRoutes.SERIAL),
    create_navigation_link(BigIcons.MANAGE_PROFILES, PageTitles.MANAGE_PROFILES, PageRoutes.MANAGE_PROFILES),
    create_navigation_link(BigIcons.MANAGE_TEST_CASES, PageTitles.MANAGE_TEST_CASES, PageRoutes.MANAGE_TEST_CASES),
    create_navigation_link(BigIcons.RUN_SIMULATOR, PageTitles.RUN_SIMULATOR, PageRoutes.RUN_SIMULATOR),
], vertical=True, pills=True, className='sidebar')
