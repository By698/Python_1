a = int(input("Podaj pierwsza liczbe"))
b = int(input("Podaj druga liczbe"))

tab1 = []
tab2 = []


def czyn_pierwsze(wartosc, tab):  # obliczanie czynnikow pierwszych(wartosc,tablica)
    p = 2  # dzielnik
    while wartosc != 1:
        if wartosc % p == 0:
            wartosc = wartosc / p
            tab.append(p)  # wrzucanie do odpowiedniej tablicy
        else:
            p = p + 1


def usuwanie_powtorzen():
    for n in tab1:
        for m in tab2:
            if (m == n):
                tab2.remove(m)
                break
    print(tab1 + tab2)
    return tab1 + tab2


def nww():
    zmienna = 1
    for n in usuwanie_powtorzen():
        zmienna = zmienna * n
    return zmienna


czyn_pierwsze(a, tab1)
czyn_pierwsze(b, tab2)
print(tab1)
print(tab2)
print(nww())
