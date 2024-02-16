import dash
from dash import callback, Output, Input, State, callback_context, ALL

from components.data_display_components.configurable_card import generate_configurable_card
from components.data_display_components.consts import DisplayDataContainer, CardIdType
from components.general_components.add_button import create_add_button
from utilities import validate_arguments

add_new_card = create_add_button(DisplayDataContainer.NEW_CARD)


@callback(
    Output(DisplayDataContainer.ID, 'children', allow_duplicate=True),
    State(DisplayDataContainer.ID, 'children'),
    Input(DisplayDataContainer.NEW_CARD, 'n_clicks'),
    prevent_initial_call=True
)
def add_new_card_to_layout(current_cards: list, button_clicked: int):
    card_id = str(len(current_cards) + 1)
    current_cards.append(generate_configurable_card(card_id)),
    return current_cards


@callback(
    Output(DisplayDataContainer.ID, 'children', allow_duplicate=True),
    State(DisplayDataContainer.ID, 'children'),
    Input({'index': ALL, 'type': CardIdType.DELETE}, 'n_clicks'),
    prevent_initial_call=True
)
def delete_card(current_cards: list, buttons_clicked: list[int]):
    validate_arguments(*buttons_clicked)
    card_id_to_remove = callback_context.triggered_id['index']
    for index in range(len(current_cards)):
        if current_cards[index]['props']['id']['index'] == card_id_to_remove:
            current_cards.pop(index)
            return current_cards
    return dash.no_update
