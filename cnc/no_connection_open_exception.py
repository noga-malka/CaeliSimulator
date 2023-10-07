class NoConnectionOpenException(Exception):
    def __init__(self, command_name: str):
        self.message = f'Error: No connection open. Can not send command: {command_name}'

    def __str__(self):
        return self.message
