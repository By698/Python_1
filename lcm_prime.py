a = int(input("Podaj pierwsza liczbe"))
b = int(input("Podaj druga liczbe"))


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


def nww(a, b):
    return a*b//nwd(a, b)


print(nww(a,b))