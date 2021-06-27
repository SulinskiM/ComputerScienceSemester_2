from Organizm import Organizm

import random
import wx

class Czlowiek(Organizm):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 4
        self.sila = 20
        self.kierunek = 0
        self.tura_umiejetnosci = 0
    
    def specjalna_umiejetnosc(self):
        pass

    def rodzaj_organizmu(self):
        return 10

    def kolor(self):
        return wx.Colour(255, 0, 255)

    def kolizja(self, x, y):
        if self.sila > self.swiat.przeciwnik(x, y).sila:
           self.swiat.organizmy.remove(self.swiat.przeciwnik(x, y))
        else:
           self.swiat.organizmy.remove(self)

    def akcja(self):
        if self.kierunek == 0:
            a = self.polozenieX - 1
            b = self.polozenieY
        elif self.kierunek == 1:
            a = self.polozenieX + 1
            b = self.polozenieY
        elif self.kierunek == 2:
            a = self.polozenieX
            b = self.polozenieY - 1
        elif self.kierunek == 3:
            a = self.polozenieX
            b = self.polozenieY + 1
        
        if self.swiat.wolne_pole(a, b):
            self.polozenieX = a
            self.polozenieY = b
        else:
            self.kolizja(a,b)
            self.polozenieX = a
            self.polozenieY = b

    def pobierz_kierunek(self):
        pass

    def czy_roslina(self):
        return False

    def czy_zwierze(self):
        return False

    def czy_czlowiek(self):
        return True




