import os.path
import pickle

from database.consts import FileNames
from database.managers.display_manager import DisplayManager
from database.managers.profile_manager import ProfileManager
from database.managers.test_case_manager import TestCaseManager
from singleton import Singleton


class DatabaseManager(Singleton):
    def initiate(self):
        self._saved_database = self._load_saved_database()
        self.test_case_manager = self._get_test_case_manager()
        self.profile_manager = self._get_profile_manager()
        self.display_manager = self._get_display_card_manager()

    @property
    def has_saved_database(self) -> bool:
        """
        :return: True if there is a saved database, else False
        """
        return self._saved_database is not None

    def _get_test_case_manager(self) -> TestCaseManager:
        """
        If there is a saved database, return its TestCaseManager object, else create a new one
        :return: TestCaseManager object
        """
        if self.has_saved_database:
            return self._saved_database.test_case_manager
        return TestCaseManager(self.save_database)

    def _get_profile_manager(self) -> ProfileManager:
        """
        If there is a saved database, return its ProfileManager object, else create a new one
        :return: ProfileManager object
        """
        if self.has_saved_database:
            return self._saved_database.profile_manager
        return ProfileManager(self.save_database)

    def _get_display_card_manager(self) -> DisplayManager:
        """
        If there is a saved database, return its DisplayManager object, else create a new one
        :return: DisplayManager object
        """
        if self.has_saved_database:
            return self._saved_database.display_manager
        return DisplayManager(self.save_database)

    def save_database(self):
        """
        Save the current DatabaseManager instance in a file
        """
        self._pickle_database(FileNames.DATABASE)
        self._backup()

    def _backup(self):
        """
        Save the current DatabaseManager instance in a backup file
        """
        self._pickle_database(FileNames.BACKUP)

    def _pickle_database(self, file_name: str):
        """
        Dump the current Object into a file for future loading

        :param file_name: the path to the file to save the current DatabaseManager into
        """
        with open(file_name, 'wb') as database_file:
            pickle.dump(self, database_file)

    @staticmethod
    def _fetch_saved_database(file_name: str) -> "DatabaseManager":
        """
        :param file_name: the path to the saved database file
        :return: DatabaseManager object loaded from the given file
        """
        with open(file_name, 'rb') as database_file:
            return pickle.load(database_file)

    def _load_saved_database(self) -> "DatabaseManager":
        """
        Check if a saved or backup file found. If so, extract them, else return None

        :return: DatabaseManager object if found, else None
        """
        if os.path.isfile(FileNames.DATABASE):
            return self._fetch_saved_database(FileNames.DATABASE)
        elif os.path.isfile(FileNames.BACKUP):
            return self._fetch_saved_database(FileNames.BACKUP)
