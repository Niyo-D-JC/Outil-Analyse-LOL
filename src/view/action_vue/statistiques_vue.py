from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.session.session import Session

class StatistiquesVue(VueAbstraite):
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
                "choices": [ "Statistiques sur les Champions", "Statistiques sur les Items", "Retour"],
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

        elif reponse["choix"] == "Statistiques sur les Champions":
            from view.action_vue.statistiques_champion_vue import StatistiquesChampionVue
            return StatistiquesChampionVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Statistiques sur les Items":
            from view.action_vue.statistiques_item_vue import StatistiquesItemVue
            return StatistiquesItemVue("Bienvenue sur Votre Application ViewerOn LoL")