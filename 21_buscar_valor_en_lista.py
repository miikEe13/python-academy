numeros = [4, 9, 12, 5, 7, 18, 21, 25, 30]

n = int(input("Ingresa un numero: "))
found = False

for i, number in enumerate(numeros):
    if(n == number):
        print(f"{n} si esta en la lista")
        found = True
        break
if not found:
    print(f"{n } no esta en la lista")