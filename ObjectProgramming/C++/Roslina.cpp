#include "Roslina.h"

Roslina::Roslina()
{

}

void Roslina::akcja()
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
