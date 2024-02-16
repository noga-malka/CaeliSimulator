import pandas
from dash import dcc, html
from plotly import express


def display_graph(yaxis: str, dataframe: pandas.DataFrame):
    figure = express.line(dataframe)
    figure.update_layout(showlegend=False, yaxis_title=yaxis)
    return dcc.Graph(figure=figure,
                     style={'height': '300px'},
                     config={
                         'displayModeBar': False,
                         'showAxisRangeEntryBoxes': False,
                         'showTips': False,
                     })


def display_text(title: str, dataframe: pandas.DataFrame):
    return html.Div(dataframe.iloc[-1], className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})


def display_timer(title: str, dataframe: pandas.DataFrame):
    seconds = int(dataframe.iloc[-1])
    timer = '{:0>2}:{:0>2}'.format(int((seconds / 60) % 60), seconds % 60)
    html.Div(timer, className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})


DISPLAY_TYPES = {
    'Graph': display_graph,
    'Text': display_text,
    'Timer': display_timer,
}
