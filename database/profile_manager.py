from database.manager import Manager
from database.name_already_exists_exception import NameAlreadyExistsException
from models.profile import Profile


class ProfileManager(Manager):
    def __init__(self):
        self.profiles: dict[str, Profile] = {}  # {name: Profile object}

    def _does_profile_exist(self, profile_name: str):
        return profile_name in self.profiles

    def get(self, profile_name: str) -> Profile:
        if not self._does_profile_exist(profile_name):
            raise NameAlreadyExistsException(profile_name)

        return self.profiles.get(profile_name)

    def add(self, profile: Profile):
        if self._does_profile_exist(profile.name):
            raise NameAlreadyExistsException(profile.name)
        self.profiles[profile.name] = profile

    def remove(self, profile: Profile):
        if not self._does_profile_exist(profile.name):
            raise NameAlreadyExistsException(profile.name)
        self.profiles.pop(profile.name)
