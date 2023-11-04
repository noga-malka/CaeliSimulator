import dash
from dash import html

from pages.consts import PageRoutes, PageTitles

dash.register_page(__name__, path=PageRoutes.HOME, title=PageTitles.HOME)

# todo: build home page
layout = html.Div([], className='flex-center')
