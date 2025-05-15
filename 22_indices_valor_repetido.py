numeros = [4, 9, 12, 5, 7, 18, 9, 25, 9]
n = int(input("Ingresa un #: "))

indices = []
for i, number in enumerate(numeros):
    if(n == number):
        indices.append(i)
        
if len(indices):
    print(f"el #: {n} aparece en las posiciones: {indices}")
else:
    print(f"el numero {n} no aparece en las posiciones")