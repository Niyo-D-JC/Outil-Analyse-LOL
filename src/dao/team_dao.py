from dao.db_connection import DBConnection
from utils.singleton import Singleton

from business_object.battle.team import Team


class TeamDao(metaclass=Singleton):
    def creer(self, team):
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
                        "(%(team_id)s, %(side)s)",
                        {"team_id": team.team_id, "side": team.side},
                    )
                    res = True
        except Exception as e:
            res = False

        return res
