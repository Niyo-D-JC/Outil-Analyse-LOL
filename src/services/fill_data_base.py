# L'objectif est de récupérer des id de joueurs de chaque division
# On récupère leurs dernières games, puis on stocke tout ça pour faire
# les stats générales


import requests, json, dotenv


api_key = "RGAPI-2e1b078e-0119-4314-96ef-b6dc1771101e"


def ListPlayerbyDivisions():
    tiers_list = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINIUM", "EMERALD", "DIAMOND"]
    divisions_list = ["IV", "III", "II", "I"]

    url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{divison}?page=1&api_key={api_key}"

    player_list_data = requests.get(final_account_url)
    player_list_data.json()

    for player_data in player_list_data:
        summoner_id = player_data["summonerId"]
        summonerName = player_data["summonerName"]
        league_id = player_data["leagueId"]
