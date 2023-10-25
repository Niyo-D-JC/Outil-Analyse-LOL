"""il faut importer les donnee de toutes les parties"""

"""
class stat_champion(JoueurInTeam, Item):
    def __init__(self, id_champ, name_champ, id_item, name_item):
        Champion(self, id_champ, name_champ)
        Item(self, id_item, name_item)
"""
from business_object.services.fill_data_base import FillDataBase


class Listeparties:
    def __init__(self, match_id):
        """_summary_

        Args:
            match_id (_type_): _description_
        """
        self.match_id = match_id

    def transfo_list(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        liste_match = FillDataBase().getMatchInfo(self.match_id)
        L = []
        Ltempo = []
        for i in range(len(liste_match)):
            if liste_match[i][0] not in Ltempo:
                Ltempo.append(liste_match[i][0])
                id_match = liste_match[i][0]
                team1 = []
                team2 = []
                if liste_match[i][6][4]:
                    team1 = [
                        [liste_match[i][2], liste_match[i][3], liste_match[i][6][3]]
                    ]
                else:
                    team2 = [
                        [liste_match[i][2], liste_match[i][3], liste_match[i][6][3]]
                    ]
                L.append([id_match, team1, team2])
            else:
                id_match = liste_match[i][0]
                for j in range(len(Ltempo)):
                    if id_match == Ltempo[j]:
                        n = j
                if liste_match[i][6][4]:
                    L[n][1].append(
                        [liste_match[i][2], liste_match[i][3], liste_match[i][6][3]]
                    )
                else:
                    L[n][2].append(
                        [liste_match[i][2], liste_match[i][3], liste_match[i][6][3]]
                    )
        return L


class Invite:
    def __init__(self):
        pass

    def stat_champion(self, list_partie, champion_id, stat, division=None):
        """_summary_

        Args:
            list_partie (list): liste telle que [[id_match, team1=[(idchamp1,iditem1,kda1),...], team2=[(idchamp6,iditem6,kda6),...]],...]
            le vainqueur est la team 1
            champion_id (int): id du champion
            stat (list): ['win rate', 'KDA', 'pick rate']
            division (str): 1,2,3,4
        """
        s1 = 0
        s2 = 0
        kill = 0
        death = 0
        assist = 0
        for i in list_partie:
            for j in i[1]:
                for k in j:
                    if champion_id in k:
                        kill += k[2][0]
                        death += k[2][1]
                        assist += k[2][2]
                        s1 += 1
                        s2 += 1
            for j in i[2]:
                for k in j:
                    if champion_id in k:
                        kill += k[2][0]
                        death += k[2][1]
                        assist += k[2][2]
                        s2 += 1
        wr = s1 / s2
        kda = [kill / s2, death / s2, assist / s2]
        pr = s2 / len(list_partie)
        L = [champion_id]
        if "win rate" in stat:
            L.append(wr)
        if "KDA" in stat:
            L.append(kda)
        if "pick rate" in stat:
            L.append(pr)
        return L

    def stat_item():
        """item populaire, item populaire par champion"""
        pass

    def liste_champion(self, stat, sens):
        pass
