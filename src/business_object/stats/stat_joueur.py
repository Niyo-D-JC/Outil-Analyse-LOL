
class StatJoeur:
    def __init__(self, total_damage_deal, total_damage_take, total_heal, 
                 kda, result) -> None:
        self.total_kills= total_kills
        self.total_deaths = total_deaths
        self.total_assists = total_assists
        self.total_heal = total_heal
        self.kda = kda
        self.total_dammage_dealt = total_dammage_dealt
        self.total_dammage_take = total_damage_take
        self.result = result

    def __str__(self) -> str:
        res = "Mes stats sont : \n"
        res += "\t Total kills = {}".format(self.total_kills)
        res += "\t Total Damage Dealt = {}".format(self.total_damage_dealt)
        res += "\t Total Deaths = {}".format(self.total_deaths)
        res += "\t Total Damage Take = {}".format(self.total_damage_take)
        res += "\t Total assists = {}".format(self.total_assists)
        res += "\t Total heal = {}".format(self.total_heal)
        return res
    
    def kda_player(self):
        for joueur in self.joueur:
            kda = f'KDA: Kills :{self.total_kills}/Deaths :{self.total_deaths}/Assists :{self.total_assists}'
            print(f"Player: {Joueur.summoner_name}, {kda}")
    
    
   
    