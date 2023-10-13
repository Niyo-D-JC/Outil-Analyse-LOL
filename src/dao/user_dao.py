from dao.db_connection import DBConnection
from utils.singleton import Singleton

class UserDao(metaclass=Singleton):
    def creer(self, user) -> bool:
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        user : User

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
                        "INSERT INTO projet.user(name, password, role) VALUES "
                        "(%(name)s, %(password)s, %(role)s)             "
                        "  RETURNING user_id;                                                ",
                        {
                            "name": user.username,
                            "password": user.password,
                            "role": "Utilisateur"
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    