
class StatJoeur:
    def __init__(self, total_damage_dealt, total_damage_take, total_heal, 
                 lane, result) -> None:
        self._total_damage_dealt = total_damage_dealt
        self._total_damage_take = total_damage_take
        self._total_heal = total_heal
        self._lane = lane
        self._result = result

    def __str__(self) -> str:
        res = "Mes stats sont : \n"
        res += "\t Total Damage Dealt = {}".format(self._total_damage_dealt)
        res += "\t Total Damage Take = {}".format(self._total_damage_take)
        return res
    
    @property
    def total_damage_dealt(self):
        return self._total_damage_dealt
    @total_damage_dealt.setter
    def total_damage_dealt(self, new_total_damage_dealt):
        self._total_damage_dealt = new_total_damage_dealt

    @property
    def total_damage_take(self):
        return self._total_damage_take
    @total_damage_take.setter
    def total_damage_take(self, new_total_damage_take):
        self._total_damage_take = new_total_damage_take

    @property
    def total_heal(self):
        return self._total_heal
    @total_heal.setter
    def total_heal(self, new_total_heal):
        self._total_heal = new_total_heal