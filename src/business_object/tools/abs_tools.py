from abc import ABC, abstractmethod
class AbsTools(ABC):
    def __init__(self, tools_id, name) -> None:
        self.tools_id = tools_id
        self.name = name
    