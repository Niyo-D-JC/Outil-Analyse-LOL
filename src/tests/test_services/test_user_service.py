from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch

from services.user_service import UserService

from business_object.battle.matchjoueur import MatchJoueur
from business_object.stats.stat_joueur import StatJoueur
from business_object.tools.champion import Champion
from business_object.tools.lane import Lane


class TestUserService(TestCase):
    def test_get_global_WR(self):
        # GIVEN

        Match_Object1 = MatchJoueur(
            match_id=None,
            joueur=None,
            champion=Champion(1, "Annie"),
            items=None,
            lane=Lane(3, "MIDDLE"),
            team=None,
            stat_joueur=StatJoueur(
                total_damage_dealt=2000,
                total_damage_take=1500,
                total_heal=800,
                kills=10,
                deaths=2,
                assists=5,
                creeps=200,
                total_gold=10000,
                win=True,
            ),
        )

        Match_Object2 = MatchJoueur(
            match_id=None,
            joueur=None,
            champion=Champion(42, "Corki"),
            items=None,
            lane=Lane(3, "MIDDLE"),
            team=None,
            stat_joueur=StatJoueur(
                total_damage_dealt=2000,
                total_damage_take=1500,
                total_heal=800,
                kills=10,
                deaths=2,
                assists=5,
                creeps=200,
                total_gold=10000,
                win=False,
            ),
        )

        Liste_Match_User = [Match_Object1, Match_Object2]

        # WHEN
        total_wins, total_games = UserService().get_global_WR(Liste_Match_User)

        # THEN
        self.assertEqual(total_wins, 1)
        self.assertEqual(total_games, 2)

    def test_get_stats_by_lane(self):
        # GIVEN
        Match_Object1 = MatchJoueur(
            match_id=None,
            joueur=None,
            champion=Champion(1, "Annie"),
            items=None,
            lane=Lane(3, "MIDDLE"),
            team=None,
            stat_joueur=StatJoueur(
                total_damage_dealt=2000,
                total_damage_take=1500,
                total_heal=800,
                kills=10,
                deaths=5,
                assists=3,
                creeps=200,
                total_gold=10000,
                win=True,
            ),
        )

        Match_Object2 = MatchJoueur(
            match_id=None,
            joueur=None,
            champion=Champion(1, "Annie"),
            items=None,
            lane=Lane(3, "MIDDLE"),
            team=None,
            stat_joueur=StatJoueur(
                total_damage_dealt=2000,
                total_damage_take=1500,
                total_heal=800,
                kills=3,
                deaths=2,
                assists=9,
                creeps=160,
                total_gold=10000,
                win=True,
            ),
        )

        Match_Object3 = MatchJoueur(
            match_id=None,
            joueur=None,
            champion=Champion(1, "Annie"),
            items=None,
            lane=Lane(3, "MIDDLE"),
            team=None,
            stat_joueur=StatJoueur(
                total_damage_dealt=1800,
                total_damage_take=1200,
                total_heal=700,
                kills=2,
                deaths=8,
                assists=6,
                creeps=180,
                total_gold=9500,
                win=False,
            ),
        )

        Liste_Match_User = [Match_Object1, Match_Object2, Match_Object3]

        # WHEN
        champions_stats = UserService().get_stats_by_lane(Liste_Match_User)

        # THEN
        self.assertEqual(champions_stats["MIDDLE"]["Annie"]["kills_avg"], 5.0)
        self.assertEqual(champions_stats["MIDDLE"]["Annie"]["deaths_avg"], 5.0)
        self.assertEqual(champions_stats["MIDDLE"]["Annie"]["assists_avg"], 6.0)
        self.assertEqual(champions_stats["MIDDLE"]["Annie"]["cs_avg"], 180.0)
        self.assertEqual(
            champions_stats["MIDDLE"]["Annie"]["winrate"], 0.6666666666666666
        )
        self.assertEqual(champions_stats["MIDDLE"]["Annie"]["nombre_de_matchs"], 3)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestUserService))
