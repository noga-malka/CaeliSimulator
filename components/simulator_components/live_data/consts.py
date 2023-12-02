from components.simulator_components.live_data.graph_live_data import GraphLiveData
from components.simulator_components.live_data.text_live_data import TextLiveData
from components.simulator_components.live_data.timer_live_data import TimerLiveData
from simulator_data_manager.packet_type_parsers.consts import SimulatorKeys


class DisplayOptions:
    TIMER = TimerLiveData()
    GRAPH = GraphLiveData()
    PLAIN_TEXT = TextLiveData()

    SIMULATOR_RESOLVER = [
        {
            SimulatorKeys.PULSE_WIDTH: GRAPH,
            SimulatorKeys.RPM: GRAPH,
        },
        {
            SimulatorKeys.FREQUENCY: GRAPH,
        },
    ]
