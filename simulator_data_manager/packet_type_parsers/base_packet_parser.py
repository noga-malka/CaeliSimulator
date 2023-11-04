from abc import abstractmethod, ABC
from threading import Event
from typing import Any, Union


class BasePacketParser(ABC):
    """
    Abstract packet parser. Each type of received packet should implement it
    """

    def __init__(self, initial_value: Any):
        # we save the initial value separately for resetting the data
        self._initial_value = initial_value
        # create a unique event for this parser. Can be used to alert when this type of packet arrives
        self._event = Event()
        self._saved_data = initial_value

    @abstractmethod
    def save(self, content: Union[str, dict]):
        """
        format and save the given packet content inside self._saved_data
        :param content: data sent from the simulator. Can be either a string or a dictionary
        """
        ...

    def get_saved_data(self) -> Any:
        """
        :return: the parser's saved data
        """
        return self._saved_data

    def get_event(self) -> Event:
        """
        :return: the parser's event
        """
        return self._event

    def clear_saved_data(self):
        """
        reset self._saved_data into the initial value of this parser
        """
        self._saved_data = self._initial_value
