#include "Swiat.h"
#include <iostream>
#include "Wilk.h"
#include "Owca.h"
#include "Lis.h"
#include "Zolw.h"
#include "Antylopa.h"
#include "Trawa.h"
#include "Mlecz.h"
#include "Guarana.h"
#include "WilczeJagody.h"
#include "BarszczSosnowskiego.h"
#include "Czlowiek.h"
#include <fstream>

using namespace std;

const int ILOSC_ORGANIZMOW = 10;
const int ILOSC_STWORZEN = 30;

void Swiat::wyswietl_menu()
{
    cout << "1. Wczytaj stan gry z pliku" << endl;
    cout << "2. Kolejna runda" << endl;
    cout << "3. Zapisz stan symulacji do pliku" << endl;
    cout << "4. Wyswietl statystyki" << endl;
    cout << "0. Koniec symulacji (automatyczny zapis do pliku auto.txt)" << endl;
}

void Swiat::zaladuj_z_pliku()
{
    cout << "Podaj nazwe pliku do wczytania: ";
    string nazwa;
    cin >> nazwa;
    wejscie.open(nazwa);

    wejscie >> tura;
    wejscie >> wymiar_X >> wymiar_Y;
    int zwierze, x, y, wiek;

    while(wejscie >> zwierze >> x >> y >> wiek)
    {
        nowe_stworzenie(x, y, zwierze);
        organizmy.back()->Set_wiek(wiek);
    }
}

void Swiat::zapisz_do_pliku()
{
    cout << "Podaj nazwe pliku do zapisania: ";
    string nazwa;
    cin >> nazwa;

    cout << nazwa << endl;

    wyjscie_nazwa.open(nazwa);

    wyjscie_nazwa << tura;
    wyjscie_nazwa << wymiar_X << wymiar_Y;

    for(int i = 0; i < organizmy.size(); i++)
        organizmy[i]->wypisz();

    wyjscie_nazwa.close();
}

Swiat::Swiat()
{
    cout << "Podaj wymiar X planszy: ";
    cin >> wymiar_Y;
    cout << "Podaj wymiar Y planszy: ";
    cin >> wymiar_X;

    for(int i=0; i<ILOSC_STWORZEN; i++)
        this->nowe_stworzenie();
}

void Swiat::usun_zwierze(int a, int b)
{
    if(swiat_tablica[a][b] != NULL)
    {
        for(int i=0; i < organizmy.size(); i++)
        {
            if(swiat_tablica[a][b] == organizmy[i])
                organizmy.erase(organizmy.begin() + i);
        }
        swiat_tablica[a][b] = NULL;
    }
}
void Swiat::Zwieksz_ture()
{
    tura++;
}

void Swiat::rysujSwiat()
{
    cout << "TURA: " << tura << endl;
    for(int j=0; j<wymiar_Y+1; j++)
        cout << "_";
    cout << endl;
    for(int i=0; i<wymiar_X; i++)
    {
        cout << "|";
        for(int j=0; j<wymiar_Y; j++)
        {
            if(swiat_tablica[i][j] != NULL)
                swiat_tablica[i][j]->rysowanie();
            else
                cout << " ";
        }
        cout << "|" << endl;
    }
    for(int j=0; j<wymiar_Y+1; j++)
        cout << "_";
    cout << endl;
}

void Swiat::nowe_stworzenie()
{
    Organizm *stworzenie;
    int a, b, zwierze;
    zwierze = rand() % ILOSC_ORGANIZMOW;
    a = rand() % this->Get_X();
    b = rand() % this->Get_Y();
    if(swiat_tablica[a][b] == NULL)
    {
        switch(zwierze)
        {
            case 0: stworzenie = new Wilk();
            stworzenie->Set_ID(0); break;
            case 1: stworzenie = new Owca();
            stworzenie->Set_ID(1); break;
            case 2: stworzenie = new Lis();
            stworzenie->Set_ID(2); break;
            case 3: stworzenie = new Zolw();
            stworzenie->Set_ID(3); break;
            case 4: stworzenie = new Antylopa();
            stworzenie->Set_ID(4); break;
            case 5: stworzenie = new Trawa();
            stworzenie->Set_ID(5); break;
            case 6: stworzenie = new Mlecz();
            stworzenie->Set_ID(6); break;
            case 7: stworzenie = new Guarana();
            stworzenie->Set_ID(7); break;
            case 8: stworzenie = new WilczeJagody();
            stworzenie->Set_ID(8); break;
            case 9: stworzenie = new BarszczSosnowskiego();
            stworzenie->Set_ID(9); break;
        }

        stworzenie->polozenie.x = a;
        stworzenie->polozenie.y = b;
        stworzenie->Set_Swiat(this);
        organizmy.push_back(stworzenie);
        swiat_tablica[a][b] = stworzenie;
    }
}
void Swiat::statystyki()
{
    for(int i = 0; i < ILOSC_ORGANIZMOW; i++)
    {
        int licznik = 0;
        for(int j = 0; j < organizmy.size(); j++)
        {
            if(organizmy[j]->Get_ID() == i)
                licznik++;
        }
        cout << nazwy_zwierzat[i] << ": " << licznik << endl;
    }
    cout << endl;
}
void Swiat::pobierz_kierunek_czlowieka()
{
    cout << "Ruch czlowieka (kierunek poruszania sie wybierasz poprzez strzalki)" << endl;
    unsigned char znak;

    kierunek_X = 0;
    kierunek_Y = 0;

    do
    {
        znak = getch();
        if( (int)znak == 224 )
        {
            znak = getch();
            switch(znak)
            {
                case 72:
                    kierunek_X = -1;
                    kierunek_Y = 0;
                    cout << "Ruch w gore" << endl;
                break;
                case 75:
                    kierunek_X = 0;
                    kierunek_Y = -1;
                    cout << "Ruch w lewo" << endl;
                break;
                case 77:
                    kierunek_X = 0;
                    kierunek_Y = 1;
                    cout << "Ruch w prawo" << endl;
                break;
                case 80:
                    kierunek_X = 1;
                    kierunek_Y = 0;
                    cout << "Ruch w dol" << endl;
                break;
            }
        }
    }while((int)znak != 72 && (int)znak != 75 && (int)znak != 77 && (int)znak != 80);
}

