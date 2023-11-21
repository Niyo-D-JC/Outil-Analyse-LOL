from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.action_vue.connexion_vue import ConnexionVue
from view.session.session import Session
from utils.reset_database import ResetDatabase
from view.action_vue.creer_compte_vue import CreerCompteVue
from view.menu.menu_invite_vue import MenuInviteVue
from view.action_vue.ajouter_data_vue import AjouterDataVue

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
                    "Créer un Compte",
                    "Se connecter",
                    "Continuer en tant qu'invité",
                    "Charger plus de données",
                    "Quitter"
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
            session = Session()
            if (session.user):
                if session.role == "Admin" :
                    message = f"Administrateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                    from view.menu.menu_admin_vue import MenuAdminVue

                    return MenuAdminVue(message)

                if session.role == "User":
                    message = f"Utilisateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                    from view.menu.menu_user_vue import MenuUserVue

                    return MenuUserVue(message)
            else : 
                return ConnexionVue()

        elif reponse["choix"] == "Créer un Compte":
            return CreerCompteVue()
        elif reponse["choix"] == "Continuer en tant qu'invité":
            return MenuInviteVue("Invité : Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Charger plus de données":
            return AjouterDataVue()
