import dash_bootstrap_components
from dash import html

from components.consts import ProfileForm
from components.input_card import build_input_card_component

add_profile_form = html.Div([
    html.Div([
        html.Div([
            build_input_card_component('Set Inspirium Time', ProfileForm.Inputs.INSPIRIUM_TIME, 0, 100),
            build_input_card_component('Set Inspirium Hold Time', ProfileForm.Inputs.INSPIRIUM_HOLD_TIME, 0, 100),
        ], className='flex'),
        html.Div([
            build_input_card_component('Set Expirium Time', ProfileForm.Inputs.EXPIRIUM_TIME, 0, 100),
            build_input_card_component('Set Expirium Hold Time', ProfileForm.Inputs.EXSPIRIUM_HOLD_TIME, 0, 100),
        ], className='flex'),
        html.Div([
            build_input_card_component('Set Tidal Volume', ProfileForm.Inputs.TIDAL_VOLUME, 0, 100),
            build_input_card_component('Set Profile Time Span', ProfileForm.Inputs.TIME_SPAN, 0, 100),
        ], className='flex'),
        dash_bootstrap_components.Button('Add Profile', ProfileForm.ADD_PROFILE_BUTTON)
    ], style={'align-items': 'center', 'flex-direction': 'column'}, className='flex')
], style={'width': '100%'})
