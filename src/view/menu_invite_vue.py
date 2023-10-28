from InquirerPy import prompt

from view.vue_abstraite import VueAbstraite
#from service.joueur_service import JoueurService


class MenuJoueurVue(VueAbstraite):
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
                "choices": [ "Afficher les statistiques d'un champion", "Trier les champions",
                 "Afficher les Statistiques Globales", "Lister les Parties du Joueur", "Se déconnecter"],
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
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Afficher les Statistiques Globales":
            pass
        
        elif reponse["choix"] == "Trier les champions":
            pass

        elif reponse["choix"] == "Afficher les statistiques d'un champion":
            pass

        elif reponse["choix"] == "Lister les Parties du Joueur":
            pass