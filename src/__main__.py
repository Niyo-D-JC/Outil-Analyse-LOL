import dotenv
from view.accueil_vue import AccueilVue
from services.user_service import UserService
from services.fill_data_base import FillDataBase
from utils.reset_database import ResetDatabase

"""
Classe de lancement de l'application
"""
if __name__ == "__main__":
    # On charge les variables d'envionnement
    dotenv.load_dotenv(override=True)
    try : 
        UserService().find_by_name("admin").name
    except :
        print("Premiere Ouverture de l'Application")
        ResetDatabase().lancer()
        FillDataBase().run(name = "KC NEXT ADKING")

    vue_courante = AccueilVue("Bienvenue sur Votre Application ViewerOn LoL")
    nb_erreurs = 0

    while vue_courante:
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())
        if nb_erreurs > 100:
            print("Le programme recense trop d'erreurs et va s'arrêter")
            break
        try:
            # Affichage du menu
            vue_courante.afficher()

            # Affichage des choix possibles
            vue_courante = vue_courante.choisir_menu()
        except Exception as e:
            print(e)
            nb_erreurs += 1
            vue_courante = AccueilVue(
                "Une erreur est survenue, retour au menu principal"
            )

    # Lorsque l on quitte l application
    print("---------------------------------")
    print("Au revoir")
