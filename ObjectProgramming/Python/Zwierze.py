from Organizm import Organizm

import random

class Zwierze(Organizm):
    def akcja(self):
        if self.swiat.tryb == 1:
            zmianaY = random.randint(-1,1)
            if zmianaY == 0:
                a = self.polozenieX + random.randint(-1,1)
            else:
                a = self.polozenieX + random.randint(0, 1)
            b = self.polozenieY + zmianaY
        else:
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
        if type(self) == self.swiat.typ_przeciwnika(x, y):
            a = x + 1
            b = y + 1
            if self.swiat.wolne_pole(a, b):
                if a >= 0 and a < self.swiat.wymiarX and b >= 0 and b < self.swiat.wymiarY:
                    nowestworzenie = type(self)(self.swiat, x + 1, y + 1)
                    self.swiat.organizmy.append(nowestworzenie)
        else:
            if self.sila > self.swiat.przeciwnik(x, y).sila:
                self.swiat.organizmy.remove(self.swiat.przeciwnik(x, y))
            else:
                self.swiat.organizmy.remove(self)

    def kolor(self):
        return 2

    def czy_roslina(self):
        return False

    def czy_zwierze(self):
        return True

    def czy_czlowiek(self):
        return False



