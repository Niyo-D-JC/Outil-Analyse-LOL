from dao.db_connection import DBConnection
from utils.singleton import Singleton
from business_object.tools.items import Item


class ItemsDao(metaclass=Singleton):
    def creer(self, item) -> bool:
        """Creation d'un item dans la base de données

        Parameters
        ----------
        item : Items

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
                        "INSERT INTO projet.item(item_id,name) VALUES "
                        "(%(item_id)s, %(name)s) ",
                        {"item_id": item.tools_id, "name": item.name},
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
        return res

    def find_by_id(self, id):
        """trouver une item grace à son id

        Parameters
        ----------
        id : int

        Returns
        -------
        item : item
            renvoie un objet item
        """
        res = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "FROM projet.item              "
                        "WHERE id = %(id)s;  ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        if res:
            item = Item(id=id, name=res["name"])

        return item

    def get_all_order(self) :
        res = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT I.name AS item_name, "
                        " COUNT(IM.item_id) AS usage_frequency, "
                        " (COUNT(CASE WHEN MJ.win = TRUE THEN 1 END)::FLOAT / COUNT(*)) AS win_rate "
                        " FROM projet.item AS I "
                        " LEFT JOIN projet.itemmatch AS IM ON I.item_id = IM.item_id "
                        " LEFT JOIN projet.matchjoueur AS MJ ON IM.match_id = MJ.match_id AND IM.puuid = MJ.puuid "
                        " GROUP BY I.name ;"
                    )
                    res = cursor.fetchall()
        except Exception as e:
            print(e)

        if res:
            return res