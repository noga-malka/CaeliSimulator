from dash import dcc, callback, Output, Input

from components.consts import Placeholder
from simulator_data_manager.packet_type import PacketType

save_data_interval = dcc.Interval(id='interval', interval=1000)


@callback(Output(Placeholder.ID, Placeholder.Fields.CONTEXT_MENU),
          Input('interval', 'n_intervals'),
          prevent_initial_call=True)
def update_saved_data(interval):
    print(PacketType.Data.value.saved_data)
