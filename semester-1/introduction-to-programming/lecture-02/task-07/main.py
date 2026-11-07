m = int(input("Podaj ilosc wierszy: "))
n = int(input("Podaj ilosc kolumn: "))

while m <= 0:
    m = int(input("Podaj poprawna ilosc wierszy: "))

while n <= 0:
    n = int(input("Podaj poprawna ilosc kolumn: "))

tablica = []

for w in range(m):
    tablica.append([])
    for k in range(n):
        tablica[w].append(int(input()))


# suma
najwieksza_suma = float("-inf")
najwiekszy_element = float("-inf")
najwiekszy_element_wiersz = 0
najwiekszy_element_kolumna = 0
wiersz_najwiekszej_sumy = 0

for indeks_wiersz, wiersz in enumerate(tablica):
    suma = 0
    for indeks_kolumna, kolumna in enumerate(wiersz):
        suma += kolumna
        if kolumna > najwiekszy_element:
            najwiekszy_element = kolumna
            najwiekszy_element_wiersz = indeks_wiersz
            najwiekszy_element_kolumna = indeks_kolumna

    if suma > najwieksza_suma:
        najwieksza_suma = suma
        wiersz_najwiekszej_sumy = indeks_wiersz
    print(f"Suma wiersza {indeks_wiersz}: {suma}")

print(f"Najwiekszy element jest w wierszu {najwiekszy_element_wiersz}, w kolumnie {najwiekszy_element_kolumna} i wynosi {najwiekszy_element}. Najwieksza suma znajduje sie w wierszu {wiersz_najwiekszej_sumy} i wynosi {najwieksza_suma}")
