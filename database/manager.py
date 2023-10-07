from abc import abstractmethod


class Manager:
    def __init__(self, save_function: callable):
        """
        :param save_function: function to trigger after making changes in the manager's data
        """
        self.save_function = save_function

    @abstractmethod
    def get(self, name: str):
        ...

    @abstractmethod
    def add(self, instance):
        ...

    @abstractmethod
    def remove(self, instance):
        ...
