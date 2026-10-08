#include <iostream>
using namespace std;

int main() {

    int liczba1, liczba2,liczba3;
    cout << "Podaj 3 liczby calkowite: \n";
    cin >> liczba1 >> liczba2 >> liczba3;
    int najwieksza = liczba1;

    if (liczba2 > najwieksza) {
        najwieksza = liczba2;
    }
    if (liczba3 > najwieksza) {
        najwieksza = liczba3;
    }
    cout << "Najwieksza liczba to: " << najwieksza << endl;


    return 0;
}
