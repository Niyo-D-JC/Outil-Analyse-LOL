from InquirerPy import prompt

from view.utils_vue.vue_abstraite import VueAbstraite
from view.session.session import Session
from services.user_service import UserService
from dao.champion_dao import ChampionDao

from view.menu.menu_user_vue import MenuUserVue


class PartiesVue(VueAbstraite):
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

        lines_to_add = []

        if session.joueur:
            df = UserService().get_match_list_bypuuid(session.joueur.puuid)

        for index, row in df.iterrows():
            # Extraire les valeurs nécessaires de la ligne
            match_id = row["match_id"]
            champion_id = row["champion_id"]
            kills = row["kills"]
            deaths = row["deaths"]
            assists = row["assists"]
            win = row["win"]

            champion_name = ChampionDao().find_by_id(champion_id).name

            line = f"{champion_name} ({kills}/{deaths}/{assists} - {'Win' if win else 'Loss'})[{match_id}]"

            while len(line) <= 70:
                line = line[:-17] + "_" + line[-17:]
                # id_match fait 15 caractères et 2 pour les crochets

            lines_to_add.append(line)

        self.questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Faites votre choix",
                "choices": ["Retour"] + lines_to_add,
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
            if session.user:
                if session.role == "Admin":
                    message = f"Administrateur : Vous êtes connecté sous le profil de {session.user.upper()}"
                    from view.menu.menu_admin_vue import MenuAdminVue

                    return MenuAdminVue(message)

                if session.role == "User":
                    message = f"Utilisateur : Vous êtes connecté sous le profil de {session.user.upper()}"
                    from view.menu.menu_user_vue import MenuUserVue

                    return MenuUserVue(message)
            else:
                from view.menu.menu_invite_vue import MenuInviteVue

                return MenuInviteVue(
                    "Invité : Bienvenue sur Votre Application ViewerOn LoL"
                )

        else:
            start_index = reponse["choix"].find("[") + 1
            end_index = reponse["choix"].find("]")
            match_id = reponse["choix"][start_index:end_index]

            UserService().vue_partie(match_id)
            print("")

            input("Appuyez sur Entrée pour retourner à la liste des parties ...")
            return self.__class__("Bienvenue sur Votre Application ViewerOn LoL")


if __name__ == "__main__":
    champion_name = ChampionDao().find_by_id(27).name
    print(champion_name)

    Acc().choisir_menu()
