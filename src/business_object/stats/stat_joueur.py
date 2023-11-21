class StatJoueur:
    def __init__(
        self,
        kills,
        deaths,
        assists,
        creeps,
        total_gold,
        total_damage_dealt,
        total_damage_take,
        total_heal,
        win,
    ) -> None:
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.creeps = creeps
        self.total_gold = total_gold
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_take = total_damage_take
        self.total_heal = total_heal
        self.win = win

    def __str__(self) -> str:
        res = "Mes stats sont : \n"
        res += "\t Total kills = {}".format(self.kills)
        res += "\t Total Damage Dealt = {}".format(self.total_damage_dealt)
        res += "\t Total Deaths = {}".format(self.deaths)
        res += "\t Total Damage Take = {}".format(self.total_damage_take)
        res += "\t Total assists = {}".format(self.assists)
        res += "\t Total heal = {}".format(self.total_heal)
        return res
