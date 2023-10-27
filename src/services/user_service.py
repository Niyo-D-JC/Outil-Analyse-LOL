from dao.user_dao import UserDao
from business_object.user.joueur import Joueur
from business_object.user.user import User

from dao.matchjoueur_dao import MatchJoueurDao


class UserService:
    def creer(self, user):
        return UserDao().creer(user)

    def creer_no_puuid(self, user):
        return UserDao().creer_no_puuid(user)

    def find_by_name(self, name):
        return UserDao().find_by_name(name)

    def get_stats_perso(self, user: User):
        pass
        #Liste_Match_User = MatchDao().filter_by_Joueur(User.joueur)
        #for Match_User in Liste_Match_User : 





            
