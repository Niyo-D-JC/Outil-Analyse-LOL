# L'objectif est de récupérer des id de joueurs de chaque division
# On récupère leurs dernières games, puis on stocke tout ça pour faire
# les stats générales


import requests, json, dotenv


api_key = "RGAPI-2e1b078e-0119-4314-96ef-b6dc1771101e"


def ListPlayerbyDivisions():
    tiers_list = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINIUM", "EMERALD", "DIAMOND"]
    divisions_list = ["IV", "III", "II", "I"]
    page = list(range(1, 50))

    url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{divison}?page={page}&api_key={api_key}"

    player_list_data = requests.get(final_account_url)
    player_list_data.json()

    for player_data in player_list_data:
        summonerName = player_data.json()["summonerName"]
        summoner_id = player_data.json()["summonerId"]
        league_id = player_data.json()["leagueId"]
        tier = player_data.json()["tier"]
        rank = player_data.json()["rank"]
        # Save player to database

    # Can add Master Grandmaster and Challenger players
    pass

def get_puuid_with_SummonerName(summonerName):

    account_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
    final_account_url = account_url + summonerName + '?api_key=' + api_key

    account_data = requests.get(final_account_url)
    account_data.json()

    puuid = account_data.json()['puuid']

    retrun puuid 



def ListMatchesbyPuuid(puiid):

    list_match_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'
    first_game, last_game = 0, 20
    final_list_match_url = list_match_url + puuid + '/ids?start=' + str(first_game) + '&' + 'count=' + str(last_game) + '&api_key=' + api_key
    list_match_data = requests.get(final_list_match_url)    
    list_match_data.json()

    return list_match_data.json()


def getMatchInfo(match_id):
    match_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/'
    final_match_url = match_url + match_id + '?api_key=' + api_key
    match_data = requests.get(final_match_url)

    # Save Match info to data base 

    return  match_data.json() # Ne pas tout exporter peut etre 

