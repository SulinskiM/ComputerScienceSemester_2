#!/usr/bin/env python

"""
Projekt 2: Python

author: Maciej Suliński
indeks: 176083
"""

import wx
import pyautogui
from Swiat import Swiat
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

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.symulacja = Swiat()
        self.symulacja.generuj_swiat()
        self.InitUI()

    def InitUI(self):
        txt1 = "Obecna tura: " + str(self.symulacja.tura)
        self.font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
        self.pnl = wx.Panel(self)
        self.col = wx.Colour(0, 0, 0)

        distros = ['Wilk', 'Owca', 'Lis', 'Żółw', 'Antylopa', 'Cyber owca', 'Trawa', 'Mlecz', 'Guarana', 'Wilcze jagody', 'Barszcz sosnowskiego']
        cb = wx.ComboBox(self, pos=(1000, 100), choices=distros, style=wx.CB_READONLY)
        rysuj = wx.Button(self, label='Nowa tura', pos=(850, 150))
        up = wx.Button(self, label='Góra', pos=(850, 180))
        down = wx.Button(self, label='Dół', pos=(850, 210))
        left = wx.Button(self, label='Lewo', pos=(850, 240))
        right = wx.Button(self, label='Prawo', pos=(850, 270))
        specjalna = wx.Button(self, label='Specjalna', pos=(850, 300))
        nowe_stworzenie = wx.Button(self, label='Dodaj', pos=(850, 350))
        zapisz = wx.Button(self, label='Zapisz', pos=(850, 500))
        wczytaj = wx.Button(self, label='Wczytaj', pos=(850, 530))
        cb.Bind(wx.EVT_COMBOBOX, self.Dodaj_organizm)

        self.st1 = wx.StaticText(self, label=txt1, style=wx.ALIGN_LEFT, pos=(1000, 200))
        self.kierunek = wx.StaticText(self, label='LEWO', style=wx.ALIGN_LEFT, pos=(20, 50))

        self.st1.SetFont(self.font)
        self.cpnl = []
        
        if self.symulacja.tryb == 1:
            self.Bind(wx.EVT_PAINT, self.OnPaint)
        else:
            self.Bind(wx.EVT_PAINT, self.OnPaint2)

        if self.symulacja.tryb == 1:
            rysuj.Bind(wx.EVT_BUTTON, self.OnPaint)
        else:
            rysuj.Bind(wx.EVT_BUTTON, self.OnPaint2)

        up.Bind(wx.EVT_BUTTON, self.OnMove1)
        down.Bind(wx.EVT_BUTTON, self.OnMove2)
        left.Bind(wx.EVT_BUTTON, self.OnMove3)
        right.Bind(wx.EVT_BUTTON, self.OnMove4)
        self.Bind(wx.EVT_BUTTON, self.OnMove4)
        specjalna.Bind(wx.EVT_BUTTON, self.specjalna_umiejetnosc)
        zapisz.Bind(wx.EVT_BUTTON, self.symulacja.zapisz_swiat_do_pliku)
        wczytaj.Bind(wx.EVT_BUTTON, self.wczytaj_stan_symulacji)
        nowe_stworzenie.Bind(wx.EVT_BUTTON, self.new)

        self.SetSize((1250, 1000))
        self.SetTitle('Symulacja wirtualnego świata')
        self.Centre()
        self.Show(True)
        self.wyswietl_statystyki()

    def wczytaj_stan_symulacji(self, event):
        self.symulacja.wczytaj_swiat_z_pliku()
        self.Pomaluj()

    def Dodaj_organizm(self, e):
        print("Na pozycji: x = " + str(self.aktualnyx) + " y = " + str(self.aktualnyy) + "dodano " + e.GetString())

        gatunek = e.GetString()
        a = self.aktualnyx
        b = self.aktualnyy

        if gatunek == "Wilk":
            self.symulacja.organizmy.append(Wilk(self.symulacja, a, b))
        if gatunek == "Owca":
            self.symulacja.organizmy.append(Owca(self.symulacja, a, b))
        if gatunek == "Lis":
            self.symulacja.organizmy.append(Lis(self.symulacja, a, b))
        if gatunek == "Żółw":
            self.symulacja.organizmy.append(Zolw(self.symulacja, a, b))
        if gatunek == "Antylopa":
            self.symulacja.organizmy.append(Antylopa(self.symulacja, a, b))
        if gatunek == "Cyber owca":
            self.symulacja.organizmy.append(CyberOwca(self.symulacja, a, b))
        if gatunek == "Trawa":
            self.symulacja.organizmy.append(Trawa(self.symulacja, a, b))
        if gatunek == "Mlecz":
            self.symulacja.organizmy.append(Mlecz(self.symulacja, a, b))
        if gatunek == "Guarana":
            self.symulacja.organizmy.append(Guarana(self.symulacja, a, b))
        if gatunek == "Wilcze jagody":
            self.symulacja.organizmy.append(WilczeJagody(self.symulacja, a, b))
        if gatunek == "Barszcz sosnowskiego":
            self.symulacja.organizmy.append(BarszczSosnowskiego(self.symulacja, a, b))

        self.Pomaluj()

    def new(self, e):
        self.aktualnyx = 10
        self.aktualnyy = 10
        wielkosc = 20
        dc = wx.ClientDC(self)
        dc.SetBrush(wx.Brush('#795548'))
        dc.SetPen(wx.Pen("#CC0000"))

        dc.DrawRectangle(self.aktualnyx * wielkosc , self.aktualnyy * wielkosc, wielkosc, wielkosc)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def new2(self):
        self.Pomaluj()
        wielkosc = 20
        dc = wx.ClientDC(self)
        dc.SetBrush(wx.Brush('#795548'))
        dc.SetPen(wx.Pen("#CC0000"))

        dc.DrawRectangle(self.aktualnyx * wielkosc , self.aktualnyy * wielkosc, wielkosc, wielkosc)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def OnKeyDown(self, event):

        keycode = event.GetKeyCode()

        if keycode == wx.WXK_LEFT:
            self.kierunek_w_lewo()

        elif keycode == wx.WXK_RIGHT:
            self.kierunek_w_prawo()

        elif keycode == wx.WXK_DOWN:
            self.kierunek_w_dol()

        elif keycode == wx.WXK_SPACE:
            self.new2()

        elif keycode == wx.WXK_UP:
            self.kierunek_w_gore()
        
        self.new2()

    def kierunek_w_lewo(self):
        self.aktualnyx = self.aktualnyx - 1

    def kierunek_w_prawo(self):
        self.aktualnyx = self.aktualnyx + 1

    def kierunek_w_dol(self):
        self.aktualnyy = self.aktualnyy + 1

    def kierunek_w_gore(self):
        self.aktualnyy = self.aktualnyy - 1

    def Pomaluj(self):
        dc = wx.ClientDC(self)
        wielkosc = 20
        
        dc.SetBrush(wx.Brush(wx.Colour(47, 79, 79)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 250, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(188, 143, 143)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 280, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(218, 165, 32)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 310, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(162, 42, 42)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 340, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(255, 248, 220)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 370, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(25, 25, 112)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 400, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(50, 205, 50)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 430, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(192, 192, 192)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 460, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(255, 69, 0)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 490, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(123, 104, 238)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 520, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(244, 164, 96)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 550, 30, 30)

        dc.SetBrush(wx.Brush('#795548'))
        dc.SetPen(wx.Pen("#000000"))

        for y in range(0, self.symulacja.wymiarY):
            for x in range(0, self.symulacja.wymiarX):
                dc.DrawRectangle(x * wielkosc , y * wielkosc, wielkosc, wielkosc)
        for i in self.symulacja.organizmy:
            dc.SetBrush(wx.Brush(i.kolor()))
            dc.SetPen(wx.Pen("#000000"))
            x = i.polozenieX
            y = i.polozenieY
            dc.DrawRectangle(x * wielkosc , y * wielkosc, wielkosc, wielkosc)
        self.wyswietl_statystyki_aktualne()

    def OnPaint2(self, e):
        self.symulacja.nowa_tura()
        self.st1.Label = "Obecna tura: " + str(self.symulacja.tura)
        self.st1.SetFont(self.font)
        self.st1.Refresh()

        dc = wx.ClientDC(self)

        dc.SetBrush(wx.Brush(wx.Colour(47, 79, 79)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 250, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(188, 143, 143)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 280, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(218, 165, 32)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 310, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(162, 42, 42)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 340, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(255, 248, 220)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 370, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(25, 25, 112)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 400, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(50, 205, 50)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 430, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(192, 192, 192)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 460, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(255, 69, 0)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 490, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(123, 104, 238)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 520, 30, 30)

        dc.SetBrush(wx.Brush(wx.Colour(244, 164, 96)))
        dc.SetPen(wx.Pen("#000000"))
        dc.DrawRectangle(970, 550, 30, 30)

        dc.SetBrush(wx.Brush('#795548'))
        dc.SetPen(wx.Pen("#000000"))

        wielkosc = 20
        wysokosc = int(wielkosc*0.8660254038)

        for i in self.symulacja.organizmy:
            i.mozliwoscruchu = 1
        for i in self.symulacja.organizmy:
            if i.mozliwoscruchu == 1:
                i.akcja()

        for y in range(0, self.symulacja.wymiarY):
            for x in range(0, self.symulacja.wymiarX):
                dc.DrawRectangle(x * wielkosc , y * wielkosc, wielkosc, wielkosc)
        for i in self.symulacja.organizmy:
            dc.SetBrush(wx.Brush(i.kolor()))
            dc.SetPen(wx.Pen("#000000"))
            x = i.polozenieX
            y = i.polozenieY
            dc.DrawRectangle(x * wielkosc , y * wielkosc, wielkosc, wielkosc)
        self.wyswietl_statystyki_aktualne()

    def OnPaint(self, e):

        pozycja = pyautogui.position()
        print(pozycja)
        self.symulacja.nowa_tura()
        self.st1.Label = "Obecna tura: " + str(self.symulacja.tura)
        self.st1.SetFont(self.font)
        self.st1.Refresh()

        dc = wx.ClientDC(self)
        dc.SetBrush(wx.Brush('#795548'))
        dc.SetPen(wx.Pen("#000000"))

        wielkosc = 15
        wysokosc = int(wielkosc*0.8660254038)

        for i in self.symulacja.organizmy:
            i.mozliwoscruchu = 1
        for i in self.symulacja.organizmy:
            if i.mozliwoscruchu == 1:
                i.akcja()

        for y in range(0, self.symulacja.wymiarY):
            for x in range(0, self.symulacja.wymiarX):
                if y % 2 == 0:
                    dc.DrawPolygon(((2*wysokosc*x, wielkosc/2 + 2*wielkosc + 1.5*wielkosc*y), (wysokosc + 2*wysokosc*x, 2*wielkosc + 1.5*wielkosc*y), (2*wysokosc + 2*wysokosc*x, wielkosc/2 + 2*wielkosc + 1.5*wielkosc*y), 
                    (2*wysokosc + 2*wysokosc*x, wielkosc/2 + wielkosc + 2*wielkosc + 1.5*wielkosc*y), (wysokosc + 2*wysokosc*x, 2*wielkosc + 2*wielkosc + 1.5*wielkosc*y), (2*wysokosc*x, wielkosc/2 + wielkosc + 2*wielkosc + 1.5*wielkosc*y)))
                else:
                    dc.DrawPolygon(((wysokosc + 2*wysokosc*x, wielkosc*2.5 + 1.5*wielkosc*y), (2*wysokosc + 2*wysokosc*x, 2*wielkosc + 1.5*wielkosc*y), (3*wysokosc + 2*wysokosc*x, wielkosc*2.5 + 1.5*wielkosc*y), 
                    (3*wysokosc + 2*wysokosc*x, wielkosc*3.5 + 1.5*wielkosc*y), (2*wysokosc + 2*wysokosc*x, 4*wielkosc + 1.5*wielkosc*y), (wysokosc + 2*wysokosc*x, wielkosc*3.5 + 1.5*wielkosc*y)))
    
        for i in self.symulacja.organizmy:
            dc.SetBrush(wx.Brush(i.kolor()))
            dc.SetPen(wx.Pen("#000000"))
            x = i.polozenieX
            y = i.polozenieY
            if y % 2 == 0:
                 dc.DrawPolygon(((2*wysokosc*x, wielkosc/2 + 2*wielkosc + 1.5*wielkosc*y), (wysokosc + 2*wysokosc*x, 2*wielkosc + 1.5*wielkosc*y), (2*wysokosc + 2*wysokosc*x, wielkosc/2 + 2*wielkosc + 1.5*wielkosc*y), 
                 (2*wysokosc + 2*wysokosc*x, wielkosc/2 + wielkosc + 2*wielkosc + 1.5*wielkosc*y), (wysokosc + 2*wysokosc*x, 2*wielkosc + 2*wielkosc + 1.5*wielkosc*y), (2*wysokosc*x, wielkosc/2 + wielkosc + 2*wielkosc + 1.5*wielkosc*y)))
            else:
                 dc.DrawPolygon(((wysokosc + 2*wysokosc*x, wielkosc*2.5 + 1.5*wielkosc*y), (2*wysokosc + 2*wysokosc*x, 2*wielkosc + 1.5*wielkosc*y), (3*wysokosc + 2*wysokosc*x, wielkosc*2.5 + 1.5*wielkosc*y), 
                 (3*wysokosc + 2*wysokosc*x, wielkosc*3.5 + 1.5*wielkosc*y), (2*wysokosc + 2*wysokosc*x, 4*wielkosc + 1.5*wielkosc*y), (wysokosc + 2*wysokosc*x, wielkosc*3.5 + 1.5*wielkosc*y)))
        self.wyswietl_statystyki_aktualne()


    def OnMove1(self, event):
        for i in self.symulacja.organizmy:
            if type(i) == Czlowiek:
                i.kierunek = 2
        self.kierunek.SetLabel('GÓRA')

    def OnMove2(self, event):
        for i in self.symulacja.organizmy:
            if type(i) == Czlowiek:
                i.kierunek = 3
        self.kierunek.SetLabel('DÓŁ')

    def OnMove3(self, event):
        for i in self.symulacja.organizmy:
            if type(i) == Czlowiek:
                i.kierunek = 0
        self.kierunek.SetLabel('LEWO')

    def OnMove4(self, event):
        for i in self.symulacja.organizmy:
            if type(i) == Czlowiek:
                i.kierunek = 1
        self.kierunek.SetLabel('PRAWO')

    def specjalna_umiejetnosc(self, event):
        for i in self.symulacja.organizmy:
            if type(i) == Czlowiek:
                i.kierunek = 1

    def wyswietl_statystyki(self):
        wilki = "Wilki: " + str(self.symulacja.policz_gatunek(Wilk))
        self.st10 = wx.StaticText(self, label=wilki, style=wx.ALIGN_LEFT, pos=(1000, 250))
        self.st10.SetFont(self.font)

        owce = "Owce: " + str(self.symulacja.policz_gatunek(Owca))
        self.st11 = wx.StaticText(self, label=owce, style=wx.ALIGN_LEFT, pos=(1000, 280))
        self.st11.SetFont(self.font)

        lisy = "Lisy: " + str(self.symulacja.policz_gatunek(Lis))
        self.st12 = wx.StaticText(self, label=lisy, style=wx.ALIGN_LEFT, pos=(1000, 310))
        self.st12.SetFont(self.font)

        zolwie = "Żółwie: " + str(self.symulacja.policz_gatunek(Zolw))
        self.st13 = wx.StaticText(self, label=zolwie, style=wx.ALIGN_LEFT, pos=(1000, 340))
        self.st13.SetFont(self.font)

        antylopa = "Antylopa: " + str(self.symulacja.policz_gatunek(Antylopa))
        self.st14 = wx.StaticText(self, label=antylopa, style=wx.ALIGN_LEFT, pos=(1000, 370))
        self.st14.SetFont(self.font)

        cyber = "Cyber owce: " + str(self.symulacja.policz_gatunek(Owca))
        self.st15 = wx.StaticText(self, label=cyber, style=wx.ALIGN_LEFT, pos=(1000, 400))
        self.st15.SetFont(self.font)

        trawa = "Trawa: " + str(self.symulacja.policz_gatunek(Trawa))
        self.st16 = wx.StaticText(self, label=trawa, style=wx.ALIGN_LEFT, pos=(1000, 430))
        self.st16.SetFont(self.font)

        mlecze = "Mlecze: " + str(self.symulacja.policz_gatunek(Mlecz))
        self.st17 = wx.StaticText(self, label=mlecze, style=wx.ALIGN_LEFT, pos=(1000, 460))
        self.st17.SetFont(self.font)

        guarana = "Guarana: " + str(self.symulacja.policz_gatunek(Guarana))
        self.st18 = wx.StaticText(self, label=guarana, style=wx.ALIGN_LEFT, pos=(1000, 490))
        self.st18.SetFont(self.font)

        jagody = "Wilcze jagody: " + str(self.symulacja.policz_gatunek(WilczeJagody))
        self.st19 = wx.StaticText(self, label=jagody, style=wx.ALIGN_LEFT, pos=(1000, 520))
        self.st19.SetFont(self.font)

        barszcz = "Barszcz sosnowskiego: " + str(self.symulacja.policz_gatunek(BarszczSosnowskiego))
        self.st110 = wx.StaticText(self, label=barszcz, style=wx.ALIGN_LEFT, pos=(1000, 550))
        self.st110.SetFont(self.font)
        
    def wyswietl_statystyki_aktualne(self):
        self.st10.Label = "Wilki: " + str(self.symulacja.policz_gatunek(Wilk))
        self.st10.Refresh()
        self.st10.SetFont(self.font)

        self.st11.Label = "Owce: " + str(self.symulacja.policz_gatunek(Owca))
        self.st11.Refresh()
        self.st11.SetFont(self.font)

        self.st12.Label = "Lisy: " + str(self.symulacja.policz_gatunek(Lis))
        self.st12.Refresh()
        self.st12.SetFont(self.font)
        
        self.st13.Label = "Żółwie: " + str(self.symulacja.policz_gatunek(Zolw))
        self.st13.Refresh()
        self.st13.SetFont(self.font)
        
        self.st14.Label = "Antylopy: " + str(self.symulacja.policz_gatunek(Antylopa))
        self.st14.Refresh()
        self.st14.SetFont(self.font)
        
        self.st15.Label = "Cyber owce: " + str(self.symulacja.policz_gatunek(CyberOwca))
        self.st15.Refresh()
        self.st15.SetFont(self.font)
        
        self.st16.Label = "Trawa: " + str(self.symulacja.policz_gatunek(Trawa))
        self.st16.Refresh()
        self.st16.SetFont(self.font)
        
        self.st17.Label = "Mlecz: " + str(self.symulacja.policz_gatunek(Mlecz))
        self.st17.Refresh()
        self.st17.SetFont(self.font)
        
        self.st18.Label = "Guarana: " + str(self.symulacja.policz_gatunek(Guarana))
        self.st18.Refresh()
        self.st18.SetFont(self.font)
        
        self.st19.Label = "Wilcze jagidy: " + str(self.symulacja.policz_gatunek(WilczeJagody))
        self.st19.Refresh()
        self.st19.SetFont(self.font)
        
        self.st110.Label = "Barszcz sosnowskiego: " + str(self.symulacja.policz_gatunek(BarszczSosnowskiego))
        self.st110.Refresh()
        self.st110.SetFont(self.font)

    def RysujSwiat(self, e):

        self.symulacja.nowa_tura()
        self.st1.Label = "Obecna tura: " + str(self.symulacja.tura)
        self.st1.SetFont(self.font)
        self.st1.Refresh()

        for i in self.symulacja.organizmy:
            i.mozliwoscruchu = 1
        for i in self.symulacja.organizmy:
            if i.mozliwoscruchu == 1:
                i.akcja()
            self.col = i.kolor()
            polozenie = i.polozenieY + self.symulacja.wymiarX*i.polozenieX

        self.Pomaluj()
        self.wyswietl_statystyki_aktualne()

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()