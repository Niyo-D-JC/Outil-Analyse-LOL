from business_object.tools.abs_tools import AbsTools

class Champion(AbsTools):
    def __init__(self, champion_id, name) -> None:
        super().__init__(champion_id,name)

    def __str__(self) -> str:
        return("Champion : " + self.name)
