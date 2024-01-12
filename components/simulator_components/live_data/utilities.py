import dash_bootstrap_components
import pandas


def build_simulator_display_grid(data: pandas.DataFrame, display_type_resolver: list[dict]):
    data_grid = []
    for row in display_type_resolver:
        data_columns = [component.create_column(field_name, data[field_name]) for field_name, component in row.items()]
        data_grid.append(dash_bootstrap_components.Row(data_columns))
    return data_grid
