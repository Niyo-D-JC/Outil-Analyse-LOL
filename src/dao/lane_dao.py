from dao.db_connection import DBConnection
from utils.singleton import Singleton
from business_object.tools.lane import Lane


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
                        {"lane_id": lane.tools_id, "name": lane.name},
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False

        return res

    def find_by_id(self, lane_id):
        """trouver une lane grace à son id

        Parameters
        ----------
        id : int

        Returns
        -------
        lane : lane
            renvoie un objet lane
        """
        res = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                 "
                        " FROM projet.lane         "
                        " WHERE id = %(lane_id)s;  ",
                        {"id": lane_id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        if res:
            lane = Lane(lane_id=lane_id, name=res["name"])

        return lane
