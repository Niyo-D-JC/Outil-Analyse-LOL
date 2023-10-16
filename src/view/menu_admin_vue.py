from InquirerPy import prompt

from view.vue_abstraite import VueAbstraite
from services.fill_data_base import FillDataBase
from utils.reset_database import ResetDatabase
from view.accueil_vue import AccueilVue

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
            pass
        elif reponse["choix"] == "Réinitialiser la base de données":
            succes = ResetDatabase().lancer()
            fill = FillDataBase().run(name = "KC NEXT ADKING")
            message = (
                "Ré-initilisation de la base de données terminée" if succes else None
            )
            return AccueilVue(message) 

        elif reponse["choix"] == "Changer un mot de passe":
            pass #à coder

if __name__ == "__main__":
    succes = ResetDatabase().lancer()
    fill = FillDataBase().run(name = "KC NEXT ADKING")