numeros = [4, 9, 12, 9, 7, 18, 9, 25, 7, 4, 4]

frecuencias = {}

# Contar cuántas veces aparece cada número
for n in numeros:
    frecuencias[n] = frecuencias.get(n, 0) + 1

# Buscar el número con más apariciones
mayor = 0
numero_mas_frecuente = None

for numero, cantidad in frecuencias.items():
    if cantidad > mayor:
        mayor = cantidad
        numero_mas_frecuente = numero

# Mostrar el resultado
print(frecuencias)
print(f"El número más frecuente es {numero_mas_frecuente}, y aparece {mayor} veces.")
