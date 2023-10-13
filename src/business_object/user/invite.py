"""il faut importer les donnee de toutes les parties"""

"""
class stat_champion(JoueurInTeam, Item):
    def __init__(self, id_champ, name_champ, id_item, name_item):
        Champion(self, id_champ, name_champ)
        Item(self, id_item, name_item)
"""


class Invite:
    def __init__(self):
        pass

    def stat_champion(self, list_partie, champion_id, stat, division=None):
        """_summary_

        Args:
            list_partie (list): liste telle que [[id_match, team1=[(idchamp1,iditem1,kda1),...], team2=[(idchamp6,iditem6,kda6),...], vainqueur=1 ou 2, ],...]
            champion_id (int): id du champion
            stat (str): 'win rate', 'KDA', 'pick rate', 'item populaire'
            division (str): 1,2,3,4
        """
        if stat == "win rate":
            s1 = 0
            s2 = 0
            for i in list_partie:
                for j in i[1]:
                    for k in j:
                        if champion_id in k and i[3] == 1:
                            s1 += 1
                        if champion_id in k:
                            s2 += 1
                for j in i[2]:
                    for k in j:
                        if champion_id in k and i[3] == 2:
                            s1 += 1
                        if champion_id in k:
                            s2 += 1
            wr = s1 / s2
        if stat == "KDA":
            kill = 0
            death = 0
            assist = 0
            s2 = 0
            for i in list_partie:
                for j in i[1]:
                    for k in j:
                        if champion_id in k:
                            kill += k[2][0]
                            death += k[2][1]
                            assist += k[2][2]
                            s2 += 1
                for j in i[2]:
                    for k in j:
                        if champion_id in k:
                            kill += k[2][0]
                            death += k[2][1]
                            assist += k[2][2]
                            s2 += 1
                kda = [kill / s2, death / s2, assist / s2]
        if stat == "pick rate":
            s2 = 0
            for i in list_partie:
                for j in i[1]:
                    for k in j:
                        if champion_id in k:
                            s2 += 1
                for j in i[2]:
                    for k in j:
                        if champion_id in k:
                            s2 += 1
            pr = s2 / len(list_partie)
        pass

    def stat_item():
        """item populaire, item populaire par champion"""
        pass

    def liste_champion(self, stat, sens):
        pass
