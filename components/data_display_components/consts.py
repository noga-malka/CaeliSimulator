from simulator_data_manager.packet_type_parsers.consts import SimulatorKeys, CruesoKeys


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


class Inputs:
    STATIC_OPTIONS = [SimulatorKeys.INDEX,
                      SimulatorKeys.PROFILE_RUN_TIME,
                      SimulatorKeys.TOTAL_RUN_TIME,
                      SimulatorKeys.CURRENT_PROFILE,
                      SimulatorKeys.TOTAL_INTERVALS,
                      SimulatorKeys.BREATH_VOLUME,
                      SimulatorKeys.BREATH_STATE,
                      SimulatorKeys.CRITICAL_FLAG,
                      SimulatorKeys.SIMULATOR_STATUS,
                      CruesoKeys.PRESSURE_1,
                      CruesoKeys.TACH_B_1,
                      CruesoKeys.PRESSURE_2,
                      CruesoKeys.TACH_B_2]


class CardIdType:
    TITLE = 'title'
    CONTENT = 'content'
    INPUTS = 'inputs'
    CARD = 'card'
    DISPLAY = 'display'
    SIZE = 'size'
    TYPING = 'typing'
    DELETE = 'delete'
