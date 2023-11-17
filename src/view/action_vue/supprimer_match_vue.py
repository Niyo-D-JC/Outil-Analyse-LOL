from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.session.session import Session
from services.user_service import UserService


class SupprimerMatchVue(VueAbstraite):
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
        if (session):
            df = UserService().all_parties()
            add_ques = add_ques + list(df.match_id.unique())
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
            if (session.user):
                if session.role == "Admin" :
                    message = f"Administrateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                    from view.menu.menu_admin_vue import MenuAdminVue

                    return MenuAdminVue(message)

                if session.role == "User":
                    message = f"Utilisateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                    from view.menu.menu_user_vue import MenuUserVue

                    return MenuUserVue(message)
            else : 
                from view.menu.menu_invite_vue import MenuInviteVue
                return MenuInviteVue("Invité : Bienvenue sur Votre Application ViewerOn LoL")

        else :
            UserService().delete_match(reponse["choix"])
            print("")
            print("Le Match " + reponse["choix"] + " a été supprimé avec succes ! ")
            print("")
            input("Appuyez sur Entrée pour retourner à la liste des parties ...")
            return self.__class__("Bienvenue sur Votre Application ViewerOn LoL")