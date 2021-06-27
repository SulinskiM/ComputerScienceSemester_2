#include <iostream>
#include <string>
using namespace std;
struct Element
{
    Element* XOR = NULL;
    int value;
};
struct Straznik
{
    Element* next = NULL;
    Element* aktualny = NULL;
    Element* prev = NULL;
};
struct Lista
{
    Element* poczatek = NULL;
    Element* koniec = NULL;
    Straznik aktualny;
};
Element* XOR(Element* a, Element* b)
{
    return (Element*)((uintptr_t)(a) ^ (uintptr_t)(b));
}
void XOR_wypisz_aktualny(Lista& lista)
{
    if (lista.aktualny.aktualny == NULL)
        cout << "NULL" << endl;
    else cout << lista.aktualny.aktualny->value << endl;
}
void XOR_wypisz_nastepny(Lista& lista)
{
    Element* bufor;
    if (lista.aktualny.aktualny == NULL)
        cout << "NULL" << endl;
    else
    {
        if (lista.aktualny.next == NULL)
        {
            lista.aktualny.aktualny = lista.poczatek;
            lista.aktualny.next = lista.poczatek->XOR;
            lista.aktualny.prev = NULL;
        }
        else
        {
            bufor = lista.aktualny.aktualny;
            lista.aktualny.aktualny = lista.aktualny.next;
            lista.aktualny.prev = bufor;
            lista.aktualny.next = XOR(lista.aktualny.aktualny->XOR, bufor);
        }
        cout << lista.aktualny.aktualny->value << endl;
    }
}
void ustaw_straznika(Lista* lista, Element* a, Element* b, Element* c)
{
    lista->aktualny.aktualny = a;
    lista->aktualny.prev = b;
    lista->aktualny.next = c;
}
void XOR_wypisz_poprzedni(Lista& lista)
{
    Element* bufor;
    if (lista.aktualny.aktualny == NULL)
        cout << "NULL" << endl;
    else
    {
        if (lista.aktualny.prev == NULL)
            ustaw_straznika(&lista, lista.koniec, lista.koniec->XOR, NULL);
        else
        {
            bufor = lista.aktualny.aktualny;
            lista.aktualny.aktualny = lista.aktualny.prev;
            lista.aktualny.prev = XOR(lista.aktualny.aktualny->XOR, bufor);
            lista.aktualny.next = bufor;
        }
        cout << lista.aktualny.aktualny->value << endl;
    }
}

void XOR_dodaj_wartosc_koniec(Lista& lista, int wartosc)
{
    Element* add = new Element;
    add->value = wartosc;
    add->XOR = XOR(NULL, NULL);

    if (lista.poczatek == NULL)
    {
        lista.poczatek = add;
        lista.koniec = add;
        ustaw_straznika(&lista, add, NULL, NULL);
    }
    else
    {
        if (lista.koniec == lista.aktualny.aktualny)
            lista.aktualny.next = add;
        add->XOR = XOR(NULL, lista.koniec);
        lista.koniec->XOR = XOR(add, lista.koniec->XOR);
        lista.koniec = add;
    }
}

void XOR_dodaj_wartosc_poczatek(Lista& lista, int wartosc)
{
    Element* add = new Element;
    add->value = wartosc;
    add->XOR = XOR(NULL, NULL);
    if (lista.poczatek == NULL)
    {
        lista.aktualny.aktualny = add;
        lista.poczatek = add;
        lista.koniec = add;
    }
    else
    {
        if (lista.poczatek == lista.aktualny.aktualny)
            lista.aktualny.prev = add;
        add->XOR = XOR(NULL, lista.poczatek);
        lista.poczatek->XOR = XOR(add, lista.poczatek->XOR);
        lista.poczatek = add;
    }
}

