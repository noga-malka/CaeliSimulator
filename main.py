import dash
from dash import dcc
from dash_extensions.enrich import html, DashProxy, LogTransform

from components.io_components.input_connection_buttons import io_connection_buttons
from components.navigation_bar import navigation_bar
from components.placeholder import placeholder
from components.simulator_components.consts import ProgressBar
from components.title import title
from database.database_manager import DatabaseManager
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

app = DashProxy(__name__,
                suppress_callback_exceptions=True,
                use_pages=True,
                transforms=[LogTransform()],
                title='Caeli')

app.layout = html.Div([
    title,
    placeholder,
    html.Div([
        navigation_bar,
        dcc.Store(ProgressBar.CURRENT_TEST_CASE),
        html.Div([
            io_connection_buttons,
            dash.page_container  # here we insert each page content
        ], className='full-width')
    ], className='flex', style={'height': '100vh'})])

if __name__ == '__main__':
    SimulatorDataManager()
    DatabaseManager()
    app.run(host='0.0.0.0', debug=True)
