from InquirerPy import prompt
import requests, json, dotenv, os
from view.session.session import Session
from api.fill_data_base import FillDataBase
from view.utils_vue.vue_abstraite import VueAbstraite
from services.joueur_service import JoueurService
from business_object.user.user import User, Joueur
from services.user_service import UserService
import time


class AjouterPartieVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)
        self.questions = [
            {"type": "input", "name": "pseudo", "message": "Entrez le nom du joueur :"},
    ]
        dotenv.load_dotenv(override=True)

        self.HOST_WEBSERVICE_EUW1 = os.environ["HOST_WEBSERVICE_EUW1"]
        self.HOST_WEBSERVICE_EUROPA = os.environ["HOST_WEBSERVICE_EUROPA"]
        self.API_KEY = os.environ["API_KEY"]

    def afficher(self):
        self.nettoyer_console()
        print("Creez votre compte")
        print()

    def choisir_menu(self):
        answers = prompt(self.questions)

        account_url = self.HOST_WEBSERVICE_EUW1 + '/lol/summoner/v4/summoners/by-name/'
        name = answers["pseudo"]
        final_account_url = account_url + name + '?api_key=' + self.API_KEY
        puuid_joueur = None
        try : 
            account_data = requests.get(final_account_url)
            dta = account_data.json()
            name_joueur = dta["name"]
            puuid_joueur = dta["puuid"]
            print()
            print(f"Le joueur a bien été trouvé \n - Nom : {name_joueur} \n - puuid : {puuid_joueur} \n")
            input("Appuyez sur Entrée si vous voulez ajouter ses parties ...")
            from dao.joueur_dao import JoueurDao
            joueur = Joueur(puuid_joueur,name_joueur,"Inconnu")
            if (not(JoueurDao().existe(joueur))):
                JoueurService().creer(joueur)

            list_match_url = self.HOST_WEBSERVICE_EUROPA + '/lol/match/v5/matches/by-puuid/'
            first_game, last_game = 0, 5
            final_list_match_url = list_match_url + puuid_joueur + '/ids?start=' + str(first_game) + '&' + 'count=' + str(last_game) + '&api_key=' + self.API_KEY
            list_match_data = requests.get(final_list_match_url)
            list_match_data.json()

            fill_dta = FillDataBase()
            fill_dta.bar.total = 5
            from dao.matchjoueur_dao import MatchJoueurDao
            from dao.itemmatch_dao import ItemMatchDao

            for match_id in list_match_data.json()[:5]:
                if (not(MatchJoueurDao().existe(joueur,match_id))):
                    matchjoueur = fill_dta.getJoueurMatchInfo(joueur,match_id)
                    MatchJoueurDao().creer(matchjoueur)
                    [
                        ItemMatchDao().creer(match_id, joueur.puuid, item_.tools_id, item_.item_position)
                        for item_ in matchjoueur.items
                    ]

                fill_dta.bar.set_description('Chargement en Cours')
                fill_dta.bar.update(1)
            print("")
            print(
                "------------------------- Les Parties ont bien été ajoutées -------------------------"
            )
        except:
            print("\nLe joueur n'a pas été trouvé")

        
        print("")
        print(
            "--------------------------- Retour à la page précédente ---------------------------"
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
