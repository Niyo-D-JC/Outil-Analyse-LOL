from dao.db_connection import DBConnection
from utils.singleton import Singleton

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
                        "(%(champion_id)s, %(name)s)",
                        {
                            "champion_id": champion.id,
                            "name": champion.name
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    