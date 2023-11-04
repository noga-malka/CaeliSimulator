import dash_bootstrap_components
from dash import html


def create_modal(title: str, modal_id: str, content: list) -> dash_bootstrap_components.Modal:
    """
    create a modal with the given title, id and content

    :param title: modal's title
    :param modal_id: unique id
    :param content: modal's content. list of components
    :return: the modal component
    """
    return dash_bootstrap_components.Modal([
        dash_bootstrap_components.ModalHeader(html.H3(title)),
        dash_bootstrap_components.ModalBody(content, style={'align-items': 'center'}, className='flex-column')],
        id=modal_id)
