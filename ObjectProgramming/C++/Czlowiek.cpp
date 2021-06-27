#include "Czlowiek.h"

Czlowiek::Czlowiek()
{
    sila = 5;
    inicjatywa = 4;
}

void Czlowiek::akcja()
{
    int new_X = polozenie.x + swiat->kierunek_X;
    int new_Y = polozenie.y + swiat->kierunek_Y;

    if(new_X < 0) new_X = 0;
    if(new_Y < 0) new_Y = 0;
    if(new_X >= swiat->Get_X()) new_X = swiat->Get_X();
    if(new_Y >= swiat->Get_Y()) new_Y = swiat->Get_Y();

    if(swiat->swiat_tablica[new_X][new_Y] == NULL)
    {
        polozenie.x = new_X;
        polozenie.y = new_Y;
    }
    else
    {
        if(swiat->swiat_tablica[new_X][new_Y]->Get_ID() == 7)
            swiat->swiat_tablica[new_X][new_Y]->kolizja(this);
        kolizja(swiat->swiat_tablica[new_X][new_Y]);
    }
}

void Czlowiek::kolizja(Organizm *przeciwnik)
{

}

void Czlowiek::rysowanie()
{
    cout << "C";
}
