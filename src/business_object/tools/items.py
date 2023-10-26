from business_object.tools.abs_tools import AbsTools

class Item(AbsTools):
    def __init__(self, item_id, name, item_position = None) -> None:
        super().__init__(item_id,name)
        self.item_position = item_position

    def __str__(self) -> str:
        return("Item : " + self.name)