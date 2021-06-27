#ifndef LIS_H
#define LIS_H
#include "Zwierze.h"
#include <iostream>

using namespace std;

class Lis : public Zwierze
{
    public:
        Lis();
        virtual void rysowanie()
        {
            cout << "L";
        }
    protected:

    private:
};

#endif // LIS_H
