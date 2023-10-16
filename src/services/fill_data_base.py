# L'objectif est de récupérer des id de joueurs de chaque division
# On récupère leurs dernières games, puis on stocke tout ça pour faire
# les stats générales
import requests, json, dotenv, os
from business_object.battle.match import Match
from business_object.battle.team import Team
from business_object.user.joueur import Joueur
from business_object.user.user import User
from business_object.tools.champion import Champion
from business_object.tools.items import Item
from business_object.tools.lane import Lane, LANE
from business_object.stats.stat_joueur import StatJoeur
from dao.champion_dao import ChampionDao
from dao.items_dao import ItemsDao
from dao.joueur_dao import JoueurDao
from dao.user_dao import UserDao
from dao.match_dao import MatchDao
from dao.team_dao import TeamDao
from dao.itemmatch_dao import ItemMatchDao
import time

SIDE = {100 : "Blue", 200 : "Purple"}

class FillDataBase:
    def __init__(self):
        dotenv.load_dotenv(override=True)
        f = open('data/item.json')

        self.HOST_WEBSERVICE_EUW1 = os.environ["HOST_WEBSERVICE_EUW1"]
        self.HOST_WEBSERVICE_EUROPA = os.environ["HOST_WEBSERVICE_EUROPA"]
        self.API_KEY = os.environ["API_KEY"]
        self.items = json.load(f)
    
    def RequestNoRateLimitExceed(self, url, key_):
        try : 
            response = requests.get(url).json()
            status = response[key_]
            return response
        except :
            time.sleep(121)
            response = requests.get(url).json()
            return response

    def getJoueur(self, puuid) : 
        url = self.HOST_WEBSERVICE_EUROPA + "/riot/account/v1/accounts/by-puuid/" + puuid + '?api_key=' + self.API_KEY
        data = self.RequestNoRateLimitExceed(url,"gameName")
        return Joueur(puuid, data["gameName"])

    def getMatchInfo(self, match_id):
        url = self.HOST_WEBSERVICE_EUROPA + "/lol/match/v5/matches/" + match_id + '?api_key=' + self.API_KEY
        data = self.RequestNoRateLimitExceed(url,"metadata")
        list_match = []
        for puuid in list(data["metadata"]["participants"]) : 
            player_info = data["info"]["participants"][list(data["metadata"]["participants"]).index(puuid)]

            champion = Champion(player_info["championId"],player_info["championName"])
            list_item = [Item(player_info[f"item{i}"], self.items["data"][str(player_info[f"item{i}"])]["name"]) for i in range(7) if str(player_info[f"item{i}"])!= "0"]
            lane = Lane(LANE[player_info["lane"]],player_info["lane"])
            team = Team(team_id= match_id + SIDE[player_info["teamId"]],side= SIDE[player_info["teamId"]])
            stat_joueur = StatJoeur(player_info["totalDamageDealt"],player_info["totalDamageTaken"],
            player_info["totalHeal"],player_info["challenges"]["kda"],bool(player_info["win"]))
            joueur = self.getJoueur(puuid)
            JoueurDao().creer(joueur)
            match = Match(match_id, joueur,champion, list_item, lane, team, stat_joueur)
            ChampionDao().creer(champion)

            TeamDao().creer(team)

            MatchDao().creer(match)

            [ItemsDao().creer(item_) and ItemMatchDao().creer(match_id,puuid,item_.tools_id) for item_ in list_item]

            
            list_match.append(match)

        return  list_match

    def run(self, name, first_game = 0, last_game = 5):
        url = self.HOST_WEBSERVICE_EUW1 + "/lol/summoner/v4/summoners/by-name/" + name + '?api_key=' + self.API_KEY
        puuid_ref = self.RequestNoRateLimitExceed(url,'puuid')['puuid']
        url = self.HOST_WEBSERVICE_EUROPA + "/lol/match/v5/matches/by-puuid/" + puuid_ref + '/ids?start=' + str(first_game) + '&' + 'count=' + str(last_game) + '&api_key=' + self.API_KEY
        list_match_data = list(self.RequestNoRateLimitExceed(url,"metadata"))
        [self.getMatchInfo(match_id) for match_id in  list_match_data]
        UserDao().creer(User("admin", "admin", "Admin", self.getJoueur(puuid_ref)))
        return True

if __name__ == "__main__":
    FillDataBase().run(name = "KC NEXT ADKING")