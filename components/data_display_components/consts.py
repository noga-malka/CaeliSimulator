class DisplayDataContainer:
    ID = 'live_data'
    NEW_CARD = 'add_new_card_button'


class Size:
    FULL = '100%'
    HALF = '50%'
    ONE_THIRD = '33%'
    QUARTER = '25%'

    ALL = [FULL, HALF, ONE_THIRD, QUARTER]


class Display:
    GRAPH = 'Graph'
    TEXT = 'Text'
    TIMER = 'Timer'

    ALL = [GRAPH, TEXT, TIMER]


class CardIdType:
    TITLE = 'title'
    CONTENT = 'content'
    INPUTS = 'inputs'
    CARD = 'card'
    DISPLAY = 'display'
    SIZE = 'size'
    TYPING = 'typing'
    DELETE = 'delete'
