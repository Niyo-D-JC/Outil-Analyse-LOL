from services.invite_service2 import InviteService
import math as dp

Liste_part = [
    [
        1,
        [["10", [100, 101], [1, 0, 3]], ["20", [200, 201], [1, 2, 3]]],
        [["50", [300, 301], [1, 2, 3]], ["30", [400, 401], [1, 2, 3]]],
    ],
    [
        2,
        [["30", [300, 302], [1, 2, 3]], ["20", [200, 202], [1, 2, 3]]],
        [["10", [100, 102], [1, 2, 3]], ["40", [400, 402], [1, 2, 3]]],
    ],
]


Liste_stat = ["win rate", "KDA", "pick rate", "item"]
invitsc = InviteService().stat_champion_view(
    list_partie=Liste_part, champion_id="10", stat=Liste_stat
)
print(invitsc)
"""

"""
invitlc = InviteService().liste_champion_view(
    list_partie=Liste_part, stat=Liste_stat[0], l_stat=Liste_stat[:1]
)
print(invitlc)
"""

"""
liste_match = [
    [
        1,
        10,
        10,
        [100, 101],
        "lane",
        "team",
        ["tot_domdeal", "tot_domtake", "tot_heal", 1, 2, 3, True],
    ],
    [
        1,
        10,
        20,
        [200, 201],
        "lane",
        "team",
        ["tot_domdeal", "tot_domtake", "tot_heal", 1, 2, 3, False],
    ],
]

l = InviteService().transfo_list(liste_match)
print(l)

"""

"""

invitsi = InviteService().stat_item_view(
    list_partie=Liste_part, item_id=100, stat=Liste_stat
)
print(invitsi)

"""

"""

invitli = InviteService().liste_item_view(
    list_partie=Liste_part, stat=Liste_stat[0], l_stat=Liste_stat[:1]
)
print(invitli)
