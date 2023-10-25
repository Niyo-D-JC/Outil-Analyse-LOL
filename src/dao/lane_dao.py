from dao.db_connection import DBConnection
from utils.singleton import Singleton

class LaneDao(metaclass=Singleton):
    def creer(self, champion) -> bool:
        """Creation d'un champion dans la base de données

        Parameters
        ----------
        lane : Lane

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
                        "INSERT INTO projet.lane(lane_id,name) VALUES "
                        "(%(lane_id)s, %(name)s)",
                        {
                            "lane_id": lane.tools_id,
                            "name": lane.name
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
      
        return res

    