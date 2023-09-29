from InquirerPy import prompt

from view.vue_abstraite import VueAbstraite


class MenuAdminVue(VueAbstraite):
    """Vue du menu de l'admin

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
                "choices": ["Réinitialiser la base de données", "Se déconnecter","Changer un mot de passe"],
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

        if reponse["choix"] == "Se déconnecter":
            from view.accueil_vue import AccueilVue

        elif reponse["choix"] == "Ré-initialiser la base de données":
            succes = ResetDatabase().lancer()
            message = (
                "Ré-initilisation de la base de données terminée" if succes else None
            )
            return AccueilVue(message)

            return AccueilVue()
        elif reponse["choix"] == "Changer un mot de passe":
            pass #à coder