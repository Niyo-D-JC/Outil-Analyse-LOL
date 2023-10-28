from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from utils.reset_database import ResetDatabase
from view.utils_vue.accueil_vue import AccueilVue

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
                "choices": ["Accéder aux Statistiques Personnelles", "Accéder aux Statistiques Générales",
                "Gestion de Base de Données", "Se déconnecter"],
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
            from view.utils_vue.accueil_vue import AccueilVue
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Accéder aux Statistiques Personnelles":
            from view.action_vue.statistiques_perso_vue import StatistiquesPersoVue
            return StatistiquesPersoVue("Bienvenue sur Votre Application ViewerOn LoL")
        
        elif reponse["choix"] == "Accéder aux Statistiques Générales":
            from view.action_vue.statistiques_vue import StatistiquesVue
            return StatistiquesVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Gestion de Base de Données":
            from view.action_vue.statistiques_vue import StatistiquesVue
            return StatistiquesVue("Bienvenue sur Votre Application ViewerOn LoL")

if __name__ == "__main__":
    pass