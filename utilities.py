def log_function(function):
    def inner(*args, **kwargs):
        print(f'Function: {function.__name__}. Arguments: {args}, {kwargs}')
        return function(*args, **kwargs)

    return inner
