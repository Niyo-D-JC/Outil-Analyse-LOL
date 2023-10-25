from dao.db_connection import DBConnection
from utils.singleton import Singleton
from business_object.user.joueur import Joueur


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

    def find_by_name(self, name):
        """trouver un utilisateur grace à son nom

        Parameters
        ----------
        name : string

        Returns
        -------
        joueur : Joueur
            renvoie l'utilisateur que l'on cherche par son nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet.joueur               "
                        " WHERE name = %(name)s;  ",
                        {"name": name},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        joueur = None
        if res:
            joueur = Joueur(puuid=res["puuid"], name=res["name"])

        return joueur

    def find_by_puuid(self, puuid):
        """trouver un utilisateur grace à son nom

        Parameters
        ----------
        puiid : string

        Returns
        -------
        joueur : Joueur
            renvoie l'utilisateur que l'on cherche par son nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet.joueur               "
                        " WHERE puuid = %(puuid)s;  ",
                        {"puuid": puuid},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        joueur = None
        if res:
            joueur = Joueur(puuid=res["puuid"], name=res["name"])

        return joueur
