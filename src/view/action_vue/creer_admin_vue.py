from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from services.joueur_service import JoueurService
from business_object.user.user import User
from services.user_service import UserService
import time


class CreerAdminVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)
        self.questions = [
            {"type": "input", "name": "pseudo", "message": "Entrez votre username :"},
            {"type": "password", "name": "mdp", "message": "Entrez votre mot de passe :"},
            {"type": "input", "name": "joueur", "message": "Nom de votre Joueur (Optionel) :"},
    ]

    def afficher(self):
        self.nettoyer_console()
        print("Creez votre compte")
        print()

    def choisir_menu(self):
        answers = prompt(self.questions)

        puuid = ""
        user = None

        joueur = JoueurService().find_by_name(
            answers["joueur"]
        )  # il faudrait faire un requete API au lieu de chercher dans la BDD

        if joueur != None:
            user = User(answers["pseudo"], answers["mdp"], "Admin", joueur)
            UserService().creer(user)
        else:
            print("")
            print("Aucun Joueur Referencé")
            user = User(answers["pseudo"], answers["mdp"], "Admin")
            UserService().creer_no_puuid(user)

        print("")
        print(
            "------------------------- Le Compte Admin a été Créé -------------------------"
        )
        print("")
        print(
            "----------------------- Retour à la page précédente -------------------------"
        )
        time.sleep(3)
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


if __name__ == "__main__":
    pass
