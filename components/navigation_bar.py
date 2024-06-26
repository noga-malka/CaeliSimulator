import dash_bootstrap_components
from dash import html
from dash_iconify import DashIconify

from assets.icons import NavigationBarIcons
from pages.consts import PageRoutes, PageTitles


def create_navigation_link(icon: DashIconify, title: str, navigation_link: str) -> dash_bootstrap_components.NavLink:
    """
    create a single navigation link with an icon, title and route to navigate to.
    maps the different pages the user can browse

    :param icon: icon to display
    :param title: title of the page
    :param navigation_link: link to navigate to
    :return: NavLink component
    """
    link_content = html.Div([icon, html.Div(title)], style={'display': 'inline-flex'})
    return dash_bootstrap_components.NavLink(link_content, href=navigation_link, style={'padding': '.5em 1em'})


navigation_bar = dash_bootstrap_components.Nav([
    create_navigation_link(NavigationBarIcons.PROFILE_MANAGER, PageTitles.PROFILE_MANAGER, PageRoutes.PROFILE_MANAGER),
    create_navigation_link(NavigationBarIcons.TEST_CASE_MANAGER, PageTitles.TEST_CASE_MANAGER,
                           PageRoutes.TEST_CASE_MANAGER),
    create_navigation_link(NavigationBarIcons.RUN_SIMULATOR, PageTitles.RUN_SIMULATOR, PageRoutes.RUN_SIMULATOR),
], vertical=True, pills=True, className='sidebar')
