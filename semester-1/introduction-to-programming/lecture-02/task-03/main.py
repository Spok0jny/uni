liczby = []
iloscDodatnich = iloscUjemnych = iloscZer = iloscParzystych = 0


print("Podaj ilosc elementow tablicy: ")
iloscElementow = int(input())

for i in range(iloscElementow):
    print(f"Wpisz liczbe calkowita na pozycje {i}: ")
    liczby.append(int(input()))

for i in range(iloscElementow):
    if liczby[i] > 0:
        iloscDodatnich += 1
    if liczby[i] < 0:
        iloscUjemnych += 1
    if liczby[i] == 0:
        iloscZer += 1
    if liczby[i] % 2 == 0:
        iloscParzystych += 1

print(f"Ilosc elementow dodatnich: {iloscDodatnich}")
print(f"Ilosc elementow ujemnych: {iloscUjemnych}")
print(f"Ilosc zer: {iloscZer}")
print(f"Ilosc elementow parzystych: {iloscParzystych}")

suma = iloscDodatnich + iloscUjemnych + iloscZer

if suma == iloscElementow:
    print("Suma dodatnich, zer i ujemnych jest rowna liczbie elementow tablicy")
else:
    print("nie")