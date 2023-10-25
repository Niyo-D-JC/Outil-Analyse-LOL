from dao.db_connection import DBConnection
from utils.singleton import Singleton
from business_object.user.user import User


class UserDao(metaclass=Singleton):
    def creer(self, user):
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        user : User

        Returns
        -------
        user_id : int,  l'identifiant de l'objet créé
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.user(puuid, name, password, role) VALUES "
                        "(%(puuid)s, %(name)s, %(password)s, %(role)s)             "
                        "  RETURNING user_id ; ",
                        {
                            "puuid": user.joueur.puuid,
                            "name": user.name,
                            "password": user.password,
                            "role": user.role,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return res["user_id"]

    def creer_no_puuid(self, user):
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        user : User

        Returns
        -------
        user_id : int,  l'identifiant de l'objet créé
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.user(name, password, role) VALUES "
                        "(%(name)s, %(password)s, %(role)s)             "
                        "  RETURNING user_id ; ",
                        {
                            "name": user.name,
                            "password": user.password,
                            "role": user.role,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return res["user_id"]

    def find_by_name(self, name):
        """trouver un utilisateur grace à son nom

        Parameters
        ----------
        name : string

        Returns
        -------
        user : User
            renvoie l'utilisateur que l'on cherche par son nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                           "
                        " FROM projet.user               "
                        " WHERE name = %(name)s;  ",
                        {"name": name},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        user = None
        if res:
            user = User(name=res["name"], password=res["password"], role=res["role"])

        return user
