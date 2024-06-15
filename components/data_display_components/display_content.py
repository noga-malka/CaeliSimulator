import datetime

import pandas
from dash import dcc, html
from plotly import express

from components.data_display_components.consts import Display, TICKS_TO_SECOND


def display_graph(columns: list[str], dataframe: pandas.DataFrame):
    figure = express.line(dataframe, y=columns, x=dataframe.index / TICKS_TO_SECOND)
    figure.update_layout(showlegend=False,
                         yaxis_title=','.join(columns),
                         xaxis_title='Seconds',
                         uirevision="Don't change",
                         xaxis=dict(dtick=TICKS_TO_SECOND))
    return dcc.Graph(figure=figure,
                     style={'height': '300px'},
                     config={
                         'displayModeBar': False,
                         'showAxisRangeEntryBoxes': False,
                         'showTips': False,
                     })


def display_text(columns: list[str], dataframe: pandas.DataFrame):
    last_row = dataframe.iloc[-1]
    text = [f'{column}: {int(last_row[column])}' for column in columns]
    return html.Div(', '.join(text), className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})


def display_timer(columns: list[str], dataframe: pandas.DataFrame):
    last_row = dataframe.iloc[-1]
    timer = [f'{column}: {str(datetime.timedelta(seconds=int(last_row[column])))}' for column in columns]
    return html.Div(', '.join(timer), className='flex-center', style={'font-size': '30px', 'font-weight': 'bold'})


DISPLAY_TYPES = {
    Display.GRAPH: display_graph,
    Display.TEXT: display_text,
    Display.TIMER: display_timer,
}
