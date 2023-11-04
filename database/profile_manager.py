from database.base_manager import BaseManager
from models.profile import Profile


class ProfileManager(BaseManager):
    def __init__(self, save_function: callable):
        super().__init__(save_function)

    def get(self, profile_name: str) -> Profile:
        """
        get Profile object by name

        :param profile_name: name to extract
        :return: Profile Object
        :raises: NameDoesNotExistsException if the profile does not exist
        """
        self.validate_instance_exists(instance_name=profile_name)
        return self._instances.get(profile_name)

    def add(self, profile: Profile):
        """
        save the given profile in the profiles' dictionary

        :param profile: Profile Object
        :raises: NameAlreadyExistsException if the profile does not exist
        """
        self.validate_instance_does_not_exist(instance_name=profile.name)
        self._instances[profile.name] = profile
        self.save_function()

    def remove(self, profile_name: str):
        """
        remove the profile from the profiles' dictionary

        :param profile_name: name to remove
        :raises: NameDoesNotExistsException if the profile does not exist
        """
        self.validate_instance_exists(instance_name=profile_name)
        self._instances.pop(profile_name)
        self.save_function()
