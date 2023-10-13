from typing import List
from business_object.user.joueur import Joueur


class Team:
    def __init__(self, id_, side) -> None:
        self._id = id_
        self._member: List[Joueur] = None
        self._side: side
