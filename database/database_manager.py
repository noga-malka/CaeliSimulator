import os.path
import pickle

from database.consts import FileNames
from database.profile_manager import ProfileManager
from database.test_case_manager import TestCaseManager


class DatabaseManager:
    _instance = None

    def __new__(cls):
        """
        convert DatabaseManager into a singleton class
        """
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.saved_database = cls._instance.load()
            cls._instance.test_case_manager = cls._instance.get_test_case_manager()
            cls._instance.profile_manager = cls._instance.get_profile_manager()
        return cls._instance

    def get_test_case_manager(self) -> TestCaseManager:
        if self.saved_database is not None:
            return self.saved_database.test_case_manager
        return TestCaseManager(self.save)

    def get_profile_manager(self) -> ProfileManager:
        if self.saved_database is not None:
            return self.saved_database.profile_manager
        return ProfileManager(self.save)

    def save(self):
        self._pickle_database(FileNames.DATABASE)
        self._backup()

    def _backup(self):
        self._pickle_database(FileNames.BACKUP)

    def _pickle_database(self, file_name: str):
        with open(file_name, 'wb') as database_file:
            pickle.dump(self, database_file)

    @staticmethod
    def load():
        if os.path.isfile(FileNames.DATABASE):
            file_name = FileNames.DATABASE
        elif os.path.isfile(FileNames.BACKUP):
            file_name = FileNames.BACKUP
        else:
            return None
        with open(file_name, 'rb') as database_file:
            return pickle.load(database_file)
