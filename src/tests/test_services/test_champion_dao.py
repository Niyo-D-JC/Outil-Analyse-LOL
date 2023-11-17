import unittest
from unittest.mock import patch, MagicMock
from dao.champion_dao import ChampionDao

class TestChampionDao(unittest.TestCase):

    @patch('dao.db_connection.DBConnection')
    def test_creer_method(self, mock_db_connection):
        champion_dao = ChampionDao()

        # Création d'un champion factice pour les tests
        fake_champion = MagicMock()
        fake_champion.tools_id = 1
        fake_champion.name = "Fake Champion"

        # Définition du comportement simulé de la connexion à la base de données
        mock_db_instance = mock_db_connection.return_value
        mock_db_instance.connection.__enter__.return_value.cursor.return_value.execute.return_value = None

        # Appel de la méthode à tester
        result = champion_dao.creer(fake_champion)

        # Vérification que la méthode renvoie True pour la création réussie
        self.assertTrue(result)

    @patch('dao.db_connection.DBConnection')
    def test_find_by_id_method(self, mock_db_connection):
        champion_dao = ChampionDao()

        # Définition d'un champion factice pour les tests
        champion_id = 1
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {"name": "Fake Champion"}

        # Définition du comportement simulé de la connexion à la base de données
        mock_db_instance = mock_db_connection.return_value
        mock_db_instance.connection.__enter__.return_value.cursor.return_value.execute.return_value = mock_cursor

        # Appel de la méthode à tester
        result = champion_dao.find_by_id(champion_id)

        # Vérification que la méthode renvoie un objet Champion
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Fake Champion")

    @patch('dao.db_connection.DBConnection')
    def test_get_all_order_method(self, mock_db_connection):
        champion_dao = ChampionDao()

        # Définition d'un jeu de résultats factice pour les tests
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Champion1", 10, 0.7), ("Champion2", 20, 0.6)]

        # Définition du comportement simulé de la connexion à la base de données
        mock_db_instance = mock_db_connection.return_value
        mock_db_instance.connection.__enter__.return_value.cursor.return_value.execute.return_value = mock_cursor

        # Appel de la méthode à tester
        result = champion_dao.get_all_order()

        # Vérification que la méthode renvoie un jeu de résultats non vide
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
