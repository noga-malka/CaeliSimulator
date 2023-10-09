import dash_bootstrap_components
from dash import html


def create_modal(title: str, modal_id: str, body: list):
    return dash_bootstrap_components.Modal([
        dash_bootstrap_components.ModalHeader(html.H3(title)),
        dash_bootstrap_components.ModalBody(body, style={'align-items': 'center', 'flex-direction': 'column'},
                                            className='flex')], id=modal_id)
