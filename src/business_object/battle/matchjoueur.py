from business_object.user.joueur import Joueur


class MatchJoueur:
    def __init__(
        self, match_id, joueur, champion, items, lane, team, stat_joueur
    ) -> None:
        self.match_id = match_id
        self.joueur = joueur
        self.champion = champion
        self.items = items
        self.lane = lane
        self.team = team
        self.stat_joueur = stat_joueur
