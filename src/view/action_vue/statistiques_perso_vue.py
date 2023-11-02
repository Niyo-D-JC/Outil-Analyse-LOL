from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.session.session import Session
from business_object.user.user import User
from services.user_service import UserService
import time

class StatistiquesPersoVue(VueAbstraite):
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
                "choices": [ "Accéder au Bilan Personnel", "Voir les Parties Disponibles", "Retour"],
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
                from view.menu.menu_invite_vue import MenuInviteVue
                return MenuInviteVue("Invité : Bienvenue sur Votre Application ViewerOn LoL")

        elif reponse["choix"] == "Accéder au Bilan Personnel":
            session = Session()
            if(session.joueur):
                user = User(name=session.user, role=session.role, joueur=session.joueur)
                UserService().get_stats_perso(user)
                input("Appuyez sur Entrée pour afficher retourner ...")
                return self.__class__("Bienvenue sur Votre Application ViewerOn LoL")
            else : 
                print("Vous n'êtes pas associés à un joueur, Associez maintenant")
                time.sleep(3)
                from view.action_vue.update_compte_vue import UpdateCompteVue 
                return UpdateCompteVue()

        elif reponse["choix"] == "Voir les Parties Disponibles":
            from view.action_vue.parties_vue import PartiesVue
            session = Session()
            if(session.joueur):
                return PartiesVue("Bienvenue sur Votre Application ViewerOn LoL")
            else : 
                print("Vous n'êtes pas associés à un joueur, Associez maintenant")
                time.sleep(3)
                from view.action_vue.update_compte_vue import UpdateCompteVue 
                return UpdateCompteVue()
            