#include <iostream>
using namespace std;

int main() {
    cout << "Podaj liczbę X:" << endl;
    double x;
    cin >> x;

    if (x<0) {
      cout <<  (x*x) + 1 <<endl;
    }
    else if (x>=0 && x <10) {
        cout << 2*x <<endl;
    } else if (x >= 10) {
        cout << x - 5 <<endl;
    }

    return 0;
}
