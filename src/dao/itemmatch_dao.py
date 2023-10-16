from dao.db_connection import DBConnection
from utils.singleton import Singleton

class ItemMatchDao(metaclass=Singleton):
    def creer(self, match_id, puuid, item_id) -> bool:
        """Creation d'un itemmacth dans la base de données

        Parameters
        ----------
        match_id : string, 
        puuid : string, 
        item_id : int

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
                        "INSERT INTO projet.itemmatch(match_id,puuid,item_id) VALUES "
                        "(%(match_id)s, %(puuid)s, %(item_id)s) ON CONFLICT (match_id, puuid, item_id) DO NOTHING",
                        {
                            "match_id": match_id,
                            "puuid": puuid,
                            "item_id": item_id
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False
        return res

    