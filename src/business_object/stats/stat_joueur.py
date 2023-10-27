class StatJoueur:
    def __init__(
        self, kills, deaths, assists, total_damage_deal, total_damage_take, total_heal, kda, win
    ) -> None:
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_take = total_damage_take
        self.total_heal = total_heal
        self.kda = kda
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

    def kda_player(self):
        for joueur in self.joueur:
            kda = f"KDA: Kills :{self.kills}/Deaths :{self.deaths}/Assists :{self.assists}"
            #print(f"Player: {Joueur.summoner_name}, {kda}")
