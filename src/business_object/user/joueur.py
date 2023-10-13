
class Joueur:
    def __init__(self, puuid, name):
        self._puuid = puuid
        self._name = name
        self._rang = None
        self._champion = None
        self._items = None
        self.stat_joueur = None
        self.lane = None
    
    def __str__(self):
        return ("Joueur : "+self._name)
    
    @property
    def puuid(self):
        return self._puuid
    @puuid.setter
    def puuid(self, new_puuid):
        self._puuid = new_puuid

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