void XOR_dodaj_wartosc_aktualny(Lista& lista, int wartosc)
{
    Element* add = new Element;
    add->value = wartosc;
    if (lista.aktualny.aktualny == NULL)
    {
        lista.aktualny.aktualny = add;
        lista.poczatek = add;
        lista.koniec = add;
    }
    else
    {
        if (lista.aktualny.prev == NULL)
            XOR_dodaj_wartosc_poczatek(lista, wartosc);
        else
        {
            add->XOR = XOR(lista.aktualny.prev, lista.aktualny.aktualny);
            lista.aktualny.prev->XOR = XOR(lista.aktualny.prev->XOR, lista.aktualny.aktualny);
            lista.aktualny.prev->XOR = XOR(lista.aktualny.prev->XOR, add);
            lista.aktualny.aktualny->XOR = XOR(lista.aktualny.aktualny->XOR, lista.aktualny.prev);
            lista.aktualny.aktualny->XOR = XOR(lista.aktualny.aktualny->XOR, add);
            lista.aktualny.prev = add;
        }
    }
}
void XOR_wypisz_liste_od_poczatku(Lista lista)
{
    Element* poprzedni = NULL;
    Element* aktualny = lista.poczatek;
    Element* bufor;
    if (aktualny != NULL)
    {
        while (aktualny != lista.koniec)
        {
            cout << aktualny->value << " ";
            bufor = aktualny;
            aktualny = XOR(poprzedni, aktualny->XOR);
            poprzedni = bufor;
        }
        cout << aktualny->value << " " << endl;
    }
    else cout << "NULL" << endl;
}
void XOR_wypisz_liste_od_konca(Lista lista)
{
    Element* poprzedni = NULL;
    Element* aktualny = lista.koniec;
    Element* bufor;
    if (aktualny != NULL)
    {
        while (aktualny != lista.poczatek)
        {
            cout << aktualny->value << " ";
            bufor = aktualny;
            aktualny = XOR(poprzedni, aktualny->XOR);
            poprzedni = bufor;
        }
        cout << aktualny->value << " " << endl;
    }
    else cout << "NULL" << endl;
}
void XOR_usun_poczatek(Lista& lista)
{
    Element* usuwany = lista.poczatek;
    if (lista.poczatek != NULL)
    {
        if (lista.poczatek->XOR == NULL)
        {
            lista.poczatek = NULL;
            lista.koniec = NULL;
            ustaw_straznika(&lista, NULL, NULL, NULL);
        }
        else
        {
            if (lista.aktualny.aktualny == lista.poczatek)
                ustaw_straznika(&lista, lista.koniec, lista.koniec->XOR, NULL);
            lista.poczatek->XOR->XOR = XOR(lista.poczatek->XOR->XOR, lista.poczatek);
            lista.poczatek = lista.poczatek->XOR;
        }
        delete usuwany;
    }
}
void XOR_usun_koniec(Lista& lista)
{
    Element* usuwany = lista.koniec;
    if (lista.koniec != NULL)
    {
        if (lista.koniec->XOR == NULL)
        {
            lista.poczatek = NULL;
            lista.koniec = NULL;
            ustaw_straznika(&lista, NULL, NULL, NULL);
        }
        else
        {
            if (lista.aktualny.aktualny == lista.koniec)
            {
                lista.aktualny.aktualny = lista.koniec->XOR;
                lista.aktualny.next = NULL;
                lista.aktualny.prev = XOR(lista.aktualny.aktualny->XOR, lista.koniec);
            }
            if (lista.aktualny.aktualny == lista.koniec->XOR)
                lista.aktualny.next = NULL;
            lista.koniec->XOR->XOR = XOR(lista.koniec->XOR->XOR, lista.koniec);
            lista.koniec = lista.koniec->XOR;
        }
        delete usuwany;
    }
}
void XOR_usun_aktualny(Lista& lista)
{
    Element* bufor;
    Element* usuwany = lista.aktualny.aktualny;
    if (lista.aktualny.aktualny != NULL)
    {
        if (lista.aktualny.prev == NULL && lista.aktualny.next == NULL)
        {
            lista.poczatek = NULL;
            lista.koniec = NULL;
            ustaw_straznika(&lista, NULL, NULL, NULL);
            delete usuwany;
        }
        else
        {
            if (lista.aktualny.next == NULL)
                XOR_usun_koniec(lista);
            else if (lista.aktualny.prev == NULL)
                XOR_usun_poczatek(lista);
            else
            {
                bufor = lista.aktualny.aktualny;
                lista.aktualny.prev->XOR = XOR(lista.aktualny.prev->XOR, lista.aktualny.aktualny);
                lista.aktualny.prev->XOR = XOR(lista.aktualny.prev->XOR, lista.aktualny.next);
                lista.aktualny.next->XOR = XOR(lista.aktualny.next->XOR, lista.aktualny.aktualny);
                lista.aktualny.next->XOR = XOR(lista.aktualny.next->XOR, lista.aktualny.prev);
                lista.aktualny.aktualny = lista.aktualny.prev;
                if (lista.poczatek == lista.aktualny.prev)
                    lista.aktualny.prev = NULL;
                else
                    lista.aktualny.prev = XOR(lista.aktualny.aktualny->XOR, bufor);
                lista.aktualny.next = bufor;
                delete usuwany;
            }
        }
    }
}

