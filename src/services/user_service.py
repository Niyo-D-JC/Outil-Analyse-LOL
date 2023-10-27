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

    def get_stats_perso(self, user: User):
        def get_global_WR(Liste_Match_User):
            total_games = len(Liste_Match_User)
            total_wins = 0

            for Match_User in Liste_Match_User:
                if Match_User.stat_joueur.win == True:
                    total_wins += 1

            return (total_wins, total_games)

        def get_most_played_champs(Liste_Match_User):
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

        Liste_Match_User = MatchJoueurDao().filter_by_Joueur(user.joueur)

        total_wins, total_games = get_global_WR(Liste_Match_User)
        champions_counts = get_most_played_champs(get_most_played_champs)
        pass
        ## il faut dire le WR général
        ## les champions les plus joués avec leur KDA associé et leur WR associé


if __name__ == "__main__":
    # Exemple d'utilisation
    def calculer_moyennes_par_champion(liste_matchs):
        champions_stats = {}

        for match in liste_matchs:
            champion = match.champion
            stat_joueur = match.stat_joueur

            # Vérifier si le champion est déjà dans le dictionnaire
            if champion not in champions_stats:
                champions_stats[champion] = {
                    "kda_total": 0,
                    "cs_total": 0,
                    "nombre_de_matchs": 0,
                }

            # Mettre à jour les statistiques du champion
            champions_stats[champion]["kda_total"] += stat_joueur.kda
            # Ajouter d'autres statistiques si nécessaire
            champions_stats[champion][
                "cs_total"
            ] += (
                stat_joueur.total_damage_deal
            )  # Utiliser le champ approprié pour les CS
            champions_stats[champion]["nombre_de_matchs"] += 1

        # Calculer les moyennes
        for champion, stats in champions_stats.items():
            kda_moyen = (
                stats["kda_total"] / stats["nombre_de_matchs"]
                if stats["nombre_de_matchs"] > 0
                else 0
            )
            cs_moyen = (
                stats["cs_total"] / stats["nombre_de_matchs"]
                if stats["nombre_de_matchs"] > 0
                else 0
            )

            champions_stats[champion]["kda_moyen"] = kda_moyen
            champions_stats[champion]["cs_moyen"] = cs_moyen

        return champions_stats

    # Exemple d'utilisation
    liste_matchs = [
        MatchJoueur(
            1,
            "Joueur1",
            "Champion1",
            ["Item1", "Item2"],
            "Top",
            "Team1",
            StatJoueur(5, 2, 3, 10000, 2000, 500, True),
        ),
        MatchJoueur(
            1,
            "Joueur2",
            "Champion2",
            ["Item3", "Item4"],
            "Mid",
            "Team2",
            StatJoueur(3, 1, 2, 8000, 1500, 400, False),
        ),
        MatchJoueur(
            2,
            "Joueur1",
            "Champion1",
            ["Item1", "Item2"],
            "Top",
            "Team1",
            StatJoueur(8, 3, 5, 12000, 2500, 600, True),
        ),
        # ... Ajoutez d'autres matchs selon vos besoins
    ]

    resultat = calculer_moyennes_par_champion(liste_matchs)
    print(resultat)
