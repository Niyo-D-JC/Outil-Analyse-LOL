"""Ce module contient la classe invité service.
Il permet de générer toutes les statistiques et les listes accessibles pour les invités.
Pour cela, on importe nos données depuis matchjoueur_dao.
"""

from dao.champion_dao import ChampionDao
from dao.items_dao import ItemsDao
import pandas as pd

class InviteService:
    def get_all_champions(self, by_winrate = False) :  
        results = ChampionDao().get_all_order()
        df = pd.DataFrame(results)
        if by_winrate : 
            df = df.sort_values(by='win_rate', ascending=False).reset_index(drop=True)
        else :
            df = df.sort_values(by='usage_frequency', ascending=False).reset_index(drop=True)
        df = df.rename(columns={
            'champion_name': 'Champion Name',
            'usage_frequency': 'Usage Frequency',
            'win_rate': 'Win Rate'
        })
        start_index = 0
        end = len(df) if len(df)<50 else 50
        while start_index < end:
            end_index = start_index + 10
            wave_df = df.iloc[start_index:end_index]
            print(wave_df)
            input("Appuyez sur Entrée pour afficher la vague suivante...")
            start_index = end_index

    def get_all_items(self, by_winrate = False) :  
        results = ItemsDao().get_all_order()
        df = pd.DataFrame(results)
        if by_winrate : 
            df = df.sort_values(by='win_rate', ascending=False).reset_index(drop=True)
        else :
            df = df.sort_values(by='usage_frequency', ascending=False).reset_index(drop=True)
        df = df.rename(columns={
            'item_name': 'Item Name',
            'usage_frequency': 'Usage Frequency',
            'win_rate': 'Win Rate'
        })
        start_index = 0
        end = len(df) if len(df)<50 else 50
        while start_index < end:
            end_index = start_index + 10
            wave_df = df.iloc[start_index:end_index]
            print(wave_df)
            input("Appuyez sur Entrée pour afficher la vague suivante...")
            start_index = end_index

if __name__ == "__main__":
    InviteService().get_all_items()