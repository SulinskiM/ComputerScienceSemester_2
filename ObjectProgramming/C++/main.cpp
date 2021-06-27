#include <iostream>
#include <cstdlib>
#include <ctime>
#include "Swiat.h"
#include <conio.h>

using namespace std;

int main()
{
    unsigned char znak;

    srand( time( NULL ) );
    Swiat *kraina;
    kraina = new Swiat;
    char opcja;

    kraina->nowe_stworzenie(3, 3, 10);

    while(znak != '0')
    {
        kraina->wyswietl_menu();
        do
        {
            znak = getch();
        }while(znak != '1' && znak != '2' && znak != '3' && znak != '4' && znak != '0' && znak != 's');

        switch(znak)
        {
        case '1':
            system( "cls" );
            kraina->zaladuj_z_pliku();
            break;
        case '2':
            cout << "Symulacja kolejnej rundy!" << endl;
            system( "cls" );
            kraina->pobierz_kierunek_czlowieka();
            kraina->wykonajTure();
            kraina->rysujSwiat();
            break;
        case '3':
            system( "cls" );
            kraina->zaladuj_z_pliku();
            break;
        case '4':
            system( "cls" );
            cout << "Statystyki:" << endl;
            kraina->statystyki();
            break;
        case 's':
            cout << "Aktywacja specjalnej umiejetnosci" << endl;
            kraina->statystyki();
            break;
        }
    }

    delete kraina;

    return 0;
}
