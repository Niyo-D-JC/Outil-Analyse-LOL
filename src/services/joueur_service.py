from dao.joueur_dao import JoueurDao
class JoueurService:
    def find_by_name(self, name):
        return JoueurDao().find_by_name(name)