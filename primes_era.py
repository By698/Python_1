range_ = int(input("Podaj górny zakres: "))
prime_numbers = []
for i in range(range_ + 1):
    prime_numbers.append(True)
number = 2
while number ** 2 <= range_:
    if prime_numbers[number]:
        for i in range(number * 2, range_ + 1, number):
            prime_numbers[i] = False
    number += 1

for i in range(2, range_ + 1):
    if prime_numbers[i]:
        print(i)
