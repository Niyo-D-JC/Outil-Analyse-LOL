from dao.db_connection import DBConnection
from utils.singleton import Singleton

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
                        {
                            "item_id": item.tools_id,
                            "name": item.name
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
        return res

    