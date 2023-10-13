from dao.db_connection import DBConnection
from utils.singleton import Singleton

class ItemMatchDao(metaclass=Singleton):
    def creer(self, match_id, puuid, item_id) -> bool:
        """Creation d'un itemmacth dans la base de données

        Parameters
        ----------
        match_id, puuid, item_id

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
                        "INSERT INTO projet.match(match_id,puuid,item_id) VALUES "
                        "(%(match_id)s, %(puuid)s, %(item_id)s)",
                        {
                            "match_id": match.match_id,
                            "puuid": joueur.puuid,
                            "item_id": joueur.lane.id
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    