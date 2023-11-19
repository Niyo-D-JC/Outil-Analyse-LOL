from business_object.tools.abs_tools import AbsTools


class Lane(AbsTools):
    def __init__(self, lane_id, name) -> None:
        super().__init__(lane_id, name)

    def __str__(self) -> str:
        return "Lane : " + self.name


LANE = {"TOP": 1, "JUNGLE": 2, "MIDDLE": 3, "BOTTOM": 4, "UTILITY": 5, "NONE": 6, "": 6}
