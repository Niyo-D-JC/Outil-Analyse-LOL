
class StatJoeur:
    def __init__(self, total_damage_deal, total_damage_take, total_heal, 
                 kda, result) -> None:
        self.total_damage_deal = total_damage_deal
        self.total_damage_take = total_damage_take
        self.total_heal = total_heal
        self.kda = kda
        self.result = result

    def __str__(self) -> str:
        res = "Mes stats sont : \n"
        res += "\t Total Damage Dealt = {}".format(self.total_damage_dealt)
        res += "\t Total Damage Take = {}".format(self.total_damage_take)
        return res
    