from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch

from services.user_service import UserService

from business_object.battle.matchjoueur import MatchJoueur
from business_object.stats.stat_joueur import StatJoueur


class TestUserService(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        liste_matchs = [
            MatchJoueur(
                1,
                "Joueur1",
                "Champion1",
                ["Item1", "Item2"],
                "Top",
                "Team1",
                StatJoueur(5, 2, 3, 100, 20, 50, 4.0, True),
            ),
            MatchJoueur(
                2,
                "Joueur1",
                "Champion1",
                ["Item1", "Item2"],
                "Top",
                "Team1",
                StatJoueur(8, 3, 5, 120, 25, 60, 4.0, True),
            ),
            MatchJoueur(
                3,
                "Joueur1",
                "Champion1",
                ["Item1", "Item2"],
                "Top",
                "Team1",
                StatJoueur(3, 1, 2, 80, 15, 40, 6.0, False),
            ),
            # ... Ajoutez d'autres matchs selon vos besoins
        ]

        # WHEN
        total_wins, total_games = UserService().get_global_WR(liste_matchs)

        # THEN
        self.assertEqual(total_wins, 2)
        self.assertEqual(total_games, 3)

    def test_get_stats_by_champ(self):
        # GIVEN
        liste_matchs = [
            MatchJoueur(
                1,
                "Joueur1",
                "Champion1",
                ["Item1", "Item2"],
                "Top",
                "Team1",
                StatJoueur(5, 2, 3, 100, 20, 50, 4.0, True),
            ),
            MatchJoueur(
                2,
                "Joueur1",
                "Champion1",
                ["Item1", "Item2"],
                "Top",
                "Team1",
                StatJoueur(8, 3, 5, 120, 25, 60, 4.0, True),
            ),
            MatchJoueur(
                3,
                "Joueur2",
                "Champion2",
                ["Item3", "Item4"],
                "Mid",
                "Team2",
                StatJoueur(3, 1, 2, 80, 15, 40, 6.0, False),
            ),
            # ... Ajoutez d'autres matchs selon vos besoins
        ]

        # WHEN
        champions_stats = UserService().get_stats_by_champ(liste_matchs)

        # THEN
        # Vérifiez les statistiques pour chaque champion
        self.assertEqual(champions_stats["Champion1"]["kills_avg"], 6.5)
        self.assertEqual(champions_stats["Champion1"]["deaths_avg"], 2.5)
        self.assertEqual(champions_stats["Champion1"]["assists_avg"], 4.0)
        self.assertEqual(champions_stats["Champion1"]["cs_avg"], 55.0)
        self.assertEqual(champions_stats["Champion1"]["nombre_de_matchs"], 2)

        self.assertEqual(champions_stats["Champion2"]["kills_avg"], 3.0)
        self.assertEqual(champions_stats["Champion2"]["deaths_avg"], 1.0)
        self.assertEqual(champions_stats["Champion2"]["assists_avg"], 2.0)
        self.assertEqual(champions_stats["Champion2"]["cs_avg"], 40.0)
        self.assertEqual(champions_stats["Champion2"]["nombre_de_matchs"], 1)

        # Ajoutez des assertions supplémentaires si nécessaire


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestUserService))
