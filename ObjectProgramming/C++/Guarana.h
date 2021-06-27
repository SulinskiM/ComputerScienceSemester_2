#ifndef GUARANA_H
#define GUARANA_H
#include "Roslina.h"

class Guarana : public Roslina
{
    public:
        Guarana();
        void rysowanie();
        void kolizja(Organizm *organizm);

    protected:

    private:
};

#endif // GUARANA_H
