from unittest import TestCase, TextTestRunner, TestLoader

from dao.champion_dao import ChampionDao
from business_object.tools.champion import Champion


class TestChampionDAO(TestCase):
    def test_find_by_id(self):
        # GIVEN
        champion_id = 27

        # WHEN
        champion_object = ChampionDao().find_by_id(champion_id)
        champion_name = champion_object.name

        # THEN
        self.assertIsInstance(champion_object, Champion)
        self.assertEqual(champion_name, "Singed")


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestChampionDAO))
