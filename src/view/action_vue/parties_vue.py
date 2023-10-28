from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
#from service.joueur_service import JoueurService


class PartiesVue(VueAbstraite):
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
                "choices": [ "PARTI1", "PARTIE2", "Retour"],
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
            from view.menu.menu_user_vue import MenuUserVue
            return MenuUserVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "PARTIE":
            pass