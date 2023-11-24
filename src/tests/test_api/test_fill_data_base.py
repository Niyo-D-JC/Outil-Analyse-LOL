from unittest import TestCase, TextTestRunner, TestLoader

from api.fill_data_base import FillDataBase
from business_object.user.joueur import Joueur


class TestFillDataBase(TestCase):
    def test_get_puuid(self):
        # GIVEN
        name = "KC NEXT ADKING"

        # WHEN
        puuid = FillDataBase().get_puuid(name)

        # THEN
        self.assertIsInstance(puuid, str)
        self.assertEqual(
            puuid,
            "T-pbiOyzw1nTq0vBzFH-XnS8S21T1nnOjxe8IX3Xk7hpjOPXqkdOVOdydV_-38BWCI3vdNrFGoBjow",
        )

    def test_get_summonerId(self):
        # GIVEN
        puuid = "T-pbiOyzw1nTq0vBzFH-XnS8S21T1nnOjxe8IX3Xk7hpjOPXqkdOVOdydV_-38BWCI3vdNrFGoBjow"

        # WHEN
        summonerid = FillDataBase().get_summonerId(puuid)

        # THEN
        self.assertEqual(summonerid, "rkhZb_0UNx-2yicNGyooxhqixmJhKzpVAA4an3IxCDinS0NT")

    def test_get_tier(self):
        # GIVEN
        name = "Hifoly"

        # WHEN
        puuid = FillDataBase().get_puuid(name)
        tier = FillDataBase().get_tier(puuid)

        # THEN
        self.assertEqual(tier, "BRONZE")

    def test_get_matchlist(self):
        # GIVEN
        joueur = Joueur(
            "T-pbiOyzw1nTq0vBzFH-XnS8S21T1nnOjxe8IX3Xk7hpjOPXqkdOVOdydV_-38BWCI3vdNrFGoBjow",
            "KC NEXT ADKING",
            "CHALLNGER",
        )

        # WHEN
        list_match = FillDataBase().get_matchlist(joueur, 0, 7)

        # THEN
        self.assertEqual(len(list_match), 7)
        self.assertIsInstance(list_match, list)

    def test_reqLimit(self):
        # GIVEN
        url = "https://url-bidon.com"

        # WHEN
        response = FillDataBase().reqLimit(url)

        # THEN
        self.assertIsNone(response)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestFillDataBase))
