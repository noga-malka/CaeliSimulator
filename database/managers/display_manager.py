from database.base_manager import BaseManager
from models.display import DisplayCard


class DisplayManager(BaseManager):

    def get(self, display_card_name: str) -> DisplayCard:
        """
        get Display object by name

        :param display_card_name: name to extract
        :return: Display Object
        :raises: NameDoesNotExistsException if the display card does not exist
        """
        self.validate_instance_exists(instance_name=display_card_name)
        return self._instances.get(display_card_name)

    def add(self, display_card: DisplayCard):
        """
        save the given display_card in the display_cards' dictionary

        :param display_card: DisplayCard Object
        """
        self._instances[display_card.card_id] = display_card
        self.save_function()

    def remove(self, display_card_name: str):
        """
        remove the display_card from the display_cards' dictionary

        :param display_card_name: name to remove
        :raises: NameDoesNotExistsException if the display_card does not exist
        """
        self.validate_instance_exists(instance_name=display_card_name)
        self._instances.pop(display_card_name)
        self.save_function()
