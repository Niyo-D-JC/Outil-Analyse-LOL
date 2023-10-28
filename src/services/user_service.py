from dao.user_dao import UserDao
from business_object.user.joueur import Joueur
from business_object.user.user import User
from business_object.battle.matchjoueur import MatchJoueur
from business_object.stats.stat_joueur import StatJoueur
from dao.matchjoueur_dao import MatchJoueurDao


class UserService:
    def creer(self, user):
        return UserDao().creer(user)

    def creer_no_puuid(self, user):
        return UserDao().creer_no_puuid(user)

    def find_by_name(self, name):
        return UserDao().find_by_name(name)

    def get_stats_by_champ(Liste_Match_User):
        """Calcule les statistiques moyennes par champion à partir d'une liste de matchs d'un utilisateur.

        Cette fonction parcourt la liste de matchs d'un utilisateur, regroupe les statistiques par champion,
        et calcule les moyennes pour les statistiques telles que les kills, deaths, assists, et creeps (cs).

        Parameters
        ----------
        Liste_Match_User : List[MatchJoueur]
            Une liste d'objets MatchJoueur représentant les matchs d'un utilisateur.

        Returns
        -------
        champions_stats : dict
            Un dictionnaire contenant les statistiques moyennes par champion.
            Chaque entrée du dictionnaire a pour clé le nom du champion et
            pour valeur un sous-dictionnaire avec les clés suivantes :
                - "kills_avg" : La moyenne des kills par match.
                - "deaths_avg" : La moyenne des deaths par match.
                - "assists_avg" : La moyenne des assists par match.
                - "cs_avg" : La moyenne des creeps (cs) par match.
                - "nombre_de_matchs" : Le nombre total de matchs joués avec ce champion.
        """

        champions_stats = {}

        for Match_User in Liste_Match_User:
            champion = Match_User.champion
            stat_joueur = Match_User.stat_joueur

            # Vérifier si le champion est déjà dans le dictionnaire
            if champion not in champions_stats:
                champions_stats[champion] = {
                    "kills_avg": 0,
                    "deaths_avg": 0,
                    "assists_avg": 0,
                    "cs_avg": 0,
                    "nombre_de_matchs": 0,
                }

            # Mettre à jour les statistiques du champion
            champions_stats[champion]["kills_avg"] += stat_joueur.kills
            champions_stats[champion]["deaths_avg"] += stat_joueur.deaths
            champions_stats[champion]["assists_avg"] += stat_joueur.assists
            champions_stats[champion]["cs_avg"] += stat_joueur.creeps
            champions_stats[champion]["nombre_de_matchs"] += 1

        # Calculer les moyennes
        for champion, stats in champions_stats.items():
            nombre_de_matchs = stats["nombre_de_matchs"]
            champions_stats[champion]["kills_avg"] /= nombre_de_matchs
            champions_stats[champion]["deaths_avg"] /= nombre_de_matchs
            champions_stats[champion]["assists_avg"] /= nombre_de_matchs
            champions_stats[champion]["cs_avg"] /= nombre_de_matchs

        return champions_stats

    def get_global_WR(Liste_Match_User):
        """Calcule le taux de victoire global d'un utilisateur.

        Cette fonction prend en compte la liste des matchs d'un utilisateur, compte le nombre total de parties
        et le nombre total de victoires, puis calcule le taux de victoire global en fonction de ces deux valeurs.

        Parameters
        ----------
        Liste_Match_User : List[MatchJoueur]
            Une liste d'objets MatchJoueur représentant les matchs d'un utilisateur.

        Returns
        -------
        tuple
            Un tuple contenant deux éléments :
            - total_wins : Le nombre total de victoires de l'utilisateur.
            - total_games : Le nombre total de parties jouées par l'utilisateur.
        """

        total_games = len(Liste_Match_User)
        total_wins = 0

        for Match_User in Liste_Match_User:
            if Match_User.stat_joueur.win == True:
                total_wins += 1

        return (total_wins, total_games)

    def get_stats_perso(self, user: User):
        Liste_Match_User = MatchJoueurDao().filter_by_Joueur(user.joueur)

        total_wins, total_games = UserService().get_global_WR(Liste_Match_User)
        champions_counts = UserService().get_stats_by_champ(Liste_Match_User)


if __name__ == "__main__":
    # Exemple d'utilisation
    pass
