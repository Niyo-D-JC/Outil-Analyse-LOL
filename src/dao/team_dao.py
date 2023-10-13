from dao.db_connection import DBConnection
from utils.singleton import Singleton

class TeamDao(metaclass=Singleton):
    def creer(self, champion) -> bool:
        """Creation d'une equipe dans la base de données

        Parameters
        ----------
        team : Team

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
                        "INSERT INTO projet.team(team_id, side) VALUES "
                        "(%(team_id)s, %(side)s)",
                        {
                            "team_id": team._id,
                            "side": team._name
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    