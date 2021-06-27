from Zwierze import Zwierze

import random
import wx

class Wilk(Zwierze):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 5
        self.sila = 9

    def kolor(self):
        return wx.Colour(47, 79, 79)

    def rodzaj_organizmu(self):
        return 0

class Owca(Zwierze):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 4
        self.sila = 4

    def kolor(self):
        return wx.Colour(188, 143, 143)

    def rodzaj_organizmu(self):
        return 1

class Lis(Zwierze):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 7
        self.sila = 3

    def kolor(self):
        return wx.Colour(218, 165, 32)

    def akcja(self):
        a = self.polozenieX + random.randint(-1,1)
        b = self.polozenieY + random.randint(-1,1)
        if self.swiat.wolne_pole(a, b):
            self.polozenieX = a
            self.polozenieY = b
        else:
            if a != self.polozenieX and b != self.polozenieY:
                przeciwnik = self.swiat.przeciwnik(a, b)
                if przeciwnik.sila < self.sila:
                    self.kolizja(a,b)
                    self.polozenieX = a
                    self.polozenieY = b

    def czy_walczy(self, przeciwnik):
        if przeciwnik.sila < 5:
            return False
        else:
            return True

    def rodzaj_organizmu(self):
        return 2

class Zolw(Zwierze):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 1
        self.sila = 2

    def kolor(self):
        return wx.Colour(162, 42, 42)

    def akcja(self):
        szansza = random.randint(0, 100)
        if szansza > 75:
            super().akcja()

    def kolizja(self, x, y):
        pass

    def rodzaj_organizmu(self):
        return 3

class Antylopa(Zwierze):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 4
        self.sila = 4

    def akcja(self):
        self.polozenieX = self.polozenieX + 2*random.randint(-1,1)
        self.polozenieY = self.polozenieY + 2*random.randint(-1,1)
    
    def kolizja(self, x, y):
        szansza = random.randint(0, 100)
        if szansza > 50:
            self.akcja()

    def kolor(self):
        return wx.Colour(255, 248, 220)
    
    def rodzaj_organizmu(self):
        return 4

class CyberOwca(Owca):
    def __init__(self, pochodzenie, x, y):
        super().__init__(pochodzenie, x, y)
        self.inicjatywa = 4
        self.sila = 11

    def akcja(self):
        a = self.polozenieX + random.randint(-1,1)
        b = self.polozenieY + random.randint(-1,1)
        if self.swiat.wolne_pole(a, b):
            self.polozenieX = a
            self.polozenieY = b
        else:
            if a != self.polozenieX and b != self.polozenieY:
                self.kolizja(a,b)
                self.polozenieX = a
                self.polozenieY = b
    
    def kolizja(self, x, y):
        pass

    def kolor(self):
        return wx.Colour(25, 25, 112)

    def rodzaj_organizmu(self):
        return 5




