
import json

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from dao.items_dao import ItemsDao
from dao.champion_dao import ChampionDao
from business_object.tools.champion import Champion
from business_object.tools.items import Item

class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    def lancer(self):
        print("Réinitialisation de la base de données")

        init_db = open("data/init_db.sql", encoding="utf-8")
        init_db_as_string = init_db.read()
        
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(init_db_as_string)


            items_json = json.load(open("data/item.json"))
            champions_json = json.load(open("data/champion.json", "r", encoding="utf-8"))

            for it in items_json["data"].keys():
                ItemsDao().creer(Item(it, items_json["data"][it]["name"]))

            for cp in champions_json["data"].keys():
                ChampionDao().creer(Champion(champions_json["data"][cp]["key"], cp))
            
        except Exception as e:
            print(e)
            raise
        return True


if __name__ == "__main__":
    ResetDatabase().lancer()