import time
import pandas as pd
from tabulate import tabulate


from dao.user_dao import UserDao
from business_object.user.joueur import Joueur
from business_object.user.user import User
from business_object.battle.matchjoueur import MatchJoueur
from business_object.stats.stat_joueur import StatJoueur
from services.stat_match import StatMatch
from business_object.tools.lane import Lane

from dao.matchjoueur_dao import MatchJoueurDao
from services.invite_service import InviteService


class UserService(InviteService):
    def creer(self, user: User):
        """
        Crée un nouvel utilisateur dans la base de données en utilisant UserDao.

        Parameters:
        ----------
        user: User
            L'objet utilisateur à créer en BDD.

        Returns
        -------
        user_id : int
            L'identifiant en BDD de l'objet créé
        """
        return UserDao().creer(user)

    def creer_no_puuid(self, user: User):
        """
        Crée un nouvel utilisateur sans attribut puuid dans la base de données en utilisant UserDao.

        Parameters:
        ----------
        user: User
            L'objet utilisateur à créer en BDD.

        Returns
        -------
        user_id : int
            L'identifiant en BDD de l'objet créé
        """

        return UserDao().creer_no_puuid(user)

    def find_by_name(self, name: str):
        """
        Recherche un utilisateur par nom dans la base de données en utilisant UserDao.

        Parameters:
        ----------
            name: Le nom de l'utilisateur à rechercher.

        Returns:
        ----------
            User: Renvoie l'objet User associé au nom choisi
        """

        return UserDao().find_by_name(name)

    def delete_by_name(self, name: str):
        """
        Supprime un utilisateur par nom de la base de données en utilisant UserDao.

        Parameters:
        ----------
            name: Le nom de l'utilisateur à supprimer.

        Returns:
        ----------
        bool
            Renvoie True si la suppression s'est faite correctement.
        """
        return UserDao().delete_by_name(name)

    def get_users(self):
        """
        Récupère tous les utilisateurs de la base de données en utilisant UserDao.

        Returns:
        ----------
            pandas.Dataframe: Renvoie le contenu de la table User
        """
        return UserDao().get_users()

    def get_match_list_bypuuid(self, puuid: str):
        """
        Récupère la liste des matchs pour un utilisateur donné par puuid en utilisant MatchJoueurDao.

        Parameters:
        ----------
            puuid: L'identifiant unique de l'utilisateur.

        Returns:
        ----------
            pandas.Dataframe: Renvoie le contenu de la table MatchJoueur pour le puuid choisi.
        """
        return MatchJoueurDao().get_match_list_bypuuid(puuid)

    def update_puuid(self, new_puuid: str, name: str):
        """
        Met à jour l'attribut puuid d'un utilisateur dans la base de données en utilisant UserDao.

        Parameters:
        ----------
            puuid: Le nouvel identifiant unique de l'utilisateur.
            name: Le nom de l'utilisateur à mettre à jour.

        Returns:
        ----------
        bool
            Renvoie True si la mise a jour s'est faite correctement.
        """
        return UserDao().update_puuid(new_puuid, name)

    def delete_match(self, match_id: str):
        """
        Supprime un match par son identifiant de la base de données en utilisant MatchJoueurDao.

        Parameters:
        ----------
            match_id: L'identifiant du match à supprimer.

        Returns:
        ----------
        bool
            Renvoie True si la suppression s'est faite correctement.
        """
        return MatchJoueurDao().delete_match(match_id)

    def all_parties(self):
        """
        Récupère toutes les parties de la base de données en utilisant MatchJoueurDao.

        Returns:
        ----------
        pandas.Dataframe
            Renvoie le contenu de la table MatchJoueur.
        """
        return MatchJoueurDao().all_parties()

    def vue_partie(self, match_id: str):
        """Affiche dans la console le résumé d'un partie

        Cette fonction affiche l'équipe gagnante et la performance de tous les joueurs de la partie.
        Elle affiche également les MVP de la partie selon 5 critères différents

        Parameters
        ----------
        match_id : str
            Identifiant d'une partie de League of Legends

        """

        print("")
        pd_match = MatchJoueurDao().vue_partie(match_id)

        try:
            first_row = pd_match.iloc[0]
            blue_win = first_row["side"] == "Blue" and first_row["win_lose"] == "Win"

            pd_match_blue = pd_match.iloc[:5].set_index(["side", "win_lose"])
            pd_match_red = pd_match.iloc[5:].set_index(["side", "win_lose"])

            kda_blue_team = (
                "=" * 65
                + " {"
                + " " * 5
                + StatMatch().kda_team(pd_match_blue)
                + " " * 5
                + "} "
                + "=" * 65
            )
            kda_red_team = (
                "=" * 65
                + " {"
                + " " * 5
                + StatMatch().kda_team(pd_match_red)
                + " " * 5
                + "} "
                + "=" * 65
            )

            ################ Blue  Team ################
            if blue_win:
                print("=" * 65, "{ EQUIPE BLEUE : VICTOIRE }", "=" * 65)
            else:
                print("=" * 65, "{ EQUIPE BLEUE : DEFAITE }", "=" * 65)

            print(kda_blue_team)

            print(
                tabulate(
                    pd_match_blue,
                    headers="keys",
                    tablefmt="double_outline",
                    showindex=False,
                )
            )

            ################ Red Team ################
            print("")

            if blue_win:
                print("=" * 65, "{ EQUIPE ROUGE : DEFAITE }", "=" * 65)
            else:
                print("=" * 65, "{ EQUIPE ROUGE : VICTOIRE }", "=" * 65)

            print(kda_red_team)

            print(
                tabulate(
                    pd_match_red,
                    headers="keys",
                    tablefmt="double_outline",
                    showindex=False,
                )
            )

            print("")
            print("=" * 15, "{ MVP DU MATCH }", "=" * 15)
            print(
                f" 🔪 Assassin : {StatMatch().mvp_by_category(pd_match, 'kills')} (Le plus de kills)"
            )
            print(
                f" 💰 Avare : {StatMatch().mvp_by_category(pd_match, 'golds')} (Le plus de golds accumulés)"
            )

            print(
                f" ⚔️ Combattant : {StatMatch().mvp_by_category(pd_match, 'dégats_infligés')} (Le plus de dégats infligés)"
            )
            print(
                f" 🛡️ Montagne : {StatMatch().mvp_by_category(pd_match, 'dégats_subis')} (Le plus de dégats subis)"
            )
            print(
                f" ❤️ Médecin :{StatMatch().mvp_by_category(pd_match, 'soins_totaux')} (Le plus de points de vie soignés)"
            )
            print("=" * 45)
            print("")
        except:
            print("Erreur Match inexistant")

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

    def get_stats_by_lane(self, Liste_Match_User):
        """Calcule les statistiques moyennes par champion et par lane à partir d'une liste de matchs d'un utilisateur.

        Cette fonction parcourt la liste de matchs d'un utilisateur, regroupe les statistiques par champion et par lane,
        et calcule les moyennes pour les statistiques telles que les kills, deaths, assists, et creeps (cs).

        Parameters
        ----------
        Liste_Match_User : List[MatchJoueur]
            Une liste d'objets MatchJoueur représentant les matchs d'un utilisateur.

        Returns
        -------
        lane_stats : Dict[str, Dict[str, Dict[str, Union[float, int]]]]
            Un dictionnaire contenant les statistiques moyennes par champion et par lane.
            Chaque entrée du dictionnaire a pour clé le nom de la lane, et pour valeur un dictionnaire
            trié par le nombre de matchs dans l'ordre décroissant, contenant les statistiques par champion.
        """

        lane_stats = {
            "TOP": {},
            "JUNGLE": {},
            "MIDDLE": {},
            "BOTTOM": {},
            "SUPPORT": {},
            "NONE": {},
        }

        for Match_User in Liste_Match_User:
            champion = Match_User.champion.name
            stat_joueur = Match_User.stat_joueur
            lane = Match_User.lane.name

            # Vérifier si le champion est déjà dans le dictionnaire de la lane
            if champion not in lane_stats[lane]:
                lane_stats[lane][champion] = {
                    "kills_avg": 0,
                    "deaths_avg": 0,
                    "assists_avg": 0,
                    "cs_avg": 0,
                    "winrate": 0,
                    "nombre_de_matchs": 0,
                }

            # Mettre à jour les statistiques du champion dans la lane
            lane_stats[lane][champion]["kills_avg"] += stat_joueur.kills
            lane_stats[lane][champion]["deaths_avg"] += stat_joueur.deaths
            lane_stats[lane][champion]["assists_avg"] += stat_joueur.assists
            lane_stats[lane][champion]["cs_avg"] += stat_joueur.creeps
            lane_stats[lane][champion]["nombre_de_matchs"] += 1
            # Ajouter la victoire si le joueur a gagné
            if stat_joueur.win:
                lane_stats[lane][champion]["winrate"] += 1

        # Trier les champions dans chaque lane par le nombre de matchs dans l'ordre décroissant
        for lane, champions in lane_stats.items():
            lane_stats[lane] = dict(
                sorted(
                    champions.items(),
                    key=lambda x: x[1]["nombre_de_matchs"],
                    reverse=True,
                )
            )

        # Calculer les moyennes pour chaque lane
        for lane, champions in lane_stats.items():
            for champion, stats in champions.items():
                nombre_de_matchs = stats["nombre_de_matchs"]
                lane_stats[lane][champion]["kills_avg"] /= nombre_de_matchs
                lane_stats[lane][champion]["deaths_avg"] /= nombre_de_matchs
                lane_stats[lane][champion]["assists_avg"] /= nombre_de_matchs
                lane_stats[lane][champion]["cs_avg"] /= nombre_de_matchs
                lane_stats[lane][champion]["winrate"] /= nombre_de_matchs

        return lane_stats

    def get_stats_perso(self, user: User):
        """Affiche dans la console le bilan de performance d'un utilisateur

        La bilan propose le taux de victoire général sur l'ensemble des parties disponibles
        ainsi que le statistiques par champions et par lane.

        Parameters
        ----------
        user : User
            Un objet de la classe User. Il s'agit de l'utilisateur dont on veut obtenir les statistiques
        """

        Liste_Match_User = MatchJoueurDao().filter_by_Joueur(user.joueur)
        total_wins, total_games = self.get_global_WR(Liste_Match_User)
        lane_stats = self.get_stats_by_lane(Liste_Match_User)

        print("")
        print(
            "************************** Mon Bilan Personnel ***************************"
        )
        print(f"\t Nombre de Match Total : {total_games}")
        print(f"\t Nombre de Match Gagné : {total_wins}")
        print(f"\t Taux de victoire : {round(total_wins * 100 / total_games, 1)}%")
        print("")
        print(
            "*********************** Mon Bilan Par Lane et Par Champion ***************************"
        )

        separator = "-" * 98  # Longueur totale du tableau
        header = "{:<15} {:<12} {:<12} {:<13} {:<9} {:<15} {:<16}".format(
            "Champion",
            "Kills Avg",
            "Deaths Avg",
            "Assists Avg",
            "CS Avg",
            "Winrate",
            "Nombre de Matchs",
        )
        # Affichage des données des champions et par lane
        for lane, champions_stats in lane_stats.items():
            if champions_stats != {}:
                n_games_lane = 0
                wr_lane = 0
                for stats in champions_stats.values():
                    wr_lane += stats["winrate"] * stats["nombre_de_matchs"]
                    n_games_lane += stats["nombre_de_matchs"]

                wr_lane = round(wr_lane * 100 / n_games_lane, 1)

                print("\n" + separator)
                print(f"\t\t{lane} STATS (Taux de victoire : {wr_lane}%)")

                # Affichage de l'en-tête et du séparateur
                print(header)
                print(separator)

                # Affichage des données des champions dans la lane
                for champion, stats in champions_stats.items():
                    row = "{:<15} {:<12} {:<12} {:<13} {:<9} {:<16} {:<16}".format(
                        champion,
                        round(stats["kills_avg"], 2),
                        round(stats["deaths_avg"], 2),
                        round(stats["assists_avg"], 2),
                        round(stats["cs_avg"], 2),
                        round(stats["winrate"] * 100, 3),
                        stats["nombre_de_matchs"],
                    )
                    print(row)


if __name__ == "__main__":
    df = UserService().vue_partie("EUW1_6681929582")
    print(df)
