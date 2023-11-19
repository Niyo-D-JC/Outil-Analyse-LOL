import unittest
from unittest.mock import patch, MagicMock
import os
import sys
champion_dao_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'dao'))
sys.path.insert(0, champion_dao_path)
from dao.champion_dao import ChampionDao
from business_object.tools.champion import Champion

class TestChampionDao(unittest.TestCase):
    def setUp(self):
        self.mock_champion = Champion(champion_id=1, name="TestChampion")

    @patch('dao.champion_dao.DBConnection')
    def test_creer_champion(self, mock_db_connection):
        champion_dao = ChampionDao()
        mock_cursor = MagicMock()
        mock_cursor.__enter__.return_value.execute.return_value = None
        mock_db_connection.return_value.connection.__enter__.return_value.cursor.return_value = mock_cursor
        result = champion_dao.creer(self.mock_champion)
        self.assertTrue(result)

    @patch('dao.champion_dao.DBConnection')
    def test_find_by_id(self, mock_db_connection):
        champion_dao = ChampionDao()
        mock_cursor = MagicMock()
        mock_cursor.__enter__.return_value.fetchone.return_value = {"name": "TestChampion"}
        mock_db_connection.return_value.connection.__enter__.return_value.cursor.return_value = mock_cursor
        champion = champion_dao.find_by_id(1)
        self.assertIsNotNone(champion)
        self.assertEqual(champion.name, "TestChampion")

    @patch('dao.champion_dao.DBConnection')
    def test_get_all_order(self, mock_db_connection):
        champion_dao = ChampionDao()
        mock_cursor = MagicMock()
        mock_cursor.__enter__.return_value.fetchall.return_value = [("Champion1", 10, 0.6), ("Champion2", 5, 0.4)]
        mock_db_connection.return_value.connection.__enter__.return_value.cursor.return_value = mock_cursor
        result = champion_dao.get_all_order()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
