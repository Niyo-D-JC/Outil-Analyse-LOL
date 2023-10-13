from dao.db_connection import DBConnection
from utils.singleton import Singleton

class MatchDao(metaclass=Singleton):
    def creer(self, match, joueur) -> bool:
        """Creation d'un item dans la base de données

        Parameters
        ----------
        match : Match
        joueur : Joueur
        
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
                        "(%(match_id)s, %(puuid)s, %(lane_id)s, %(champion_id)s, %(team_id)s, %(total_damage_deal)s, %(total_damage_take)s, %(total_heal)s, %(kda)s, %(result)s)",
                        {
                            "match_id": match.match_id,
                            "puuid": joueur.puuid,
                            "lane_id": joueur.lane.id,
                            "champion_id": joueur._champion.id,
                            "team_id": joueur._team._id,
                            "total_damage_deal": joueur.stat_joueur._total_damage_deal,
                            "total_damage_take": joueur.stat_joueur._total_damage_take,
                            "total_heal": joueur.stat_joueur._total_heal,
                            "kda": joueur.stat_joueur._kda,
                            "result": joueur.stat_joueur._result
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    