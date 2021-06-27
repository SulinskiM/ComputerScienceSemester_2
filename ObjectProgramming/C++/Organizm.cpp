#include "Organizm.h"

Organizm::Organizm()
{
    ruch = false;
}

void Organizm::Set_Swiat(Swiat *sw)
{
    swiat = sw;
}

void Organizm::Set_ID(int numer)
{
    id = numer;
}

void Organizm::zwieksz_sile(int value)
{
    sila += value;
}

void Organizm::Set_wiek(int WIEK)
{
    wiek = WIEK;
}

void Organizm::new_polozenie(int x, int y)
{
    polozenie.x = x;
    polozenie.y = y;
}

int Organizm::Get_ID()
{
    return id;
}

void Organizm::kolizja(Organizm *przeciwnik)
{
    if(this->id == przeciwnik->id)
    {
        int kierunek_X = rand() % 3 - 1;
        int kierunek_Y = rand() % 3 - 1;
        if(swiat->swiat_tablica[polozenie.x + kierunek_X][polozenie.y + kierunek_Y] == NULL)
        {
            swiat->nowe_stworzenie(polozenie.x + kierunek_X, polozenie.y + kierunek_Y, id);
        }
    }
    else
    {
        if(this->sila > przeciwnik->sila)
            swiat->usun_zwierze(przeciwnik->polozenie.x, przeciwnik->polozenie.y);
        else
            swiat->usun_zwierze(polozenie.x, polozenie.y);
    }
}

void Organizm::wypisz()
{
    swiat->wyjscie << id << " " << polozenie.x << " " << polozenie.y << " " << wiek << endl;
}

int Organizm::Get_inicjatywa()
{
    return inicjatywa;
}

Organizm::~Organizm()
{
    swiat->wyjscie_nazwa << id << " " << polozenie.x << " " << polozenie.y << " " << wiek << endl;
}

void Organizm::zwieksz_wiek()
{
    wiek++;
}
