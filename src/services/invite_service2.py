class ListePartiesInvite:
    """_summary_"""

    def __init__(self):
        pass

    def transfo_list(self, liste_match):
        """transforme la liste obtenue avec le remplissage de la base de donnée en
        la liste dont nous avons besoin
        [id_game,joueur,champ,items,lane,team,[tot_domdeal,tot_domtake,tot_heal,k,d,a,win]]
        Returns:
            list: liste dans le bon format
        """
        L = []
        Ltempo = []
        for i in range(len(liste_match)):
            id_match = liste_match[i][0]
            champion = liste_match[i][2]
            liste_item = liste_match[i][3]
            kda = [liste_match[i][6][3], liste_match[i][6][4], liste_match[i][6][5]]
            win = liste_match[i][6][6]
            if id_match not in Ltempo:
                Ltempo.append(id_match)
                team1 = []
                team2 = []
                if win:
                    team1 = [[champion, liste_item, kda]]
                else:
                    team2 = [[champion, liste_item, kda]]
                L.append([id_match, team1, team2])
            else:
                for j in range(len(Ltempo)):
                    if id_match == Ltempo[j]:
                        n = j
                if win:
                    L[n][1].append([champion, liste_item, kda])
                else:
                    L[n][2].append([champion, liste_item, kda])
        return L


