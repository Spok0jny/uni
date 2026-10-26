from math import isqrt

n = int(input("Podaj liczbe calkowita:"))
counter = 0

if n < 2:
    print(f"Liczba {n} nie jest liczbą pierwszą")
else:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            counter += 1
            break

    if counter == 0:
        print("Liczba jest pierwsza")
    else:
        print("Liczba nie jest pierwsza")