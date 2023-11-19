import requests
import json
import dotenv
import os
import time

from dao.user_dao import UserDao
from business_object.user.joueur import Joueur
from business_object.user.user import User
from business_object.battle.matchjoueur import MatchJoueur
from business_object.stats.stat_joueur import StatJoueur
from dao.matchjoueur_dao import MatchJoueurDao
from services.invite_service import InviteService
from api.fill_data_base import FillDataBase


class UserService(InviteService):
    def creer(self, user):
        return UserDao().creer(user)

    def creer_no_puuid(self, user):
        return UserDao().creer_no_puuid(user)

    def find_by_name(self, name):
        return UserDao().find_by_name(name)

    def delete_by_name(self, name):
        return UserDao().delete_by_name(name)

    def get_users(self):
        return UserDao().get_users()

    def update_puuid(self, puuid, name):
        return UserDao().update_puuid(puuid, name)

    def delete_match(self, match_id):
        return MatchJoueurDao().delete_match(match_id)

    def all_parties(self):
        return MatchJoueurDao().all_parties()

    def vue_partie(self, match_id):
        print("")
        pd_match = (
            MatchJoueurDao()
            .vue_partie(match_id)
            .to_string(
                index=False,
                formatters={
                    "total_damage_dealt": "{:,.0f}".format,
                    "total_damage_take": "{:,.0f}".format,
                    "total_heal": "{:,.0f}".format,
                    "total_gold": "{:,.0f}".format,
                },
            )
        )
        print(pd_match)

    def get_match_list_bypuuid(self, puuid):
        return MatchJoueurDao().get_match_list_bypuuid(puuid)

    def get_stats_by_champ(self, Liste_Match_User):
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
            champion = Match_User.champion.name
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

    def get_global_WR(self, Liste_Match_User):
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

        total_wins, total_games = self.get_global_WR(Liste_Match_User)
        champions_counts = self.get_stats_by_champ(Liste_Match_User)
        print(
            "************************** Mon Bilan Personnel ***************************"
        )
        print(f"\t Nombre de Match Total : {total_games}")
        print(f"\t Nombre de Match Gagné : {total_wins}")
        print("")
        print(
            "*********************** Mon Bilan Par Champion ***************************"
        )
        header = "{:<15} {:<12} {:<12} {:<13} {:<9} {:<16}".format(
            "Champion",
            "Kills Avg",
            "Deaths Avg",
            "Assists Avg",
            "CS Avg",
            "Nombre de Matchs",
        )
        separator = "-" * 74  # Longueur totale du tableau

        # Affichage de l'en-tête et du séparateur
        print(header)
        print(separator)

        # Affichage des données des champions
        for champion, stats in champions_counts.items():
            row = "{:<15} {:<12} {:<12} {:<13} {:<9} {:<16}".format(
                champion,
                round(stats["kills_avg"], 2),
                round(stats["deaths_avg"], 2),
                round(stats["assists_avg"], 2),
                round(stats["cs_avg"], 2),
                stats["nombre_de_matchs"],  # Ne pas arrondir le nombre de matchs
            )
            print(row)

    def update_data_of_player(self, user: User):
        """
        Permet de rajouter en BDD, les 20 dernières parties de l'utilisateur

        """

        time.sleep(2)

        # match_list_url = "/lol/match/v5/matches/by-puuid/"
        # first_game, last_game = 0, 20
        # final_list_match_url = (
        #     EUW_api_url
        #     + match_list_url
        #     + account_puuid
        #     + "/ids?start="
        #     + str(first_game)
        #     + "&"
        #     + "count="
        #     + str(last_game)
        #     + "&api_key="
        #     + os.environ["API_KEY"]
        # )
        # list_match_data = requests.get(final_list_match_url)

        time.sleep(2)

        for match_id in list_match_data.json():
            MatchJoueur_Object = FillDataBase().getJoueurMatchInfo(
                joueur=user.joueur, match_id=match_id
            )

            MatchJoueurDao().creer()


if __name__ == "__main__":
    df = UserService().vue_partie("EUW1_6648309581")
    print(df)
