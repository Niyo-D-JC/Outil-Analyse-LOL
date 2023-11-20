from business_object.user.joueur import Joueur
from business_object.battle.team import Team
from business_object.stats.stat_joueur import StatJoueur


class Stat_match:
    def __init__(
        self,
        puuid,
        name,
        total_kills,
        total_deaths,
        total_assists,
        total_heal,
        total_dammage_dealt,
        total_dammage_take,
        result,
        team_id,
    ):
        self.puuid = puuid
        self.name = name
        self.team_id = team_id
        self.total_kills = total_kills
        self.total_deaths = total_deaths
        self.total_assists = total_assists
        self.total_heal = total_heal
        self.total_dammage_dealt = total_dammage_dealt
        self.total_dammage_take = total_damage_take
        self.result = result

    def kda_player(self):
        for players in self.players:
            kda = f"KDA de {self.name}: Kills: {self.total_kills}/Deaths: {self.total_deaths}/Assists: {self.total_assists}"
            print(kda)

    def kda_team(self):
        team_kda = {}
        for players in self.players:
            kda = [self.total_kills, self.total_deaths, self.total_assists]
            if self.team_id not in team_kda:
                team_kda[self.team_id] = kda
            else:
                team_kda[self.team_id][0] += kda[0]  # Somme des kills
                team_kda[self.team_id][1] += kda[1]  # Somme des deaths
                team_kda[self.team_id][2] += kda[2]  # Somme des assists

            print(
                f"Team {self.team_id}: Total KDA -> Kills: {team_kda[self.team_id][0]}/Deaths: {team_kda[self.team_id][1]}/Assists: {team_kda[self.team_id][2]}"
            )

    def best_game_attacker(self):
        for players in self.players:
            best_attacker = 0
            while self.total_dammage_dealt >= best_attacker:
                best_attacker = self.name
            return best_attacker

    def best_game_healer(self):
        for players in self.players:
            best_healer = 0
            while self.total_dammage_dealt >= best_healer:
                best_healer = self.name
            return best_healer

    # Créer un tableau qui référence dans un tableau a 2 colonnes le nom des joueurs
    def get_teams(self):
        team1, team2 = [], []
        if self.team_id == 100:
            team1.append((self.name, self.kda_player()))
        elif self.team_id == 200:
            team2.append((self.name, self.kda_player()))
        return (team1, team2)

    def game_summary(self):
        total_kills = sum(player.total_kills for player in self.players)
        total_deaths = sum(player.total_deaths for player in self.players)
        total_assists = sum(player.total_assists for player in self.players)
        total_heal = sum(player.total_heal for player in self.players)
        total_dammage_dealt = sum(player.total_dammage_dealt for player in self.players)
        total_dammage_take = sum(player.total_dammage_take for player in self.players)

        return {
            "TotalKills": total_kills,
            "TotalDeaths": total_deaths,
            "TotalAssists": total_assists,
            "TotalHeal": total_heal,
            "TotalDamageDealt": total_dammage_dealt,
            "TotalDamageTaken": total_dammage_take,
        }


if __name__ == "__main__":
    joueur1 = Stat_match.(
        "puuid1",
        "Joueur1",
        100,
        5,
        2,
        7,
        1000,
        15000,
        1600,
        "5/2/7",
        "Victoire",
    )
    joueur2 = Stat_match().("puuid2", "Joueur2", 100, 3, 4, 6, 800, 12000, 1500, "3/4/6", "Défaite")

    players.kda_team()
