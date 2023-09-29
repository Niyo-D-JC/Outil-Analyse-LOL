from typing import List
from business_object.stats.stat_joueur import StatJoeur
from business_object.tools.abs_tools import AbsTools
from business_object.user.joueur import Joueur

from enum import Enum

class TeamPosition(Enum):
    TOP = "TOP"
    JUNGLE = "JUNGLE"
    MID = "MID"
    AD = "AD"
    SUPPORT = "SUPPORT"


class JoueurInTeam:
    def __init__(self, joueur, team_position, champion) -> None:
        self._joueur : Joueur = joueur
        self._team_position : TeamPosition = team_position
        self._champion : AbsTools = champion
        self._items : List[AbsTools] = None
        self._stat_joueur : StatJoueur = None