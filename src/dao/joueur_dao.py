from dao.db_connection import DBConnection
from utils.singleton import Singleton

class JoueurDao(metaclass=Singleton):
    def creer(self, joueur) -> bool:
        """Creation d'un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur
        user_id : int

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
                        "INSERT INTO projet.joueur(puuid, name) VALUES "
                        "(%(puuid)s,  %(name)s)"
                        "ON CONFLICT (puuid) DO NOTHING",
                        {
                            "puuid": joueur.puuid,
                            "name": joueur.name,
                        },
                    )
                    res = True
        except Exception as e:
            print(e)
            res = False

        return res

    