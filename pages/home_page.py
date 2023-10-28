import dash
from dash import html

dash.register_page(
    __name__,
    path='/',
    title='Home'
)

layout = html.Div(
    html.H1('Calei\'s Breath Simulator')
    , className='flex-center')
