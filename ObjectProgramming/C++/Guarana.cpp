#include "Guarana.h"

Guarana::Guarana()
{
    sila = 0;
}

void Guarana::rysowanie()
{
    cout << "G";
}
void Guarana::kolizja(Organizm *organizm)
{
    organizm->zwieksz_sile(3);
}
