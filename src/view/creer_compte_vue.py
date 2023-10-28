from InquirerPy import prompt

from view.vue_abstraite import VueAbstraite
from services.joueur_service import JoueurService
from business_object.user.user import User
from services.user_service import UserService
import time 

class CreerCompteVue(VueAbstraite):
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
        
        joueur = JoueurService().find_by_name(answers["pseudo"])
        if joueur != None :
            user = User(answers["pseudo"],answers["mdp"],"User",joueur)
            UserService().creer(user)
        else :    
            print("")         
            print("Aucun Joueur Referencé")
            user = User(answers["pseudo"],answers["mdp"],"User")    
            UserService().creer_no_puuid(user)
        
        print("")
        print("-------------------------Votre Compte a été Créé-------------------------")
        print("")
        print("-----------------------Retour à la page d'accueil-------------------------")
        time.sleep(3)
        from view.accueil_vue import AccueilVue
        return AccueilVue("Bienvenue sur Votre Application ViewerOn LoL") 

       

if __name__ == "__main__":
     CreerCompteVue("").choisir_menu()