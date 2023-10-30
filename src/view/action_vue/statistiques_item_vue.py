from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite


class StatistiquesItemVue(VueAbstraite):
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
                "choices": [ "Filtrer par popularité", "Filter par taux de victoire", "Retour"],
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
            from view.action_vue.statistiques_vue import StatistiquesVue
            return StatistiquesVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Filtrer par popularité":
            from services.invite_service import InviteService
            from view.action_vue.statistiques_vue import StatistiquesVue
            InviteService().get_all_items()
            return StatistiquesVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Filter par taux de victoire":
            from services.invite_service import InviteService
            from view.action_vue.statistiques_vue import StatistiquesVue
            InviteService().get_all_items(True)
            return StatistiquesVue("Bienvenue sur Votre Application ViewerOn LoL")