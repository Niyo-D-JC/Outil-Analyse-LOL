from dao.db_connection import DBConnection
from utils.singleton import Singleton

from business_object.tools.items import Item
from dao.items_dao import ItemsDao


class ItemMatchDao(metaclass=Singleton):
    def creer(self, match_id, puuid, item_id, item_position) -> bool:
        """Creation d'un itemmacth dans la base de données

        Parameters
        ----------
        match_id : string,
        puuid : string,
        item_id : int
        item_position : int

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
                        "INSERT INTO projet.itemmatch(match_id,puuid,item_id, item_position) VALUES "
                        "(%(match_id)s, %(puuid)s, %(item_id)s, %(item_position)s)",
                        {
                            "match_id": match_id,
                            "puuid": puuid,
                            "item_id": item_id,
                            "item_position": item_position,
                        },
                    )
                    res = True
        except Exception as e:
            # print(e)
            res = False
        return res

    def find_all_by_match_puuid(self, match_id: int, puuid: int):
        """trouver un utilisateur grace à son nom

        Parameters
        ----------
        game_id : int
        puuid : int

        Returns
        -------
        Item : Item
            renvoie l'utilisateur que l'on cherche par son nom
        """
        res = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                           "
                        " FROM projet.itemmatch               "
                        " WHERE match_id = %(match_id)s AND puuid= %(puuid)s;  ",
                        {
                            "match_id": match_id,
                            "puuid": puuid,
                        },
                    )
                    res = cursor.fetchall()
        except Exception as e:
            pass

        if res:
            List_items = []

            for item in res:
                item_object = ItemsDao().find_by_id(id=res["item_id"])
                # type(item_object) == Item

                List_items.append(item_object)

        return List_items
