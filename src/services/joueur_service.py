from dao.joueur_dao import JoueurDao
from business_object.user.joueur import Joueur


class JoueurService:
    def creer(self, joueur):
        return JoueurDao().creer(joueur)

    def find_by_name(self, name):
        return JoueurDao().find_by_name(name)
