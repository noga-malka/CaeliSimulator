import dash_bootstrap_components
import pandas

from components.simulator_components.live_data.consts import DisplayOptions


def build_simulator_display_grid(data: pandas.DataFrame):
    data_grid = []
    for row in DisplayOptions.SIMULATOR_RESOLVER:
        data_columns = [component.create_column(field_name, data[field_name]) for field_name, component in row.items()]
        data_grid.append(dash_bootstrap_components.Row(data_columns))
    return data_grid
