from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite


class ChampionsVue(VueAbstraite):
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
                "choices": [ "Accéder aux statistiques Générales", "Revenir au Menu Principal"],
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

        if reponse["choix"] == "Revenir au Menu Principal":
            from view.utils_vue.accueil_vue import AccueilVue
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Accéder aux statistiques Générales":
            pass