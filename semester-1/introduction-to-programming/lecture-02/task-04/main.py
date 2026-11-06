rozmiar_tablicy = 0

while rozmiar_tablicy <= 0:
    rozmiar_tablicy = int(input("Podaj rozmiar tablicy: "))

tablica = []



for i in range(0, rozmiar_tablicy):
    nowa_wartosc = int(input(f"Podaj liczbe calkowita dla indeksu {i}: "))
    tablica.append(nowa_wartosc)

najwiekszy_element = float("-inf")
drugi_najwiekszy = float("-inf")

for element in tablica:
    if element >= najwiekszy_element:
        najwiekszy_element = element

tablica_z_jednego_elementu = True
for element in tablica:
    if element != najwiekszy_element:
        tablica_z_jednego_elementu = False
        break

if tablica_z_jednego_elementu:
    print(najwiekszy_element)
else:
    for element in tablica:
        if element >= drugi_najwiekszy and element < najwiekszy_element:
            drugi_najwiekszy = element

    print(najwiekszy_element, drugi_najwiekszy)
