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
                "message": " Attention ! Chacun des ajouts ne peut être executé qu'une seule fois",
                "choices": [
                    "Ajouter 1000 performances supplémentaires",
                    "Ajouter 10000 performances supplémentaires",
                    "Ajouter 20000 performances supplémentaires",
                    "Annuler",
                ],
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

        elif reponse["choix"] == "Ajouter 1000 performances supplémentaires":
            FillDataBase().initiate(0, 2, 2, 2)
            print("")
            print(
                "--------------------------- Retour à la page précédente ---------------------------"
            )
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Ajouter 10000 performances supplémentaires":
            FillDataBase().initiate(0, 5, 7, 3)
            print("")
            print(
                "--------------------------- Retour à la page précédente ---------------------------"
            )
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Ajouter 20000 performances supplémentaires":
            FillDataBase().initiate(0, 7, 10, 4)
            print("")
            print(
                "--------------------------- Retour à la page précédente ---------------------------"
            )
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")
