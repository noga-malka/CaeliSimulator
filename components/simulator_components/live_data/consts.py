from components.simulator_components.live_data.graph_live_data import GraphLiveData
from components.simulator_components.live_data.text_live_data import TextLiveData
from components.simulator_components.live_data.timer_live_data import TimerLiveData
from simulator_data_manager.packet_type_parsers.consts import SimulatorKeys, CruesoKeys


class DisplayOptions:
    TIMER = TimerLiveData()
    GRAPH = GraphLiveData()
    PLAIN_TEXT = TextLiveData()

    DISPLAY_TYPE_RESOLVER = [
        {
            SimulatorKeys.BREATH_VOLUME: GRAPH,
        },
        {
            frozenset([CruesoKeys.TACH_B_1, CruesoKeys.TACH_B_2]): GRAPH,
        },
        {
            CruesoKeys.PRESSURE_1: GRAPH,
        },
        {
            CruesoKeys.PRESSURE_2: GRAPH,
        },
        {
            SimulatorKeys.TOTAL_RUN_TIME: TIMER,
            SimulatorKeys.PROFILE_RUN_TIME: TIMER,
            SimulatorKeys.CURRENT_PROFILE: PLAIN_TEXT,
            SimulatorKeys.TOTAL_INTERVALS: PLAIN_TEXT,
        },
        {
            SimulatorKeys.BREATH_STATE: GRAPH,
            SimulatorKeys.CRITICAL_FLAG: GRAPH,
            SimulatorKeys.SIMULATOR_STATUS: GRAPH,
        }]
