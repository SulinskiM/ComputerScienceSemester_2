from Roslina import Roslina

import random
import wx

class Trawa(Roslina):
    def kolor(self):
        return wx.Colour(50, 205, 50)
    
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 0
        self.sila = 0

    def rodzaj_organizmu(self):
        return 6

class Mlecz(Roslina):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 0
        self.sila = 0

    def kolor(self):
        return wx.Colour(192, 192, 192)

    def akcja(self):
        super().akcja()
        super().akcja()
        super().akcja()

    def szansza_na_rozmnozenie(self):
        return 95

    def rodzaj_organizmu(self):
        return 7

class Guarana(Roslina):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 0
        self.sila = 0

    def kolor(self):
        return wx.Colour(255, 69, 0)

    def kolizja(self, x, y):
        przeciwnik = self.swiat.przeciwnik(x, y)
        if przeciwnik.czy_zwierze() == True:
            przeciwnik.zwieksz_sile(3)

    def rodzaj_organizmu(self):
        return 8

class WilczeJagody(Roslina):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 0
        self.sila = 99

    def kolor(self):
        return wx.Colour(123, 104, 238)

    def kolizja(self, x, y):
        przeciwnik = self.swiat.przeciwnik(x, y)
        if przeciwnik.czy_zwierze() == True:
            self.swiat.organizmy.remove(przeciwnik)

    def rodzaj_organizmu(self):
        return 9

class BarszczSosnowskiego(Roslina):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 0
        self.sila = 10

    def akcja(self):
        a = self.polozenieX
        b = self.polozenieY
        self.swiat.zabij_stworzenie(a - 1, b - 1)
        self.swiat.zabij_stworzenie(a, b - 1)
        self.swiat.zabij_stworzenie(a + 1, b - 1)
        self.swiat.zabij_stworzenie(a - 1, b)
        self.swiat.zabij_stworzenie(a + 1, b)
        self.swiat.zabij_stworzenie(a - 1, b + 1)
        self.swiat.zabij_stworzenie(a, b + 1)
        self.swiat.zabij_stworzenie(a + 1, b + 1)
        super().akcja()

    def szansza_na_rozmnozenie(self):
        return 97

    def kolor(self):
        return wx.Colour(244, 164, 96)

    def kolizja(self, x, y):
        przeciwnik = self.swiat.przeciwnik(x, y)
        if przeciwnik.czy_zwierze() == True and type(przeciwnik) != CyberOwca:
            self.swiat.organizmy.remove(przeciwnik)

    def rodzaj_organizmu(self):
        return 10




