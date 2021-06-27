#ifndef ANTYLOPA_H
#define ANTYLOPA_H
#include "Zwierze.h"

class Antylopa : public Zwierze
{
    public:
        Antylopa();
        ~Antylopa();
        void rysowanie();
        virtual void akcja()
        {
            int kierunek_X = (rand() % 3 - 1) * 2;
            int kierunek_Y = (rand() % 3 - 1) * 2;
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
                kolizja(swiat->swiat_tablica[new_X][new_Y]);
        }

    protected:

    private:
};

#endif // ANTYLOPA_H
