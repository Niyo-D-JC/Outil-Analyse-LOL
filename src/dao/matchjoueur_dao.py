from dao.db_connection import DBConnection
from dao.joueur_dao import JoueurDao
from dao.champion_dao import ChampionDao
from dao.items_dao import ItemsDao
from dao.itemmatch_dao import ItemMatchDao
from dao.lane_dao import LaneDao
from dao.team_dao import TeamDao


from utils.singleton import Singleton
from business_object.battle.matchjoueur import MatchJoueur
from business_object.stats.stat_joueur import StatJoueur
from business_object.tools.champion import Champion


class MatchJoueurDao(metaclass=Singleton):
    def creer(self, match) -> bool:
        """Creation d'un item dans la base de données

        Parameters
        ----------
        match : Match

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.matchjoueur(match_id,puuid,lane_id,champion_id,team_id,total_damage_dealt,total_damage_take,total_heal,kills,deaths,assists,creeps, total_gold, win) VALUES "
                        "(%(match_id)s, %(puuid)s, %(lane_id)s, %(champion_id)s, %(team_id)s, %(total_damage_dealt)s, %(total_damage_take)s, %(total_heal)s,  %(kills)s, %(deaths)s, %(assists)s, %(creeps)s,  %(total_gold)s, %(win)s)",
                        {
                            "match_id": match.match_id,
                            "puuid": match.joueur.puuid,
                            "lane_id": match.lane.tools_id,
                            "champion_id": match.champion.tools_id,
                            "team_id": match.team.team_id,
                            "total_damage_dealt": match.stat_joueur.total_damage_dealt,
                            "total_damage_take": match.stat_joueur.total_damage_take,
                            "total_heal": match.stat_joueur.total_heal,
                            "kills": match.stat_joueur.kills,
                            "deaths": match.stat_joueur.deaths,
                            "assists": match.stat_joueur.assists,
                            "creeps" : match.stat_joueur.creeps,
                            "total_gold": match.stat_joueur.total_gold,
                            "win": match.stat_joueur.win,
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
        return res

    def get_match_list_bypuuid(self, puuid) : 
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "
                        " FROM projet.matchjoueur "
                        " WHERE puuid = %(puuid)s ; ",
                        {"puuid": puuid },
                    )
                    res = cursor.fetchall()

        except Exception as e:
            print(e)

        if res:
            import pandas as pd
            return pd.DataFrame(res)

    def vue_partie(self, match_id) : 
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT j.name AS Joueur, c.name AS champion_name, "
                        " mj.total_damage_dealt, mj.total_damage_take, "
                        " mj.total_heal, mj.kills, mj.deaths, mj.assists, mj.creeps, "
                        " mj.total_gold, mj.win "
                        " FROM projet.matchjoueur mj "
                        " JOIN projet.champion c ON mj.champion_id = c.champion_id "
                        " JOIN projet.joueur j ON mj.puuid = j.puuid "
                        " WHERE mj.match_id = %(match_id)s ; ",
                        {"match_id": match_id },
                    )
                    res = cursor.fetchall()

        except Exception as e:
            print(e)

        if res:
            import pandas as pd
            return pd.DataFrame(res)


    def all_parties(self) : 
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * " 
                        "FROM projet.matchjoueur  "
                    )
                    res = cursor.fetchall()

        except Exception as e:
            print(e)

        if res:
            import pandas as pd
            return pd.DataFrame(res)

    def delete_match(self, match_id) : 
        deleted = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " DELETE FROM projet.itemmatch "
                        " WHERE match_id = %(match_id)s;",
                        {
                            "match_id": match_id,
                        },
                    )
                    cursor.execute(
                        " DELETE FROM projet.matchjoueur"
                        " WHERE match_id = %(match_id)s;",
                        {
                            "match_id": match_id,
                        },
                    )
                    deleted = True
        except Exception as e:
            print(e)
            deleted = False
            
        return deleted

    def get_all_match(self):
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * " "FROM projet.matchjoueur  ",
                        {"puuid": joueur.puuid},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            print(e)
            res = False

        if res:
            Player_Matches = []

            for game in res:  # game est un dictionnaire
                joueur = JoueurDao().find_by_puuid(puuid=game["puuid"])
                champion = ChampionDao().find_by_id(id=game["champion_id"])
                list_items = ItemMatchDao().find_all_by_match_puuid(
                    match_id=game["match_id"]
                )
                lane = LaneDao().find_by_id(id=game["lane_id"])
                team = TeamDao().find_by_id(team_id=game["team_id"])
                stat_joueur = StatJoueur(
                    total_damage_dealt=game["total_damage_deal"],
                    total_damage_take=game["total_damage_take"],
                    total_heal=game["total_heal"],
                    kills=game["kills"],
                    deaths=game["deaths"],
                    assists=game["assists"],
                    win=game["win"],
                )

                Match_Object = MatchJoueur(
                    match_id=game["match_id"],
                    joueur=joueur,
                    champion=champion,
                    items=list_items,
                    lane=lane,
                    team=team,
                    stat_joueur=stat_joueur,
                )

                Player_Matches.append(Match_Object)

        return Player_Matches

    def filter_by_Joueur(self, joueur) -> bool:
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT mj.match_id, mj.puuid, c.name AS champion_name, "
                        " mj.lane_id, mj.team_id, mj.total_damage_dealt, mj.total_damage_take, "
                        " mj.total_heal, mj.kills, mj.deaths, mj.assists, mj.creeps, "
                        " mj.total_gold, mj.win "
                        " FROM projet.matchjoueur mj "
                        " JOIN projet.champion c ON mj.champion_id = c.champion_id "
                        " WHERE mj.puuid = %(puuid)s ; ",
                        {"puuid": joueur.puuid},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            print(e)
            res = False

        if res:
            Player_Matches = []

            for game in res:  # game est un dictionnaire
                champion = Champion(0,game["champion_name"])
                stat_joueur = StatJoueur(
                    total_damage_dealt=game["total_damage_dealt"],
                    total_damage_take=game["total_damage_take"],
                    total_heal=game["total_heal"],
                    kills=game["kills"],
                    deaths=game["deaths"],
                    assists=game["assists"],
                    creeps=game["creeps"],
                    total_gold=game["total_gold"],
                    win=game["win"],
                )

                Match_Object = MatchJoueur(
                    match_id=game["match_id"],
                    joueur=None,
                    champion=champion,
                    items=None,
                    lane=None,
                    team=None,
                    stat_joueur=stat_joueur,
                )

                Player_Matches.append(Match_Object)

        return Player_Matches
