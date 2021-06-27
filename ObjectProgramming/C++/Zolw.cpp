#include "Zolw.h"

Zolw::Zolw()
{
    sila = 2;
    inicjatywa = 1;
}
void Zolw::akcja()
{
    int szansa = rand() % 100;

    if(szansa >= 75)
    {
        int kierunek_X = rand() % 3 - 1;
        int kierunek_Y = rand() % 3 - 1;
        int new_X = polozenie.x + kierunek_X;
        int new_Y = polozenie.y + kierunek_Y;

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
            kolizja(swiat->swiat_tablica[new_X][new_Y]);
        }
    }
}
void Zolw::rysowanie()
{
    cout << "Z";
}
