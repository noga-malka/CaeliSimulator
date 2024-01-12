import pandas
from dash import html


def build_simulator_display_grid(data: pandas.DataFrame, display_type_resolver: list[dict]):
    data_grid = []
    for row in display_type_resolver:
        data_columns = [component.create_column(field_name, data[field_name]) for field_name, component in row.items()]
        data_grid.append(html.Div(data_columns, className='flex-row'))
    return data_grid
