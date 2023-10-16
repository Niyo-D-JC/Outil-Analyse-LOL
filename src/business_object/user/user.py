from .joueur import Joueur

class User:
    def __init__(self, name, password, role = "User", joueur = None):
        self.name = name
        self.password = password
        self.role = role 
        self.joueur = joueur

    def __str__(self):
        return ("Joueur : " + self._name)

    def global_stat_perso(self):
        pass
