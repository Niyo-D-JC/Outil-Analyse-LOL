class Joueur:
    def __init__(self, puuid, name=None, tier = None):
        self.puuid = puuid
        self.name = name
        self.tier = tier

    def __str__(self):
        return "Joueur : " + self.name
