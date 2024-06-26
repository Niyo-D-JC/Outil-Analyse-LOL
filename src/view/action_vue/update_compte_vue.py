from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from services.joueur_service import JoueurService
from business_object.user.user import User
from services.user_service import UserService
from view.session.session import Session
import time


class UpdateCompteVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)
        self.questions = [
            {"type": "input", "name": "joueur", "message": "Nom de votre Joueur :"},
        ]

    def afficher(self):
        self.nettoyer_console()
        print("Mis a jour de vos informations")
        print()

    def choisir_menu(self):
        answers = prompt(self.questions)

        puuid = ""
        user = None

        joueur = JoueurService().create_joueur_object(answers["joueur"])

        if joueur != None:
            session = Session()
            session.joueur = joueur

            JoueurService().creer(joueur)
            UserService().update_puuid(joueur.puuid, session.user)
            print("")
            print(
                "-------------------------Votre Compte a été Mis à Jour-------------------------"
            )
        else:
            print("")
            print("Aucun joueur ne porte ce nom d'invocateur")

        print("")
        print(
            "-------------------------- Retour sur votre Page ---------------------------"
        )
        time.sleep(2)
        session = Session()
        
        if session.user:
            if session.role == "Admin":
                message = f"Administrateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                from view.menu.menu_admin_vue import MenuAdminVue

                return MenuAdminVue(message)

            if session.role == "User":
                message = f"Utilisateur : Vous êtes connectés sous le profil de {session.user.upper()}"
                from view.menu.menu_user_vue import MenuUserVue

                return MenuUserVue(message)


if __name__ == "__main__":
    CreerCompteVue("").choisir_menu()
