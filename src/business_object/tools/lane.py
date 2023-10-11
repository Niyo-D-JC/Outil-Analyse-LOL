
class Lane(AbsTools):
    def __init__(self, id, name) -> None:
        super().__init__(self,id,name)
    
    def __str__(self) -> str:
        return("Item : " + self._name)