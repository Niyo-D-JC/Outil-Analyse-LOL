from .joueur import Joueur
from .invite import Invite

class User(Invite):
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._joueur : Joueur 
    
    def __str__(self):
        return ("Joueur : "+self._name)

    def global_stat_perso(self):
        pass

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, new_password):
        self._password = new_password