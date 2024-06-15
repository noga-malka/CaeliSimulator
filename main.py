import dash
from dash import dcc
from dash_extensions.enrich import html, DashProxy, LogTransform

from components.io_components.bluetooth import bluetooth_connection_buttons, bluetooth_connection_modal
from components.io_components.serial import serial_connection_buttons, serial_connection_modal
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
            html.Div([
                html.Div(serial_connection_buttons, style=dict(width='50%')),
                html.Div(bluetooth_connection_buttons, style=dict(width='50%')),
                serial_connection_modal,
                bluetooth_connection_modal,
            ], className='bg-secondary flex-center flex-row'),
            dash.page_container  # here we insert each page content
        ], className='full-width')
    ], className='flex', style={'height': '100vh'})])

if __name__ == '__main__':
    SimulatorDataManager()
    DatabaseManager()
    app.run(host='0.0.0.0', debug=True)
