#ifndef BARSZCZSOSNOWSKIEGO_H
#define BARSZCZSOSNOWSKIEGO_H
#include "Roslina.h"

class BarszczSosnowskiego : public Roslina
{
    public:
        BarszczSosnowskiego();
        void rysowanie();
        void akcja();
        void kolizja(Organizm *organizm);

    protected:

    private:
};

#endif // BARSZCZSOSNOWSKIEGO_H
