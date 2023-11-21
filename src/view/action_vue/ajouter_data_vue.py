from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from api.fill_data_base import FillDataBase

class AjouterDataVue(VueAbstraite):
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
                "message": " Attention ! Chaqun des ajouts ne peut être executé qu'une seule fois",
                "choices": [ "Peu de données (environ 20 mins)", "Beaucoup de données (environ 3h)", 'Annuler'],
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

        if reponse["choix"] == "Annuler":
            from view.utils_vue.accueil_vue import AccueilVue
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Peu de données (environ 20 mins)":
            FillDataBase().initiate(0,2,2,2)
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Beaucoup de données (environ 2h)":
            FillDataBase().initiate(0,5,5,3)
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")
