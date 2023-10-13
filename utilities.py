def log_function(function):
    def inner(*args, **kwargs):
        formatted_arguments = [str(argument) for argument in args]
        formatted_kwargs = {key: str(value) for key, value in kwargs.items()}
        print(f'log_function: {function.__name__}: {formatted_arguments}, {formatted_kwargs}')
        return function(*args, **kwargs)

    return inner
