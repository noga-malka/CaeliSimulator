from database.manager import Manager
from database.name_already_exists_exception import NameAlreadyExistsException
from models.test_case import TestCase


class TestCaseManager(Manager):
    def __init__(self, save_function: callable):
        super().__init__(save_function)
        self.test_cases: dict[str, TestCase] = {}  # {name: TestCase object}

    def _does_test_case_exist(self, test_case_name: str):
        return test_case_name in self.test_cases

    def get(self, test_case_name: str) -> TestCase:
        if not self._does_test_case_exist(test_case_name):
            raise NameAlreadyExistsException(test_case_name)

        return self.test_cases.get(test_case_name)

    def add(self, test_case: TestCase):
        if self._does_test_case_exist(test_case.name):
            raise NameAlreadyExistsException(test_case.name)

        self.test_cases[test_case.name] = test_case
        self.save_function()

    def remove(self, test_case: TestCase):
        if not self._does_test_case_exist(test_case.name):
            raise NameAlreadyExistsException(test_case.name)

        self.test_cases.pop(test_case.name)
        self.save_function()
