#include "BarszczSosnowskiego.h"

BarszczSosnowskiego::BarszczSosnowskiego()
{
    sila = 10;
}

void BarszczSosnowskiego::rysowanie()
{
    cout << "B";
}

void BarszczSosnowskiego::akcja()
{
    if(swiat->swiat_tablica[polozenie.x - 1][polozenie.y - 1] != NULL)
    if(swiat->swiat_tablica[polozenie.x - 1][polozenie.y - 1]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x - 1, polozenie.y - 1);

    if(swiat->swiat_tablica[polozenie.x - 1][polozenie.y] != NULL)
    if(swiat->swiat_tablica[polozenie.x - 1][polozenie.y]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x - 1, polozenie.y);

    if(swiat->swiat_tablica[polozenie.x - 1][polozenie.y + 1] != NULL)
    if(swiat->swiat_tablica[polozenie.x - 1][polozenie.y + 1]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x - 1, polozenie.y + 1);

    if(swiat->swiat_tablica[polozenie.x][polozenie.y - 1] != NULL)
    if(swiat->swiat_tablica[polozenie.x][polozenie.y - 1]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x, polozenie.y - 1);

    if(swiat->swiat_tablica[polozenie.x][polozenie.y + 1] != NULL)
    if(swiat->swiat_tablica[polozenie.x][polozenie.y + 1]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x, polozenie.y + 1);

    if(swiat->swiat_tablica[polozenie.x + 1][polozenie.y - 1] != NULL)
    if(swiat->swiat_tablica[polozenie.x + 1][polozenie.y - 1]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x + 1, polozenie.y - 1);

    if(swiat->swiat_tablica[polozenie.x + 1][polozenie.y] != NULL)
    if(swiat->swiat_tablica[polozenie.x + 1][polozenie.y]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x + 1, polozenie.y);

    if(swiat->swiat_tablica[polozenie.x + 1][polozenie.y + 1] != NULL)
    if(swiat->swiat_tablica[polozenie.x + 1][polozenie.y + 1]->Get_ID() <= 4)
        swiat->usun_zwierze(polozenie.x + 1, polozenie.y + 1);

    int szansza = rand() % 100;

    if(szansza >= MIN_SZANSZA)
    {
        int kierunek_X = rand() % 3 - 1;
        int kierunek_Y = rand() % 3 - 1;
        if(swiat->swiat_tablica[polozenie.x + kierunek_X][polozenie.y + kierunek_Y] == NULL)
            swiat->nowe_stworzenie(polozenie.x + kierunek_X, polozenie.y + kierunek_Y, id);
    }
}

void BarszczSosnowskiego::kolizja(Organizm *organizm)
{

}
