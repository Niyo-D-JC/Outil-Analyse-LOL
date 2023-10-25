from business_object.tools.abs_tools import AbsTools

class Lane(AbsTools):
    def __init__(self, lane_id, name) -> None:
        super().__init__(lane_id,name)
    
    def __str__(self) -> str:
        return("Item : " + self.name)

LANE = {"TOP": 1, "JUNGLE": 2, "BOTTOM":3, "MIDDLE": 4, "NONE": 5}