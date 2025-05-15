numeros = [4, 9, 12, 5, 7, 18, 9, 25, 9]

n = int(input("ingresa un numero: "))
posiciones = []
count = 0

for i, number in enumerate(numeros):
    if(n == number):
        posiciones.append(i)
        count += 1

if count:
    print(f"El numero {n} aparece {count} veces, en las posciciones {posiciones}")
else:
    print(f"El numero {n} no aparece en el array")