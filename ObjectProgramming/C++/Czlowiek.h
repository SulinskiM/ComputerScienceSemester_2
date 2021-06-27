#ifndef CZLOWIEK_H
#define CZLOWIEK_H
#include "Zwierze.h"
#include <conio.h>

class Czlowiek : public Zwierze
{
    public:
        Czlowiek();
        void rysowanie();
        void akcja();
        void kolizja(Organizm *przeciwnik);
    protected:

    private:
};

#endif // CZLOWIEK_H
