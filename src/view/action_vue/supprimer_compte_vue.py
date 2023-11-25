from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.session.session import Session
from services.user_service import UserService


class SupprimerCompteVue(VueAbstraite):
    """Vue du menu du joueur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisi par l'utilisateur de l'application
    """

    def __init__(self, message="") -> None:
        super().__init__(message)
        session = Session()

        add_ques = []
        if session:
            df = UserService().get_users()

            df.sort_values(by="role", ascending=False).reset_index(drop=True)
            df["Role : Name"] = df["role"] + " : " + df["name"]

            df = df.drop(df[df["name"] == "admin"].index)
            add_ques = add_ques + list(df["Role : Name"].unique())

        self.questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Faites votre choix",
                "choices": ["Retour"] + add_ques,
            }
        ]

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisi par l'utilisateur dans le terminal
        """
        reponse = prompt(self.questions)

        if reponse["choix"] == "Retour":
            session = Session()
            if session.user:
                if session.role == "Admin":
                    message = f"Administrateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                    from view.menu.menu_admin_vue import MenuAdminVue

                    return MenuAdminVue(message)

                if session.role == "User":
                    message = f"Utilisateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                    from view.menu.menu_user_vue import MenuUserVue

                    return MenuUserVue(message)
            else:
                from view.menu.menu_invite_vue import MenuInviteVue

                return MenuInviteVue(
                    "Invité : Bienvenue sur Votre Application ViewerOn LoL"
                )

        else:
            UserService().delete_by_name(reponse["choix"].split(":")[1][1:])
            print("")
            print(
                "Le compte "
                + reponse["choix"].split(":")[1][1:].upper()
                + " a été supprimé avec succes !"
            )
            print("")
            input("Appuyez sur Entrée pour continuer ...")
            return self.__class__("Bienvenue sur Votre Application ViewerOn LoL")
