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
TIER = ["DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "IRON"]
DIVISION = ["I", "II", "III", "IV"]


class FillDataBase:
    def __init__(self):
        dotenv.load_dotenv(override=True)
        f = open("data/item.json")
        fc = open("data/champion.json", "r", encoding="utf-8")
        print("")
        self.bar = tqdm()
        self.HOST_WEBSERVICE_EUW1 = os.environ["HOST_WEBSERVICE_EUW1"]
        self.HOST_WEBSERVICE_EUROPA = os.environ["HOST_WEBSERVICE_EUROPA"]
        self.API_KEY = os.environ["API_KEY"]
        self.items = json.load(f)
        self.champions = json.load(fc)

    def reqLimit(self, url, key_=None):
        if key_:
            try:
                response = requests.get(url).json()
                status = response[key_]
                return response
            except:
                self.bar.set_description(
                    "Limit Rate Requests Atteint : Attendre 2 minutes sup"
                )
                time.sleep(125)
                response = requests.get(url).json()
                return response
        else:
            response = requests.get(url).json()
            if response != []:
                return response
            else:
                self.bar.set_description(
                    "Limit Rate Requests Atteint : Attendre 2 minutes sup"
                )
                time.sleep(125)
                response = requests.get(url).json()
                return response

    def getJoueurByLeague(self, tier, div, first=True, limit=0):
        url = (
            self.HOST_WEBSERVICE_EUW1
            + "/tft/league/v1/entries/"
            + tier
            + "/"
            + div
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

    def getJoueurBySummonerId(self, summonerId, first=True, limit=0):
        url = (
            self.HOST_WEBSERVICE_EUW1
            + "/tft/league/v1/entries/by-summoner/"
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

    def getJoueurMatchInfo(self, joueur: Joueur, match_id: str):
        url = (
            self.HOST_WEBSERVICE_EUROPA
            + "/lol/match/v5/matches/"
            + match_id
            + "?api_key="
            + self.API_KEY
        )
        data = self.reqLimit(url, "metadata")

        player_info = data["info"]["participants"][
            list(data["metadata"]["participants"]).index(joueur.puuid)
        ]
        champion = Champion(player_info["championId"], player_info["championName"])
        list_item = [
            Item(
                player_info[f"item{i}"],
                self.items["data"][str(player_info[f"item{i}"])]["name"],
                i,
            )
            for i in range(7)
            if str(player_info[f"item{i}"]) != "0"
        ]
        lane = Lane(LANE[player_info["lane"]], player_info["lane"])
        team = Team(
            team_id=player_info["teamId"],
            side=SIDE[player_info["teamId"]],
        )
        stat_joueur = StatJoueur(
            player_info["kills"],
            player_info["deaths"],
            player_info["assists"],
            player_info["totalMinionsKilled"],
            player_info["goldEarned"],
            player_info["totalDamageDealt"],
            player_info["totalDamageTaken"],
            player_info["totalHeal"],
            bool(player_info["win"]),
        )
        matchjoueur = MatchJoueur(
            match_id, joueur, champion, list_item, lane, team, stat_joueur
        )
        return matchjoueur

    def getJoueurAllMatchInfo(self, joueur, first_game=0, last_game=20):
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
        JoueurDao().creer(joueur)
        for match_id in list_match:
            try:
                matchjoueur = self.getJoueurMatchInfo(joueur, match_id)
                MatchJoueurDao().creer(matchjoueur)
                [
                    ItemMatchDao().creer(
                        match_id, joueur.puuid, item_.tools_id, item_.item_position
                    )
                    for item_ in matchjoueur.items
                ]

            except:
                pass
            self.bar.set_description("Chargement en Cours")
            self.bar.update(1)
        return 1

    def initiate(self, first_game=0, last_game=20):
        for it in self.items["data"].keys():
            ItemsDao().creer(Item(it, self.items["data"][it]["name"]))
        for cp in self.champions["data"].keys():
            ChampionDao().creer(Champion(self.champions["data"][cp]["key"], cp))
        self.bar.total = len(TIER) * len(DIVISION) * (last_game - first_game)
        for T in TIER:
            for D in DIVISION:
                joueur = self.getJoueurByLeague(T, D)
                self.getJoueurAllMatchInfo(
                    joueur, first_game=first_game, last_game=last_game
                )

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
        return Joueur(puuid, data["gameName"])

    def add_matches(self, user: User):
        pass


if __name__ == "__main__":
    FillDataBase().initiate(0, 3)
