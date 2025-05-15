n1 = int(input("n1: "))
n2 = int(input("n2: "))
sum = 0
multiples = []  # Creamos una lista vacía

for i in range(n1, n2+1):
    if i % 3 == 0:
        sum = sum +  i
        multiples.append(i)
        
# Imprimir los resultados
print(f"Números múltiplos de 3 encontrados: {multiples}")
print(f"Suma total: {sum}")