void XOR_usun_wartosci(Lista& lista, int liczba)
{
    Element* poprzedni = NULL;
    Element* nastepny = NULL;
    Element* aktualny = lista.poczatek;
    Element* bufor;
        while (aktualny != lista.koniec)
        {
            if (aktualny->value == liczba)
            {
                nastepny = XOR(aktualny->XOR, poprzedni);
                if (poprzedni != NULL && nastepny != NULL)
                {
                    poprzedni->XOR = XOR(poprzedni->XOR, aktualny);
                    poprzedni->XOR = XOR(poprzedni->XOR, nastepny);
                    nastepny->XOR = XOR(nastepny->XOR, aktualny);
                    nastepny->XOR = XOR(nastepny->XOR, poprzedni);
                }
                else if (poprzedni == NULL)
                    XOR_usun_poczatek(lista);
                else if (nastepny == NULL)
                    XOR_usun_koniec(lista);
                aktualny = nastepny;
            }
            else
            {
                bufor = aktualny;
                aktualny = XOR(poprzedni, aktualny->XOR);
                poprzedni = bufor;
            }
        }
        if(lista.koniec->value == liczba)
            XOR_usun_koniec(lista);
}
int main()
{
    Lista lista;
    int liczba;
    string komenda;
    while (cin >> komenda)
        if (komenda == "ACTUAL")
            XOR_wypisz_aktualny(lista);
        else if (komenda == "NEXT")
            XOR_wypisz_nastepny(lista);
        else if (komenda == "PREV")
            XOR_wypisz_poprzedni(lista);
        else if (komenda == "PRINT_FORWARD")
            XOR_wypisz_liste_od_poczatku(lista);
        else if (komenda == "PRINT_BACKWARD")
            XOR_wypisz_liste_od_konca(lista);
        else if (komenda == "DEL_BEG")
            XOR_usun_poczatek(lista);
        else if (komenda == "DEL_END")
            XOR_usun_koniec(lista);
        else if (komenda == "DEL_ACT")
            XOR_usun_aktualny(lista);
        else
        {
            cin >> liczba;
            if (komenda == "ADD_BEG")
                XOR_dodaj_wartosc_poczatek(lista, liczba);
            else if (komenda == "ADD_END")
                XOR_dodaj_wartosc_koniec(lista, liczba);
            else if (komenda == "ADD_ACT")
                XOR_dodaj_wartosc_aktualny(lista, liczba);
            else if (komenda == "DEL_VAL")
                XOR_usun_wartosci(lista, liczba);
        }
}