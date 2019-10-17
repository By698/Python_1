a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))


def prime_numbers_distribution(number):
    prime_numbers = []
    i = 2
    while i <= number:
        if number % i == 0:
            prime_numbers.append(i)
            number /= i
        else:
            i += 1
    return prime_numbers


def table_reduction(tab1, tab2):
    # first = set(tab1)
    # second = set(tab2)
    # second_without_first = second - first
    # result = tab1 + list(second_without_first)
    # return result


if __name__ == '__main__':
    primes1 = prime_numbers_distribution(a)
    primes2 = prime_numbers_distribution(b)
    print(table_reduction(primes1, primes2))
