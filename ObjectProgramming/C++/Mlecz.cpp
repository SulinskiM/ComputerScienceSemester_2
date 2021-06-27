#include "Mlecz.h"

Mlecz::Mlecz()
{
    sila = 0;
}

void Mlecz::rysowanie()
{
    cout << "M";
}

void Mlecz::akcja()
{
    for(int i=0; i<3; i++)
    {
        int szansza = rand() % 100;
        if(szansza >= MIN_SZANSZA)
        {
            int kierunek_X = rand() % 3 - 1;
            int kierunek_Y = rand() % 3 - 1;
            if(swiat->swiat_tablica[polozenie.x + kierunek_X][polozenie.y + kierunek_Y] == NULL)
            {
                swiat->nowe_stworzenie(polozenie.x + kierunek_X, polozenie.y + kierunek_Y, id);
            }
        }
    }
}
