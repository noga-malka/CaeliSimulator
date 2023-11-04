class NameAlreadyExistsException(Exception):
    def __init__(self, name: str):
        self.message = f"Error: Name {name} already exists in database"

    def __str__(self):
        return self.message
