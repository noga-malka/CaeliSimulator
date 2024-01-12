from dash import html

from components.simulator_components.inputs.crueso import crueso_connection_modal, crueso_connection_buttons
from components.simulator_components.inputs.simulator import simulator_connection_modal, simulator_connection_buttons

control_buttons = html.Div([
    html.Div(simulator_connection_buttons, style=dict(width='50%')),
    html.Div(crueso_connection_buttons, style=dict(width='50%')),
    simulator_connection_modal,
    crueso_connection_modal,
], className='bg-secondary flex-center flex-row')
