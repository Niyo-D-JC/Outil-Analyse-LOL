
class Joueur:
    def __init__(self, puuid, name = None):
        self.puuid = puuid
        self.name = name
    
    def __str__(self):
        return ("Joueur : "+self._name)
    
   
