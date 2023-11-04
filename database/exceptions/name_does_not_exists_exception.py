class NameDoesNotExistsException(Exception):
    def __init__(self, name: str):
        self.message = f"Error: Name {name} does not exists in database"

    def __str__(self):
        return self.message
