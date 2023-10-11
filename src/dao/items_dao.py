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
                        "(%(item_id)s, %(name)s)",
                        {
                            "item_id": item.id,
                            "name": item.name
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    