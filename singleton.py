from abc import abstractmethod, ABC


class Singleton(ABC):
    _instance = None

    def __new__(cls):
        """
        convert any child classes into a singleton class
        """
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.initiate()
        return cls._instance

    @abstractmethod
    def initiate(self):
        ...
