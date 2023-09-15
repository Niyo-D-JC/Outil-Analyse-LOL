from business_object.battle.team import Team


class Match:
    def __init__(self, match_id, team1, team2, duration,winner) -> None:
        self._match_id = match_id
        self._team1 : Team = team1
        self._team2 : Team = team2
        self._duration = duration
        self._winner = winner