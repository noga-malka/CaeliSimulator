from dash import callback, Output, Input, State

from components.data_display_components.configurable_card import generate_configurable_card
from components.data_display_components.consts import DisplayDataContainer
from components.general_components.add_button import create_add_button

add_new_card = create_add_button(DisplayDataContainer.NEW_CARD)


@callback(
    Output(DisplayDataContainer.ID, 'children'),
    State(DisplayDataContainer.ID, 'children'),
    Input(DisplayDataContainer.NEW_CARD, 'n_clicks'),
    prevent_initial_call=True
)
def add_new_card_to_layout(current_cards: list, button_clicked: int):
    card_id = str(len(current_cards) + 1)
    current_cards.append(generate_configurable_card(card_id)),
    return current_cards
