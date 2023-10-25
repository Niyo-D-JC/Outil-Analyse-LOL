from abc import ABC, abstractmethod


class VueAbstraite(ABC):
    def __init__(self, message=""):
        self.message = message
        with open("./src/graphical_assets/banner.txt", "r") as banner :
            ban = banner.read()
            self.message = ban + "\n\n\n" + "\t"*4 + self.message
    def nettoyer_console(self):
        for i in range(1):
            print("")

    def afficher(self) -> None:
        """Echappe un grand espace dans le terminal pour simuler le changement de page de l'application"""
        self.nettoyer_console()
        print(self.message)
        print()

    @abstractmethod
    def choisir_menu(self):
        pass