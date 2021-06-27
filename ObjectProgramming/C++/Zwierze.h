#ifndef ZWIERZE_H
#define ZWIERZE_H
#include "Organizm.h"
#include <iostream>

using namespace std;

class Zwierze : public Organizm{
    public:
        Zwierze();
        ~Zwierze();
        virtual void akcja();

    protected:

    private:
};

#endif // ZWIERZE_H
