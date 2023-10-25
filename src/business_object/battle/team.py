from typing import List
from business_object.user.joueur import Joueur


class Team:
    def __init__(self, team_id="", side=None) -> None:
        self.team_id = team_id
        self.side = side
