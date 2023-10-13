from InquirerPy import prompt

from view.vue_abstraite import VueAbstraite
from view.connexion_vue import ConnexionVue
from view.session import Session
from utils.reset_database import ResetDatabase


class AccueilVue(VueAbstraite):
    """Vue de l'accueil de l'application du Jeu de Rôle.

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
                "choices": [
                    "Afficher les statistiques d'un champion",
                    "Trier les champions",
                    "Se connecter",
                    "Quitter",
                    "Créer un compte"
                ],
            }
        ]
    def banner(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisi par l'utilisateur dans le terminal
        """
        reponse = prompt(self.questions)

        if reponse["choix"] == "Quitter":
            pass
        elif reponse["choix"] == "Se connecter":
            return ConnexionVue()
        elif reponse["choix"] == "Afficher les statistiques d'un champion":
            return ChampionVue()
        elif reponse["choix"] == "Trier les champions":
            return ChampionVue()
        elif reponse["choix"] == "Créer un compte":
            return CreationCompteVue()