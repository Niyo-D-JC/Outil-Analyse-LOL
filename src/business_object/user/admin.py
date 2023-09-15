from business_object.user.joueur import Joueur


class Admin(Joueur):
    def __init__(self, puuid, name):
        super().__init__(puuid, name)