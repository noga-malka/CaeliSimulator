import pandas
from dash import html


def multiple_inputs_grid(field_names: frozenset, component, data: pandas.DataFrame):
    field_names = [column for column in field_names if column in data.columns]
    if field_names:
        return component.create_column(', '.join(field_names), data[field_names].dropna())


def single_input_grid(field_name: str, component, data: pandas.DataFrame):
    if field_name in data.columns:
        return component.create_column(field_name, data[field_name].dropna())


def build_live_data_display_grid(data: pandas.DataFrame, display_type_resolver: list[dict]):
    data_grid = []
    for row in display_type_resolver:
        data_columns = []
        for field_name, component in row.items():
            generated_grid = None
            if type(field_name) == str:
                generated_grid = single_input_grid(field_name, component, data)
            elif type(field_name) == frozenset:
                generated_grid = multiple_inputs_grid(field_name, component, data)

            if generated_grid:
                data_columns.append(generated_grid)
        data_grid.append(html.Div(data_columns, className='flex-row'))
    return data_grid
