from abc import abstractmethod


class Manager:
    @abstractmethod
    def get(self, name: str):
        ...

    @abstractmethod
    def add(self, instance):
        ...

    @abstractmethod
    def remove(self, instance):
        ...
