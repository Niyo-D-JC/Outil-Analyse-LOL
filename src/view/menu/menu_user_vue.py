from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.session.session import Session
            

class MenuUserVue(VueAbstraite):
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
        session = Session()
        add_ques = []
        if (not session.joueur):
            add_ques.append("Vous n'êtes pas associés à un joueur, Associez maintenant")

        self.questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Faites votre choix",
                "choices": add_ques + [ "Accéder aux Statistiques Personnelles", "Accéder aux Statistiques Générales", "Se déconnecter"],
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
            session = Session()
            session.user , session.role = None , None
            return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Accéder aux Statistiques Personnelles":
            from view.action_vue.statistiques_perso_vue import StatistiquesPersoVue
            return StatistiquesPersoVue("Bienvenue sur Votre Application ViewerOn LoL")
        
        elif reponse["choix"] == "Accéder aux Statistiques Générales":
            from view.action_vue.statistiques_vue import StatistiquesVue
            return StatistiquesVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Vous n'êtes pas associés à un joueur, Associez maintenant":
            from view.action_vue.update_compte_vue import UpdateCompteVue 
            return UpdateCompteVue()
