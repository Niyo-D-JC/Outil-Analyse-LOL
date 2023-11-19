from dao.joueur_dao import JoueurDao
from business_object.user.joueur import Joueur
from api.fill_data_base import FillDataBase


class JoueurService:
    def creer(self, joueur):
        JoueurDao().creer(joueur=joueur)

    def find_by_name(self, name):
        return JoueurDao().find_by_name(name)

    def create_joueur_object(self, name):
        try:
            puuid = FillDataBase().get_puuid(name)
            tier = FillDataBase().get_tier(puuid)

            joueur_object = Joueur(puuid, name, tier)
            return joueur_object

        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    moi = JoueurService().create_joueur_object("Fan2Chat")
