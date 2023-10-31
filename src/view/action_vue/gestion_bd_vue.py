from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite


class GestionBDVue(VueAbstraite):
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
        self.questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Faites votre choix",
                "choices": ["Ajouter un Administrateur", "Supprimer un Compte",  "Supprimer un Match", "Retour"],
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

        elif reponse["choix"] == "Ajouter un Administrateur":
            pass

        elif reponse["choix"] == "Supprimer un Compte":
            pass
        
        elif reponse["choix"] == "Supprimer un Match":
            pass