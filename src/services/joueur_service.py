from dao.joueur_dao import JoueurDao
from business_object.user.joueur import Joueur


class JoueurService:
    def find_by_name(self, name):
        return JoueurDao().find_by_name(name)

    def update_data_of_player(self, joueur: Joueur):
        # tant que la requete sur match est non nulle
        # on remplit la base de données avec de requete sur les matchs
        pass
