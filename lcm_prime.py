
def prime_numbers_distribution(result):
    tab = []
    i = 2
    while result != 1:
        if result % i == 0:
            result /= i
            tab.append(i)
        else:
            i += 1
    return tab


def list_reduction(tab1, tab2):
    for n in tab1:
        for m in tab2:
            if m == n:
                tab2.remove(m)
                break
    print(tab1 + tab2)
    return tab1 + tab2


def nww(primes_list):
    result = 1
    for prime in primes_list:
        result = result * prime
    return result


if __name__ == '__main__':
    a = int(input("Podaj pierwsza liczbe: "))
    b = int(input("Podaj druga liczbe: "))

    primes_a = prime_numbers_distribution(a)
    primes_b = prime_numbers_distribution(b)
    print(primes_a)
    print(primes_b)
    reduced_list = list_reduction(primes_a, primes_b)
    print(nww(reduced_list))
