from Organizm import Organizm

import random

class Roslina(Organizm):
    def kolor(self):
        pass

    def akcja(self):
        a = self.polozenieX + random.randint(-1,1)
        b = self.polozenieY + random.randint(-1,1)
        if random.randint(0, 100) > self.szansza_na_rozmnozenie() and self.swiat.wolne_pole(a, b):
            if a >= 0 and a < self.swiat.wymiarX and b >= 0 and b < self.swiat.wymiarY:
                nowestworzenie = type(self)(self.swiat, a, b)
                self.swiat.organizmy.append(nowestworzenie)

    def czy_roslina(self):
        return True

    def czy_zwierze(self):
        return False

    def czy_czlowiek(self):
        return False

    def szansza_na_rozmnozenie(self):
        return 90


