n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

# Determinar el mayor
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# Determinar el menor
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

# Calcular promedio
avg = (n1 + n2 + n3) / 3

# Salida
print("El mayor:", mayor)
print("El menor:", menor)
print("Promedio de los tres:", avg)
