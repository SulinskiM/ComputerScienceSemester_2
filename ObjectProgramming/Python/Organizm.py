class Organizm(object):
    def __init__(self, pochodzenie, x, y):
        self._wiek = 0;
        self._polozenieX = x
        self._polozenieY = y
        self.mozliwoscruchu = 0
        self.swiat = pochodzenie

    def konwersja_na_napis(self):
        return str(self.rodzaj_organizmu()) + "\n" + str(self._wiek) + "\n" + str(self._polozenieX) + "\n" + str(self._polozenieY) + "\n" + str(self.inicjatywa) + "\n"

    def kolor(self):
        return 1

    def czy_walczy(self, przeciwnik):
        return True

    def kolor_hex(self):
        return '#FF0033'

    @property
    def polozenieX(self):
        return self._polozenieX
    @polozenieX.setter
    def polozenieX(self, x):
        if x < 0:
            self._polozenieX = 0
        elif x >= self.swiat.wymiarX:
            self._polozenieX = self.swiat.wymiarX - 1
        else:
            self._polozenieX = x

    @property
    def polozenieY(self):
        return self._polozenieY
    @polozenieY.setter
    def polozenieY(self, y):
        if y < 0:
            self._polozenieY = 0
        elif y >= self.swiat.wymiarY:
            self._polozenieY = self.swiat.wymiarY - 1
        else:
            self._polozenieY = y

    @property
    def wiek(self):
        return self._wiek
    @wiek.setter
    def wiek(self, wiek):
        if wiek < 0:
            self._wiek = 0
        elif wiek > 100:
            self._wiek = 100
        else:
            self._wiek = wiek

    def rodzaj_organizmu(self):
        pass

    def akcja(self):
        pass

    def kolizja(self):
        pass

    def zwieksz_wiek(self):
        wiek = wiek + 1

    def zwieksz_sile(self, sila):
        self.sila = self.sila + sila

