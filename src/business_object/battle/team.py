from typing import List
from business_object.battle.joueur_in_team import JoueurInTeam


class Team:
    def __init__(self, id) -> None:
        self._id = id
        self._member : List[JoueurInTeam] = None