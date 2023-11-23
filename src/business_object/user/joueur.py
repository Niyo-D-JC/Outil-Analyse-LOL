class Joueur:
    def __init__(self, puuid:str, name:str=None,tier:str=None):
        self.puuid = puuid
        self.name = name
        self.tier = tier

    def __str__(self):
        return f"Joueur : {self.name} ({self.puuid})\nrank : {self.tier}"
