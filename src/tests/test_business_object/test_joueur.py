from unittest import TestCase, TextTestRunner, TestLoader


from business_object.user.joueur import Joueur


class TestJoueur(TestCase):
    def test_joueur_creation(self):
        # GIVEN
        puuid = "T-pbiOyzw1nTq0vBzFH-XnS8S21T1nnOjxe8IX3Xk7hpjOPXqkdOVOdydV_-38BWCI3vdNrFGoBjow"
        name = "KC NEXT ADKING"
        tier = "CHALLENGER"

        # WHEN
        joueur = Joueur(puuid, name, tier)

        # THEN
        self.assertEqual(joueur.puuid, puuid)
        self.assertEqual(joueur.name, name)
        self.assertEqual(joueur.tier, tier)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestJoueur))
