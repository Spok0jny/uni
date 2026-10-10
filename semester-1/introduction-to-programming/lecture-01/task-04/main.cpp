#include <iostream>
using namespace std;

void sprawdzTrojkat(double a, double b, double c) {
    cout<<"Testuje boki o dlugosciach: " << a << ", " << b << ", " << c << endl;

  if (a+b > c && a+c > b && b + c > a) {
      if (a == b && b == c) {
          cout<<"Rownoboczny"<<endl;
      } else if (a == b || a == c || b == c) {
          cout << "Rownoramienny"<<endl;

      } else {
          cout<<"Roznoboczny"<<endl;
      }
  } else {
      cout<<"Nie da sie zubdowac trojakta z tych bokow"<<endl;
  }

}


int main() {
    sprawdzTrojkat(3, 4, 5);     // 1. Zwykły różnoboczny
    sprawdzTrojkat(5, 5, 5);     // 2. Równoboczny
    sprawdzTrojkat(5, 5, 3);     // 3. Równoramienny
    sprawdzTrojkat(1, 2, 3);     // 4. Przypadek graniczny (1 + 2 == 3 -> nie da się)
    sprawdzTrojkat(1, 10, 12);   // 5. Nie da się zbudować (1 + 10 < 12)
    sprawdzTrojkat(0, 4, 4);     // 6. Boki zerowe bledne
    return 0;
}
