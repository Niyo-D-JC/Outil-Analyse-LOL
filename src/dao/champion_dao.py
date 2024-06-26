from dao.db_connection import DBConnection
from utils.singleton import Singleton
from business_object.tools.champion import Champion


class ChampionDao(metaclass=Singleton):
    def creer(self, champion) -> bool:
        """Creation d'un champion dans la base de données

        Parameters
        ----------
        champion : Champion

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
                        "INSERT INTO projet.champion(champion_id,name) VALUES "
                        "(%(champion_id)s, %(name)s) ",
                        {"champion_id": champion.tools_id, "name": champion.name},
                    )
                    res = True
        except Exception as e:
            # print(e)
            res = False
        return res

    def find_by_id(self, champion_id):
        """trouver un Champion grace à son id

        Parameters
        ----------
        id : int

        Returns
        -------
        champion : Champion
            renvoie un objet Champion
        """
        res = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        " FROM projet.champion               "
                        " WHERE champion_id = %(champion_id)s;  ",
                        {"champion_id": champion_id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            # print(e)
            pass

        if res:
            champion = Champion(champion_id=id, name=res["name"])
            return champion

    def get_all_order(self):
        res = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT C.name AS champion_name, "
                        " COUNT(MJ.champion_id) AS usage_frequency,"
                        " (COUNT(CASE WHEN MJ.win = TRUE THEN 1 END)::FLOAT / COUNT(*)) * 100 AS win_rate "
                        "FROM projet.champion AS C  "
                        "LEFT JOIN projet.matchjoueur AS MJ ON C.champion_id = MJ.champion_id "
                        "GROUP BY C.name ;"
                    )
                    res = cursor.fetchall()
        except Exception as e:
            # print(e)
            pass

        if res:
            return res
