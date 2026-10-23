
// 1. Analiza cyfr liczbyNapisz program, który wczytuje dodatnią liczbę całkowitą i bez zamiany jej na napis:   oblicza liczbę jej cyfr,   oblicza sumę jej cyfr,   tworzy liczbę powstałą przez zapisanie cyfr w odwrotnej kolejności.   Przykładowo dla liczby 5724 program powinien podać: 4 cyfry, sumę cyfr 18 oraz odwróconą liczbę 4275.
#include <iostream>
using namespace std;

int main() {
    int liczba = 0;
    int licznik = 0;
    int suma = 0;
    int odwrocona = 0;
   while (true) {
       cout << "Podaj dodatnia liczbe calkowita \n";
       cin >> liczba;
       if (liczba > 0){ break; }
   }
    int kopia = liczba;


    while (liczba > 0) {
        int cyfra = liczba % 10;
        liczba /= 10;
        licznik++;
        suma += cyfra;
        odwrocona = (odwrocona*10)+cyfra;
    }

    cout << "Oryginalna: "<< kopia << endl;
    cout << "Liczba cyfr: "<< licznik <<endl;
    cout << "Suma: " << suma << endl;
    cout << "Odwrocona: " << odwrocona << endl;


    return 0;
}
