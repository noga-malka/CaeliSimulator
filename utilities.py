import logging

from dash import no_update
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashLogger


def log_function(function):
    def inner(*args, **kwargs):
        formatted_arguments = [str(argument) for argument in args]
        formatted_kwargs = {key: str(value) for key, value in kwargs.items()}
        print(f'log_function: {function.__name__}: {formatted_arguments}, {formatted_kwargs}')
        return function(*args, **kwargs)

    return inner


def int_to_bytes(payload: int, byte_count: int = 2):
    return payload.to_bytes(byte_count, 'big')


def validate_arguments(*args):
    if not any(args):
        raise PreventUpdate


def dash_logging(logger: DashLogger, message, level: int = logging.INFO):
    logger.log(level, message, autoClose=5000)
    return no_update
