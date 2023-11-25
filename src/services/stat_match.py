from business_object.user.joueur import Joueur
from business_object.battle.team import Team
from business_object.stats.stat_joueur import StatJoueur


class StatMatch:
    def kda_team(self, df_team):
        team_kills = df_team["kills"].sum()
        team_deaths = df_team["deaths"].sum()
        team_assists = df_team["assists"].sum()

        return f"{team_kills} / {team_deaths} / {team_assists}"

    def mvp_by_category(self, pd_match, category):
        best_players = []  # Si jamais il y a plusieurs mvp à égalité
        max = 0

        for index, row in pd_match.iterrows():
            var = row[category]

            if var >= max:
                if var == max:
                    best_players.append(row["joueur"])
                else:
                    max = var
                    best_players = [row["joueur"]]

        if len(best_players) == 1:
            return best_players[0]
        else:
            return best_players
