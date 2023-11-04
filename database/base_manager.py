from abc import abstractmethod
from typing import Any

from database.exceptions.name_already_exists_exception import NameAlreadyExistsException
from database.exceptions.name_does_not_exists_exception import NameDoesNotExistsException


class BaseManager:
    """
    Abstract manager. All other managers must implement it
    """

    def __init__(self, save_function: callable):
        """
        :param save_function: function to trigger after making changes in the manager's data
        """
        self.save_function = save_function
        self._instances: dict = {}

    def validate_instance_exists(self, instance_name: str):
        """
        check that the given instance is inside self._instances
        :param instance_name: instance to check
        :raises NameDoesNotExistsException if the instance is not in self._instances
        """
        if instance_name not in self._instances:
            raise NameDoesNotExistsException(instance_name)

    def validate_instance_does_not_exist(self, instance_name: str):
        """
        check that the given instance is not inside self._instances
        :param instance_name: instance to check
        :raises NameAlreadyExistsException if the instance is in self._instances
        """
        if instance_name in self._instances:
            raise NameAlreadyExistsException(instance_name)

    def get_names(self) -> list[str]:
        """
        :return: list of keys inside self._instances
        """
        return list(self._instances.keys())

    def get_instances(self) -> list[str]:
        """
        :return: list of values inside self._instances
        """
        return list(self._instances.values())

    @abstractmethod
    def get(self, instance_name: str):
        ...

    @abstractmethod
    def add(self, instance: Any):
        ...

    @abstractmethod
    def remove(self, instance_name: str):
        ...
