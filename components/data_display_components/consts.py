class DisplayDataContainer:
    ID = 'live_data'
    NEW_CARD = 'add_new_card_button'


class Size:
    FULL = '100%'
    HALF = '50%'
    ONE_THIRD = '33%'
    QUARTER = '25%'

    ALL = [FULL, HALF, ONE_THIRD, QUARTER]


TICKS_TO_SECOND = 5


class Display:
    GRAPH = 'Graph'
    TEXT = 'Text'
    TIMER = 'Timer'

    ALL = [GRAPH, TEXT, TIMER]


class LengthInMinutes:
    HALF = 0.5
    ONE = 1
    TWO = 2
    THREE = 3
    FIVE = 5

    ALL = [dict(label=f'{minutes}m', value=minutes) for minutes in [HALF, ONE, TWO, THREE, FIVE]]


class CardIdType:
    TITLE = 'title'
    CONTENT = 'content'
    INPUTS = 'inputs'
    UPDATE_INPUTS = 'update_inputs'
    CARD = 'card'
    DISPLAY = 'display'
    SIZE = 'size'
    TYPING = 'typing'
    DELETE = 'delete'
    LENGTH = 'length'
