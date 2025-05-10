numbers = [5, 12, 7, 18, 4, 20, 2]

limit = int(input("ingrese el limite: "))

filter_numbers = []

for number in numbers:
    if (number > limit):
        filter_numbers.append(number)

if filter_numbers:
    print(filter_numbers)
else:
    print(f"No hay numeros mayores a {limit}")
