from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
#from service.joueur_service import JoueurService


class GestionBDVue(VueAbstraite):
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
                "choices": ["Ajouter un Administrateur", "Supprimer un Compte",  "Supprimer un Match", "Retour"],
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
            from view.menu.menu_admin_vue import MenuAdminVue
            return MenuAdminVue("Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Ajouter un Administrateur":
            pass

        elif reponse["choix"] == "Supprimer un Compte":
            pass
        
        elif reponse["choix"] == "Supprimer un Match":
            pass