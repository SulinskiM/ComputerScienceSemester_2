#ifndef SWIAT_H
#define SWIAT_H
#include <vector>
#include <iostream>
#include "Organizm.h"
#include <fstream>
#include <conio.h>

using namespace std;

class Organizm;

class Swiat
{
    public:
        Swiat();
        ~Swiat();
        void wykonajTure();
        void rysujSwiat();
        Organizm* swiat_tablica[100][100] = { NULL };
        int Get_X();
        int Get_Y();
        void nowe_stworzenie();
        void zapisz_stan_symulacji();
        void wczytaj_stan_symulacji();
        vector <Organizm*> organizmy;
        void nowe_stworzenie(int a, int b, int zwierze);
        void usun_zwierze(int a, int b);
        ofstream wyjscie;
        fstream wyjscie_nazwa;
        fstream wejscie;
        void wyswietl_menu();
        void nowe_stworzenie(int zwierze);
        void sortuj();
        string nazwy_zwierzat[10] = {"Wilk", "Owca", "Lis", "Zolw", "Antylopa", "Trawa", "Mlecz", "Guarana", "Wilcze jagody", "Barszcz sosnowkiego"};
        void statystyki();
        int kierunek_X = 0;
        int kierunek_Y = 0;
        void pobierz_kierunek_czlowieka();
        void zaladuj_z_pliku();
        void zapisz_do_pliku();

    protected:

    private:
        int wymiar_X;
        int wymiar_Y;
        int tura = 0;
        void Zwieksz_ture();
        void ustaw_plansze();
};

#endif // SWIAT_H
