# L'objectif est de récupérer des id de joueurs de chaque division
# On récupère leurs dernières games, puis on stocke tout ça pour faire
# les stats générales


import requests
import json
import dotenv
import os

from business_object.battle.matchjoueur import MatchJoueur
from business_object.battle.team import Team
from business_object.user.joueur import Joueur
from business_object.user.user import User
from business_object.tools.champion import Champion
from business_object.tools.items import Item
from business_object.tools.lane import Lane, LANE
from business_object.stats.stat_joueur import StatJoueur
from dao.champion_dao import ChampionDao
from dao.items_dao import ItemsDao
from dao.joueur_dao import JoueurDao
from dao.user_dao import UserDao
from dao.matchjoueur_dao import MatchJoueurDao
from dao.team_dao import TeamDao
from dao.itemmatch_dao import ItemMatchDao
import time
from tqdm import tqdm


SIDE = {100: "Blue", 200: "Purple"}
list_TIER = ["DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "IRON"]
list_DIVISION = ["I", "II", "III", "IV"]


class FillDataBase:
    def __init__(self):
        dotenv.load_dotenv(override=True)

        self.bar = tqdm()
        self.HOST_WEBSERVICE_EUW1 = "https://euw1.api.riotgames.com"
        self.HOST_WEBSERVICE_EUROPA = "https://europe.api.riotgames.com"
        self.API_KEY = os.environ["API_KEY"]
        self.items = json.load(open("data/item.json"))
        self.champions = json.load(open("data/champion.json", "r", encoding="utf-8"))

    def reqLimit(self, url, key_=None):
        try:
            response = requests.get(url)

            if response.status_code == 200:  # tout va bien
                return response.json()

            elif response.status_code == 429:  # Trop de requetes
                self.bar.set_description(
                    "Limit Rate Requests Atteint :  Attendre 1 seconde"
                )
                time.sleep(1)

                response = requests.get(url)

                if response.status_code == 429:
                    self.bar.set_description(
                        "Limit Rate Requests Atteint : Attendre 2 minutes"
                    )
                    time.sleep(121)

                    response = requests.get(url)
                    if response.status_code == 200:  # apres les 2 mins d'attente, OK
                        return response.json()
                    else:
                        pass

                elif response.status_code == 200:  # après la seconde d'attente
                    return response.json()
                else:
                    pass

        except:  # si ce n'est pas ok et que ce n'est pas à cause du limitRate
            pass

    def getJoueurByLeague(self, tier, div, first=True, limit=0, page=1):
        url = (
            self.HOST_WEBSERVICE_EUW1
            + "/lol/league/v4/entries/RANKED_SOLO_5x5/"
            + tier
            + "/"
            + div
            + "?page="
            + str(page)
            + "&api_key="
            + self.API_KEY
        )

        data = self.reqLimit(url)

        if first or limit <= 0:
            dta = data[0]

            # print("")
            # print(dta)

            if self.get_puuid(dta["summonerName"]) is not None:
                puuid = self.get_puuid(dta["summonerName"])
                name = dta["summonerName"]
                tier = dta["tier"]

                return Joueur(puuid, name, tier)

        else:
            return [
                Joueur(
                    puuid=puuid,
                    name=dta["summonerName"],
                    tier=dta["tier"],
                )
                for dta in data[:limit]
                if (puuid := self.get_puuid(dta["summonerName"])) is not None
            ]

    def getJoueurBySummonerId(self, summonerId, first=True, limit=0):  # Jamais utilisé
        url = (
            self.HOST_WEBSERVICE_EUW1
            + "/lol/league/v4/entries/by-summoner/"
            + summonerId
            + "?api_key="
            + self.API_KEY
        )
        data = self.reqLimit(url)
        if first or limit <= 0:
            dta = data[0]
            return Joueur(dta["puuid"], dta["summonerName"], dta["tier"])
        else:
            return [
                Joueur(dta["puuid"], dta["summonerName"], dta["tier"])
                for j in data[:limit]
            ]

    def getJoueurMatchInfo(
        self, match_id: str, include_tier: bool = False
    ):  # La plus importante
        self.bar.set_description("Chargemnent en cours")

        url = (
            self.HOST_WEBSERVICE_EUROPA
            + "/lol/match/v5/matches/"
            + match_id
            + "?api_key="
            + self.API_KEY
        )
        data = self.reqLimit(url, "metadata")

        for player_k in range(0, 10):
            try:
                player_info = data["info"]["participants"][player_k]

                joueur = Joueur(
                    puuid=player_info["puuid"],
                    name=player_info["summonerName"],
                    tier=self.get_tier(
                        puuid=None, summoner_id=player_info["summonerId"]
                    )
                    if include_tier
                    else None,
                )

                JoueurDao().creer(joueur)

                # print("")
                # print(joueur)

                champion = Champion(
                    player_info["championId"], player_info["championName"]
                )

                list_item = [
                    Item(
                        player_info[f"item{i}"],
                        self.items["data"][str(player_info[f"item{i}"])]["name"],
                        i,
                    )
                    for i in range(7)
                    if str(player_info[f"item{i}"]) != "0"
                ]
                lane = Lane(
                    LANE[player_info["teamPosition"]], player_info["teamPosition"]
                )
                team = Team(
                    team_id=player_info["teamId"],
                    side=SIDE[player_info["teamId"]],
                )
                stat_joueur = StatJoueur(
                    player_info["kills"],
                    player_info["deaths"],
                    player_info["assists"],
                    player_info["totalMinionsKilled"]
                    + player_info["neutralMinionsKilled"],
                    player_info["goldEarned"],
                    player_info["totalDamageDealtToChampions"],
                    player_info["totalDamageTaken"],
                    player_info["totalHeal"],
                    bool(player_info["win"]),
                )

                matchjoueur = MatchJoueur(
                    match_id, joueur, champion, list_item, lane, team, stat_joueur
                )

                self.bar.update(1)

                MatchJoueurDao().creer(matchjoueur)

                for item_ in matchjoueur.items:
                    ItemMatchDao().creer(
                        match_id, joueur.puuid, item_.tools_id, item_.item_position
                    )

                # print("")
                # print("Importation success")

            except:
                print("Importation Error")

    def get_matchlist(self, joueur, first_game=0, last_game=20):
        url = (
            self.HOST_WEBSERVICE_EUROPA
            + "/lol/match/v5/matches/by-puuid/"
            + joueur.puuid
            + "/ids?start="
            + str(first_game)
            + "&"
            + "count="
            + str(last_game)
            + "&api_key="
            + self.API_KEY
        )
        list_match = list(self.reqLimit(url))

        return list_match

    def getAllMatchesInfo(self, joueur, first_game, last_game):
        list_match_id = self.get_matchlist(joueur, first_game, last_game)
        for match_id in list_match_id:
            # print("")
            # print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            # print("MATCH ID :", match_id)

            self.getJoueurMatchInfo(match_id)

    def initiate(self, first_game=0, last_game=20, joueur_div=2, page=1):
        iter_necessaire = (
            len(list_TIER)
            * len(list_DIVISION)
            * joueur_div
            * (last_game - first_game)
            * 10
        )

        self.bar.total = iter_necessaire

        print("")
        print(
            "Temps prévu :", round((iter_necessaire / 660) * 2), "minutes"
        )  # aproximation
        print("")
        print("")

        for tier in list_TIER:
            for division in list_DIVISION:
                list_joueurs_league = self.getJoueurByLeague(
                    tier, division, first=False, limit=joueur_div, page=page
                )

                for joueur in list_joueurs_league:
                    # print("")
                    # print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                    # print("IIIIIIIIIIIII JOUEUR DE REFERENCE IIIIIIIIIIIII")
                    # print(joueur)

                    if joueur:
                        self.getAllMatchesInfo(
                            joueur, first_game=first_game, last_game=last_game
                        )

        # print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        # print("IIIIIIIIIIIII FINI IIIIIIIIIIIII")
        # print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

        UserDao().creer_no_puuid(User("admin", "admin", "Admin"))  # faille de sécurité
        self.bar.close()
        return 1

    def getJoueur(self, puuid):
        url = (
            self.HOST_WEBSERVICE_EUROPA
            + "/riot/account/v1/accounts/by-puuid/"
            + puuid
            + "?api_key="
            + self.API_KEY
        )
        data = self.reqLimit(url, "gameName")

        tier = self.get_tier(puuid)

        return Joueur(puuid, data["gameName"], tier)

    def get_puuid(self, name: str):
        url = (
            self.HOST_WEBSERVICE_EUW1
            + "/lol/summoner/v4/summoners/by-name/"
            + name
            + "?api_key="
            + self.API_KEY
        )

        account_data = self.reqLimit(url)

        if account_data:
            account_puuid = account_data["puuid"]

            return account_puuid

    def get_last_matchId(self, puuid: str):
        url = (
            self.HOST_WEBSERVICE_EUROPA
            + "/lol/match/v5/matches/by-puuid/"
            + puuid
            + "/ids?start="
            + str(0)
            + "&"
            + "count="
            + str(1)
            + "&api_key="
            + self.API_KEY
        )
        last_matchId = list(self.reqLimit(url))[0]

        return last_matchId

    def get_summonerId(self, puuid: str):
        match_id = self.get_last_matchId(puuid)

        url = (
            self.HOST_WEBSERVICE_EUROPA
            + "/lol/match/v5/matches/"
            + match_id
            + "?api_key="
            + self.API_KEY
        )
        data = self.reqLimit(url)

        try:
            players_info = data["info"]["participants"]
            # Parcourir la liste de dictionnaires
            for player in players_info:
                if player["puuid"] == puuid:
                    summoner_id = player["summonerId"]
                    break

            return summoner_id

        except:
            pass

    def get_tier(self, puuid: str, summoner_id=None):
        # Pour avoir le rank il faut acceder à la variable summonerID

        if not summoner_id:
            summoner_id = self.get_summonerId(puuid)

        url = (
            self.HOST_WEBSERVICE_EUW1
            + "/lol/league/v4/entries/by-summoner/"
            + summoner_id
            + "?api_key="
            + self.API_KEY
        )

        data = self.reqLimit(url)

        if data:
            for dico in data:
                if dico["queueType"] == "RANKED_SOLO_5x5":
                    tier = dico["tier"]
                    return tier

            # no return = only flex is available
            return data[0]["tier"]

        else:  # No Data
            return "UNRANKED"

    def add_matches_for_user(self, user: User, n_matches=90):
        # Imporation des 20 derniers matchs de l'utilisateur

        self.bar.total = n_matches * 10
        self.getAllMatchesInfo(joueur=user.joueur, first_game=0, last_game=n_matches)


if __name__ == "__main__":
    # ResetDatabase().lancer()
    # FillDataBase().initiate(0, 2, 5)

    puuid = FillDataBase().get_puuid("KC NEXT ADKING")
    print("puuid", puuid)

    summonerid = FillDataBase().get_summonerId(puuid)
    print("summonerid", summonerid)

    tier = FillDataBase().get_tier(puuid)
    print("tier", tier)
