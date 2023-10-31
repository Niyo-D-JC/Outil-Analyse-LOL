
class TestUser(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        liste_matchs = [
            MatchJoueur(1, "Joueur1", "Champion1", ["Item1", "Item2"], "Top", "Team1", StatJoueur(5, 2, 3, 100, 20, 50, 4.0, True)),
            MatchJoueur(2, "Joueur1", "Champion1", ["Item1", "Item2"], "Top", "Team1", StatJoueur(8, 3, 5, 120, 25, 60, 4.0, True)),
            MatchJoueur(3, "Joueur1", "Champion1", ["Item1", "Item2"], "Top", "Team1", StatJoueur(3, 1, 2, 80, 15, 40, 6.0, False)),
            # ... Ajoutez d'autres matchs selon vos besoins
        ]

        # WHEN
        total_wins, total_games = UserService().get_global_WR(liste_matchs)

        # THEN
        self.assertEqual(total_wins, 2)
        self.assertEqual(total_games, 3)

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestUser)
    )
