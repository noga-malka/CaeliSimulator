from database.base_manager import BaseManager
from models.test_case import TestCase


class TestCaseManager(BaseManager):
    def get(self, test_case_name: str) -> TestCase:
        """
        get TestCase object by name

        :param test_case_name: name to extract
        :return: TestCase Object
        :raises: NameDoesNotExistsException if the test case does not exist
        """
        self.validate_instance_exists(instance_name=test_case_name)
        return self._instances.get(test_case_name)

    def add(self, test_case: TestCase):
        """
        save the given test case in the test cases' dictionary

        :param test_case: TestCase Object
        :raises: NameAlreadyExistsException if the test case does not exist
        """
        self.validate_instance_does_not_exist(instance_name=test_case.name)
        self._instances[test_case.name] = test_case
        self.save_function()

    def remove(self, test_case_name: str):
        """
        remove the test case from the test cases' dictionary

        :param test_case_name: name to remove
        :raises: NameDoesNotExistsException if the profile does not exist
        """
        self.validate_instance_exists(instance_name=test_case_name)
        self._instances.pop(test_case_name)
        self.save_function()
