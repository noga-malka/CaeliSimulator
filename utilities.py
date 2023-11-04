import logging
from typing import Union

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


def int_to_bytes(payload: int, byte_count: int = 2) -> bytes:
    """
    :param payload: numeric payload to convert
    :param byte_count: number of bytes to generate
    :return: the bytes value of the given payload
    """
    return payload.to_bytes(byte_count, 'big')


def validate_arguments(*args):
    """
    if none of the given arguments does not have a valid data, raise PreventUpdate to stop the output components update
    :param args: list of arguments to validate
    :raises: dash's PreventUpdate exception
    """
    if not any(args):
        raise PreventUpdate


def ui_logger(logger: DashLogger, message: Union[str, Exception], level: int = logging.ERROR):
    """
    :param logger: DashLogger object to send log
    :param message: message to display, if it is an exception we convert to string
    :param level: the log level
    :return: dash no_update value to prevent output component update
    """
    logger.log(level, str(message), autoClose=5000)
    return no_update
