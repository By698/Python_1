prime_numbers = []
for i in range(101):
    prime_numbers.append(True)
number = 2
while number ** 2 <= 100:
    if prime_numbers[number]:
        for i in range(number * 2, 101, number):
            prime_numbers[i] = False
    number += 1

for i in range(2, 101):
    if prime_numbers[i]:
        print(i)
