#ifndef WILCZEJAGODY_H
#define WILCZEJAGODY_H
#include "Roslina.h"
#include <iostream>

using namespace std;

class WilczeJagody : public Roslina
{
    public:
        WilczeJagody();
        void rysowanie();
        void kolizja(Organizm *organizm);

    protected:

    private:
};

#endif // WILCZEJAGODY_H
