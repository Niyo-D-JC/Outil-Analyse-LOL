from business_object.tools.abs_tools import AbsTools


class Champion(AbsTools):
    def __init__(self, id, name) -> None:
        super().__init__(self,id,name)
        self._stat_champion = None

    def __str__(self) -> str:
        return("Champion : " + self._name)
    
    @property
    def stat_champion(self):
        return self._stat_champion
    @id.setter
    def stat_champion(self, new_stat_champion):
        self._stat_champion = new_stat_champion