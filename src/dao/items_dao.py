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
                        "(%(item_id)s, %(name)s) "
                        "ON CONFLICT (item_id) DO NOTHING",
                        {"item_id": item.tools_id, "name": item.name},
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
        return res

    def find_by_id(self, id):
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
                        "SELECT *                           "
                        "FROM projet.lane              "
                        "WHERE id = %(id)s;  ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        if res:
            item = Item(id=id, name=res["name"])

        return item
