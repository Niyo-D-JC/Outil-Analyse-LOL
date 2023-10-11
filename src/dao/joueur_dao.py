from dao.db_connection import DBConnection
from utils.singleton import Singleton

class JoueurDao(metaclass=Singleton):
    def creer(self, joueur, user_id) -> bool:
        """Creation d'un joueur dans la base de données

        Parameters
        ----------
        joueur : joueur

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
                        "INSERT INTO projet.joueur(puuid, user_id, name, rang) VALUES "
                        "(%(puuid)s, %(user_id)s, %(name)s, %(rang)s)",
                        {
                            "puuid": joueur.puuid,
                            "user_id": user_id,
                            "name": joueur.name,
                            "rang": joueur._rang
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            joueur.puuid = res["puuid"]
            created = True

        return created

    