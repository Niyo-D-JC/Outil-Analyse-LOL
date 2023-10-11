from typing import List
from business_object.battle.joueur_in_team import JoueurInTeam


class Team:
    def __init__(self, id_, side) -> None:
        self._id = id_
        self._member : List[JoueurInTeam] = None
        self._side : side