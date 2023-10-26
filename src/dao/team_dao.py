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
            print(e)
            res = False

        return res

    def find_by_id(team_id):
        """trouver une Team grace à son id

        Parameters
        ----------
        id : int

        Returns
        -------
        Team : Team
            renvoie un objet Team
        """
        res = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "FROM projet.team              "
                        "WHERE id = %(team_id)s;  ",
                        {"team_id": team_id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        if res:
            team = Team(team_id=team_id, side=res["side"])

        return team
