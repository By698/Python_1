bigger_number = int(input("Podaj większą liczbę: "))
smaller_number = int(input("Podaj mniejszą liczbę: "))

while smaller_number != 0:
    _ = bigger_number % smaller_number
    bigger_number = smaller_number
    smaller_number = _
print(bigger_number)
