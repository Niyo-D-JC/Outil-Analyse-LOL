class StatChampion:
    def __init__(self, total_damage) -> None:
        self._total_damage = total_damage
    
    def __str__(self) -> str:
        res = "Les stats du champion sont : \n"
        res += "\t Total Damage = {}".format(self._total_damage)
        return res
    
    @property
    def total_damage(self):
        return self._total_damage
    @total_damage.setter
    def total_damage(self, new_total_damage):
        self._total_damage = new_total_damage