from dao.db_connection import DBConnection
from dao.joueur_dao import JoueurDao
from utils.singleton import Singleton
from business_object.battle.match import Match


class MatchDao(metaclass=Singleton):
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
                        "INSERT INTO projet.match(match_id,puuid,lane_id,champion_id,team_id,total_damage_deal,total_damage_take,total_heal,kda,result) VALUES "
                        "(%(match_id)s, %(puuid)s, %(lane_id)s, %(champion_id)s, %(team_id)s, %(total_damage_deal)s, %(total_damage_take)s, %(total_heal)s, %(kda)s, %(result)s) ON CONFLICT (match_id, puuid) DO NOTHING",
                        {
                            "match_id": match.match_id,
                            "puuid": match.joueur.puuid,
                            "lane_id": match.lane.tools_id,
                            "champion_id": match.champion.tools_id,
                            "team_id": match.team.team_id,
                            "total_damage_deal": match.stat_joueur.total_damage_deal,
                            "total_damage_take": match.stat_joueur.total_damage_take,
                            "total_heal": match.stat_joueur.total_heal,
                            "kda": match.stat_joueur.kda,
                            "result": match.stat_joueur.result,
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
        return res

    def filter_by_Joueur(self, joueur) -> bool:
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * " "FROM projet.match  " "WHERE puuid = %(puuid)s ",
                        {"puuid": joueur.puuid},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            print(e)
            res = False

        if res:
            Player_Matches = []


            for game in res:  # game est un dictionnaire

                joueur = JoueurDao().find_by_puuid(game["puuid"])


                Match_Object = Match(

                    match_id=game["match"],
                    joueur=joueur,
                    champion=,
                    items=
                    lane=,
                    team=,
                    stat_joueur=,
                )


                Player_Matches.append(Match_Object)


        return Player_Matches
