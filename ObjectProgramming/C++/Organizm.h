#ifndef ORGANIZM_H
#define ORGANIZM_H

#include "Swiat.h"
#include <iostream>
#include <fstream>

using namespace std;

struct punkt
{
    int x;
    int y;
};

class Swiat;

class Organizm
{
    public:
        bool ruch;
        Organizm();
        ~Organizm();
        virtual void akcja() = 0;
        virtual void rysowanie() = 0;
        void kolizja(Organizm *przeciwnik);
        void new_polozenie(int x, int y);
        punkt polozenie;
        Swiat* swiat;
        void Set_Swiat(Swiat *sw);
        void Set_ID(int numer);
        void Set_wiek(int WIEK);
        int Get_inicjatywa();
        int Get_ID();
        void zwieksz_wiek();
        void zwieksz_sile(int value);
        void wypisz();

    protected:
        int sila;
        int inicjatywa;
        int id;
    private:
        int wiek = 0;
};

#endif // ORGANIZM_H
