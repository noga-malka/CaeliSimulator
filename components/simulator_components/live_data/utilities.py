import pandas
from dash import html


def build_live_data_display_grid(data: pandas.DataFrame, display_type_resolver: list[dict]):
    data_grid = []
    for row in display_type_resolver:
        data_columns = []
        for field_name, component in row.items():
            if field_name in data.columns:
                data_columns.append(component.create_column(field_name, data[field_name]))
        data_grid.append(html.Div(data_columns, className='flex-row'))
    return data_grid
