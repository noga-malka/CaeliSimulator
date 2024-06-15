from dash import html

from components.io_components.bluetooth import bluetooth_connection_modal, bluetooth_connection_buttons
from components.io_components.serial import serial_connection_modal, serial_connection_buttons

io_connection_buttons = html.Div([
    html.Div(serial_connection_buttons, style=dict(width='50%')),
    html.Div(bluetooth_connection_buttons, style=dict(width='50%')),
    serial_connection_modal,
    bluetooth_connection_modal,
], className='bg-secondary flex-center flex-row')