void Swiat::nowe_stworzenie(int zwierze)
{
    Organizm *stworzenie;
    int a, b;
    a = rand() % this->Get_X();
    b = rand() % this->Get_Y();

    if(swiat_tablica[a][b] == NULL && a < Get_X() && b < Get_Y() && a >= 0 && b >= 0)
    {

        switch(zwierze)
        {
            case 0: stworzenie = new Wilk();
            stworzenie->Set_ID(0); break;
            case 1: stworzenie = new Owca();
            stworzenie->Set_ID(1); break;
            case 2: stworzenie = new Lis();
            stworzenie->Set_ID(2); break;
            case 3: stworzenie = new Zolw();
            stworzenie->Set_ID(3); break;
            case 4: stworzenie = new Antylopa();
            stworzenie->Set_ID(4); break;
            case 5: stworzenie = new Trawa();
            stworzenie->Set_ID(5); break;
            case 6: stworzenie = new Mlecz();
            stworzenie->Set_ID(6); break;
            case 7: stworzenie = new Guarana();
            stworzenie->Set_ID(7); break;
            case 8: stworzenie = new WilczeJagody();
            stworzenie->Set_ID(8); break;
            case 9: stworzenie = new BarszczSosnowskiego();
            stworzenie->Set_ID(9); break;
        }

        stworzenie->polozenie.x = a;
        stworzenie->polozenie.y = b;
        stworzenie->Set_Swiat(this);
        organizmy.push_back(stworzenie);
        swiat_tablica[a][b] = stworzenie;
    }
}

void Swiat::nowe_stworzenie(int a, int b, int zwierze)
{
    if(swiat_tablica[a][b] == NULL && a < Get_X() && b < Get_Y() && a >= 0 && b >= 0)
    {
        Organizm *stworzenie;

        switch(zwierze)
        {
            case 0: stworzenie = new Wilk();
            stworzenie->Set_ID(0); break;
            case 1: stworzenie = new Owca();
            stworzenie->Set_ID(1); break;
            case 2: stworzenie = new Lis();
            stworzenie->Set_ID(2); break;
            case 3: stworzenie = new Zolw();
            stworzenie->Set_ID(3); break;
            case 4: stworzenie = new Antylopa();
            stworzenie->Set_ID(4); break;
            case 5: stworzenie = new Trawa();
            stworzenie->Set_ID(5); break;
            case 6: stworzenie = new Mlecz();
            stworzenie->Set_ID(6); break;
            case 7: stworzenie = new Guarana();
            stworzenie->Set_ID(7); break;
            case 8: stworzenie = new WilczeJagody();
            stworzenie->Set_ID(8); break;
            case 9: stworzenie = new BarszczSosnowskiego();
            stworzenie->Set_ID(9); break;
            case 10: stworzenie = new Czlowiek();
            stworzenie->Set_ID(10); break;
        }

        stworzenie->polozenie.x = a;
        stworzenie->polozenie.y = b;
        stworzenie->Set_Swiat(this);
        organizmy.push_back(stworzenie);
        swiat_tablica[a][b] = stworzenie;
    }
}

void Swiat::ustaw_plansze()
{
    for(int i=0; i<wymiar_X; i++)
    {
        for(int j=0; j<wymiar_Y; j++)
        {
            swiat_tablica[i][j] = NULL;
        }
    }

    for(int i = 0; i<organizmy.size(); i++)
    {
        swiat_tablica[organizmy[i]->polozenie.x][organizmy[i]->polozenie.y] = organizmy[i];
    }
}

int Swiat::Get_X()
{
    return wymiar_X;
}

int Swiat::Get_Y()
{
    return wymiar_Y;
}

void Swiat::sortuj()
{
    Organizm *bufor;
    for(int i = 0; i < organizmy.size(); i++)
        for(int j = i; j < organizmy.size(); j++)
        {
            if(organizmy[i]->Get_inicjatywa() < organizmy[j]->Get_inicjatywa())
            {
                bufor = organizmy[i];
                organizmy[i] = organizmy[j];
                organizmy[j] = bufor;
            }
        }
}

void Swiat::wykonajTure()
{
    Zwieksz_ture();
    sortuj();
    for(int i = 0; i<organizmy.size(); i++)
    {
        if(organizmy[i]->ruch == true)
        {
            organizmy[i]->akcja();
            ustaw_plansze();
            organizmy[i]->ruch = false;
        }
    }

    for(int i = 0; i<organizmy.size(); i++)
    {
        organizmy[i]->ruch = true;
        organizmy[i]->zwieksz_wiek();
    }
}

Swiat::~Swiat()
{
    wyjscie.open("auto.txt");

    wyjscie << tura << endl;
    wyjscie << wymiar_X << " " << wymiar_Y << endl;
    for(int i=0; i<organizmy.size(); i++)
        delete organizmy[i];
    organizmy.clear();
}
