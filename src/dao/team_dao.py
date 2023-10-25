from dao.db_connection import DBConnection
from utils.singleton import Singleton

class TeamDao(metaclass=Singleton):
    def creer(self, team) :
        """Creation d'une equipe dans la base de données

        Parameters
        ----------
        team : Team

        Returns
        -------
        res : Bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.team(team_id, side) VALUES "
                        "(%(team_id)s, %(side)s) ON CONFLICT (team_id) DO NOTHING",
                        {
                            "team_id" : team.team_id,
                            "side": team.side
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res =  False
       
        return res

    