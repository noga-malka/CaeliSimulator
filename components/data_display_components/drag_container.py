from dash import html, clientside_callback, ClientsideFunction, Output, Input


def generate_draggable_children_div(div_id: str, children: list) -> html.Div:
    """
    :param div_id: unique id of the parent div
    :param children: list of components to drag inside
    :return: the generated div with dragging enabled
    """
    parent_div = html.Div(id=div_id, className="container flex-wrap", children=children)

    clientside_callback(
        ClientsideFunction(namespace="clientside", function_name="make_draggable"),
        Output(div_id, "data-drag"),
        [Input(div_id, "id")],
    )
    return parent_div
