from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from services.user_service import UserService
from view.session.session import Session

class ConnexionVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)
        self.questions = [
            {"type": "input", "name": "pseudo", "message": "Entrez votre username :"},
            {"type": "password", "name": "mdp", "message": "Entrez votre mot de passe :"},
        ]

    def afficher(self):
        self.nettoyer_console()
        print("Connexion à l'application")
        print()

    def choisir_menu(self):
        answers = prompt(self.questions)
        
        user = UserService().find_by_name(answers["pseudo"])
        if (user.password != answers["mdp"]) : 
            return AccueilVue("Vos identifiants sont incorrects")
        message = ""
        session = Session()
        session.user = user.name
        session.role = user.role
        session.joueur = user.joueur

        if session.role == "Admin" :
            message = f"Administrateur : Vous êtes connectés sous le profil de {session.user.upper()}"
            from view.menu.menu_admin_vue import MenuAdminVue

            return MenuAdminVue(message)

        if session.role == "User":
            message = f"Utilisateur : Vous êtes connectés sous le profil de {session.user.upper()}"
            from view.menu.menu_user_vue import MenuUserVue

            return MenuUserVue(message)

        else:
            message = "Erreur de connexion. Vos identifiants sont incorrects"
            from view.accueil_vue import AccueilVue

            return AccueilVue(message)