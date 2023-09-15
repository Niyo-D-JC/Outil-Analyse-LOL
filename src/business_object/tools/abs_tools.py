from abc import ABC, abstractmethod
class AbsTools(ABC):
    def __init__(self, id, name) -> None:
        self._id = id
        self._name = name
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        pass

    @property
    def name(self):
        return self._name
    @id.setter
    def name(self, new_name):
        self._name = new_name