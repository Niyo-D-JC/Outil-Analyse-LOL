from business_object.tools.abs_tools import AbsTools

class Item(AbsTools):
    def __init__(self, item_id, name) -> None:
        super().__init__(item_id,name)
    
    def __str__(self) -> str:
        return("Item : " + self.name)