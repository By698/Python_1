
def pi_wal(appr_numbers):
    i = 1
    for i in range(1, appr_numbers + 1):
        result = 1
        for n in range(1, i + 1):
            result *= 2*n * 2*n / (2*n - 1) / (2*n + 1)
        print(i, result * 2)


if __name__ == '__main__':
    appr_numbers = int(input("Podaj ilość przybliżeń: "))
    pi_wal(appr_numbers)
