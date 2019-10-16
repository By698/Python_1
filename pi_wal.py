i = 1
for i in range(1, 11):
    result = 1
    for n in range(1, i + 1):
        result *= 2*n * 2*n / (2*n - 1) / (2*n + 1)
    print(i, result * 2)