class InviteService:
    """_summary_"""

    def __init__(self, stat_th=["win rate", "KDA", "pick rate", "item"]):
        """_summary_"""
        self.stat_th = stat_th

    def stat_champion(self, list_partie, champion_id, stat):
        """renvoie les statistiques voulues pour un champion choisi

        Args:
            list_partie (list): liste telle que :
            [[id_match, team1=[(idchamp1,iditem1,kda1),...], team2=[(idchamp6,iditem6,kda6), ]],...]
            le vainqueur est la team 1
            champion_id (int): id du champion
            stat (list): ['win rate', 'KDA', 'pick rate', 'item']

        Returns:
            list: liste des statistiques souhaitées
        """
        s1 = 0
        s2 = 0
        kill = 0
        death = 0
        assist = 0
        frequence_item = {}  # item populaire par champion
        list_item = []
        for i in list_partie:
            for k in i[1]:
                if champion_id == k[0]:
                    for l in k[1]:
                        if l not in list_item:
                            list_item.append(l)
                            frequence_item[l] = 1
                        else:
                            frequence_item[l] += 1
                    kill += k[2][0]
                    death += k[2][1]
                    assist += k[2][2]
                    s1 += 1
                    s2 += 1
            for k in i[2]:
                if champion_id in k:
                    for l in k[1]:
                        if l not in list_item:
                            list_item.append(l)
                            frequence_item[l] = 1
                        else:
                            frequence_item[l] += 1
                    kill += k[2][0]
                    death += k[2][1]
                    assist += k[2][2]
                    s2 += 1
        wr = 100 * s1 / s2
        kill, death, assist = kill / s2, death / s2, assist / s2
        kda = [[kill, death, assist]]
        if death == 0:
            death = 1
        kda.append((kill + assist) / death)
        pr = 100 * s2 / len(list_partie)
        liste_item_f = []
        for i in frequence_item:
            liste_item_f.append((i, 100 * frequence_item[i] / s2))
        n = len(liste_item_f)
        for i in range(n):
            for j in range(0, n - i - 1):
                if liste_item_f[j][1] < liste_item_f[j + 1][1]:
                    liste_item_f[j], liste_item_f[j + 1] = (
                        liste_item_f[j + 1],
                        liste_item_f[j],
                    )
        l_tempo = [
            wr,
            kda,
            pr,
            liste_item_f,
        ]  # il faut que les éléments de l_tempo soit dans le même ordre que ceux de stat_th
        L = [str(champion_id)]
        for i in range(len(self.stat_th)):
            if self.stat_th[i] in stat:
                L.append(l_tempo[i])
            else:
                L.append(None)
        return L

    def stat_champion_view(self, list_partie, champion_id, stat):
        """_summary_

        Args:
            list_partie (_type_): _description_
            champion_id (_type_): _description_
            stat (_type_): _description_

        Returns:
            _type_: _description_
        """
        L = self.stat_champion(list_partie, champion_id, stat)
        Lf = []
        Lf.append("champion : " + str(L[0]))
        for i in range(len(self.stat_th)):
            if L[i + 1] is not None and self.stat_th[i] != "item":
                Lf.append(self.stat_th[i] + " : " + str(L[i + 1]))
            if L[i + 1] is not None and self.stat_th[i] == "item":
                Lf.append(
                    "items populaires (item, taux d'utilisation) : " + str(L[i + 1][:5])
                )
        return Lf

    def stat_item(self):
        """item populaire, champions portant cet item"""

    def is_instance_liste(self, Liste, typ):
        """_summary_

        Args:
            Liste (_type_): _description_
            typ (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not isinstance(Liste, list):
            return False
        for i in Liste:
            if not isinstance(i, typ):
                return False
        return True

    def liste_champion(
        self,
        list_partie,
        stat,
        l_stat=["win rate", "KDA", "pick rate", "item"],
        sens="decroissant",
    ):
        """_summary_

        Args:
            list_partie (list): liste telle que :
            [[id_match, team1=[(idchamp1,iditem1,kda1),...], team2=[(idchamp6,iditem6,kda6), ]],...]
            le vainqueur est la team 1
            stat (str): 'win rate', 'KDA', 'pick rate' ou "item"
            sens (str, optional): _description_. Defaults to "decroissant".
        """
        if stat not in l_stat:
            l_stat = self.stat_th
        l_champ = []
        for i in list_partie:
            for k in i[1]:
                if k[0] not in l_champ:
                    l_champ.append(k[0])
            for k in i[2]:
                if k[0] not in l_champ:
                    l_champ.append(k[0])
        L = []
        for i in l_champ:
            L.append(self.stat_champion(list_partie, i, l_stat))
        L2 = L
        for i in L:
            if isintance(i, list):
                if self.is_instance_liste(i[0], int):
                    if i[0][1] == 0:
                        i[0][1] = 1
                    i = (i[0][0] + i[0][2]) / i[0][1]
        n = 0
        for i in range(len(self.stat_th)):
            if self.stat_th[i] == stat:
                n = i + 1
        if sens == "decroissant":
            for i in range(len(L)):
                for j in range(0, len(L) - i - 1):
                    if L[j][n] < L[j + 1][n]:
                        L2[j], L2[j + 1] = L2[j + 1], L2[j]
        else:
            for i in range(len(L)):
                for j in range(0, len(L) - i - 1):
                    if L[j][n] > L[j + 1][n]:
                        L2[j], L2[j + 1] = L2[j + 1], L2[j]
        return L2

    def liste_champion_view(
        self,
        list_partie,
        stat,
        l_stat=["win rate", "KDA", "pick rate", "item"],
        sens="decroissant",
    ):
        """_summary_

        Args:
            list_partie (_type_): _description_
            stat (_type_): _description_
            l_stat (list, optional): _description_. Defaults to ["win rate", "KDA", "pick rate", "item"].
            sens (str, optional): _description_. Defaults to "decroissant".

        Returns:
            _type_: _description_
        """
        L = self.liste_champion(list_partie, stat, l_stat, sens)
        Lf = []
        for j in range(len(L)):
            Lf.append(["champion : " + str(L[j][0])])
            for i in range(len(self.stat_th)):
                if L[j][i + 1] is not None and self.stat_th[i] != "item":
                    Lf[j].append(self.stat_th[i] + " : " + str(L[j][i + 1]))
                if L[j][i + 1] is not None and self.stat_th[i] == "item":
                    Lf[j].append(
                        "items populaires (item, taux d'utilisation) : "
                        + str(L[j][i + 1][:5])
                    )
        return Lf
