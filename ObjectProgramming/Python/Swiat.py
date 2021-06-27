from Zwierzeta import Wilk
from Zwierzeta import Owca
from Zwierzeta import Lis
from Zwierzeta import Zolw
from Zwierzeta import Antylopa
from Zwierzeta import CyberOwca
from Rosliny import Trawa
from Rosliny import Mlecz
from Rosliny import Guarana
from Rosliny import WilczeJagody
from Rosliny import BarszczSosnowskiego
from People import Czlowiek

import random

class Swiat:
    def __init__(self):
        self.wymiarX = 40
        self.wymiarY = 40
        self.tura = 0
        self.organizmy = []
        self.tryb = 1

    def wczytaj_swiat_z_pliku(self):
        filepath = "dane.txt"
        file = open(filepath, "r") 
        
        self.organizmy.clear()
        self.wymiarX = int(file.readline())
        self.wymiarY = int(file.readline())
        self.tura = int(file.readline())
        ilosc_zwierzat = int(file.readline())

        for i in range(ilosc_zwierzat):
            gatunek = int(file.readline())
            wiek = int(file.readline())
            x = int(file.readline())
            y = int(file.readline())
            inicjatywa = int(file.readline())

            if gatunek == 0:
                self.organizmy.append(Wilk(self, x, y))
            if gatunek == 1:
                self.organizmy.append(Owca(self, x, y))
            if gatunek == 2:
                self.organizmy.append(Lis(self, x, y))
            if gatunek == 3:
                self.organizmy.append(Zolw(self, x, y))
            if gatunek == 4:
                self.organizmy.append(Antylopa(self, x, y))
            if gatunek == 5:
                self.organizmy.append(CyberOwca(self, x, y))
            if gatunek == 6:
                self.organizmy.append(Trawa(self, x, y))
            if gatunek == 7:
                self.organizmy.append(Mlecz(self, x, y))
            if gatunek == 8:
                self.organizmy.append(Guarana(self, x, y))
            if gatunek == 9:
                self.organizmy.append(WilczeJagody(self, x, y))
            if gatunek == 10:
                self.organizmy.append(BarszczSosnowskiego(self, x, y))

    def zapisz_swiat_do_pliku(self, event):
        filepath = "dane.txt"
        file = open(filepath, "w") 
        file.write(str(self.wymiarX) + "\n")
        file.write(str(self.wymiarY) + "\n")
        file.write(str(self.tura) + "\n")
        file.write(str(len(self.organizmy)) + "\n")

        for i in self.organizmy:
            file.write(str(i.konwersja_na_napis()))
        file.close()

    def generuj_swiat(self):
        for i in range(200):
            a = random.randint(0, self.wymiarX - 1)
            b = random.randint(0, self.wymiarY - 1)
            gatunek =  random.randint(0, 5)

            if gatunek == 0:
                self.organizmy.append(Wilk(self, a, b))
            if gatunek == 1:
                self.organizmy.append(Owca(self, a, b))
            if gatunek == 2:
                self.organizmy.append(Lis(self, a, b))
            if gatunek == 3:
                self.organizmy.append(Zolw(self, a, b))
            if gatunek == 4:
                self.organizmy.append(Antylopa(self, a, b))
            if gatunek == 5:
                self.organizmy.append(CyberOwca(self, a, b))
            if gatunek == 6:
                self.organizmy.append(Trawa(self, a, b))
            if gatunek == 7:
                self.organizmy.append(Mlecz(self, a, b))
            if gatunek == 8:
                self.organizmy.append(Guarana(self, a, b))
            if gatunek == 9:
                self.organizmy.append(WilczeJagody(self, a, b))
            if gatunek == 10:
                self.organizmy.append(BarszczSosnowskiego(self, a, b))
        
        for i in range(50):
            a = random.randint(0, self.wymiarX - 1)
            b = random.randint(0, self.wymiarY - 1)
            gatunek =  random.randint(6, 10)

            if gatunek == 0:
                self.organizmy.append(Wilk(self, a, b))
            if gatunek == 1:
                self.organizmy.append(Owca(self, a, b))
            if gatunek == 2:
                self.organizmy.append(Lis(self, a, b))
            if gatunek == 3:
                self.organizmy.append(Zolw(self, a, b))
            if gatunek == 4:
                self.organizmy.append(Antylopa(self, a, b))
            if gatunek == 5:
                self.organizmy.append(CyberOwca(self, a, b))
            if gatunek == 6:
                self.organizmy.append(Trawa(self, a, b))
            if gatunek == 7:
                self.organizmy.append(Mlecz(self, a, b))
            if gatunek == 8:
                self.organizmy.append(Guarana(self, a, b))
            if gatunek == 9:
                self.organizmy.append(WilczeJagody(self, a, b))
            if gatunek == 10:
                self.organizmy.append(BarszczSosnowskiego(self, a, b))

        self.organizmy.append(Czlowiek(self, 20, 20))

    def policz_gatunek(self, typ):
        ilosc = 0
        for i in self.organizmy:
            if type(i) == typ:
                ilosc = ilosc + 1
        return ilosc

    def kierunek_czlowieka(self):
        for i in self.organizmy:
            if type(i) == typ:
                return i.kierunek
        return -1

    def rysuj_swiat(self):
        pass

    def nowa_roslina(self):
        self.organizmy.append(Trawa(self, 9, 9))

    def zabij_stworzenie(self, x, y):
        for i in self.organizmy:
            if i.polozenieX == x and i.polozenieY == y and i.czy_zwierze():
                self.organizmy.remove(i)

    def wolne_pole(self, x, y):
        for i in self.organizmy:
            if i.polozenieX == x and i.polozenieY == y:
                return False
        return True

    def typ_przeciwnika(self, x, y):
        for i in self.organizmy:
            if i.polozenieX == x and i.polozenieY == y:
                return type(i)

    def przeciwnik(self, x, y):
        for i in self.organizmy:
            if i.polozenieX == x and i.polozenieY == y:
                return i

    def nowa_tura(self):
        self.tura = self.tura + 1
       


    




