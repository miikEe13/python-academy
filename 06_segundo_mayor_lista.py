# numeros = [10, 5, 8, 20, 15, 3, 30, 25]

# mayor = numeros[0]

# for numero in numeros:
#     if numero > mayor:
#         mayor = numero

# list_sin_mayor = []
# for numero in numeros:
#     if numero != mayor:
#         list_sin_mayor.append(numero)

# if list_sin_mayor:
#     segundo_mayor = list_sin_mayor[0]
#     for numero in list_sin_mayor:
#         if numero > segundo_mayor:
#             segundo_mayor = numero
#     print(f"El segundo mayor es: {segundo_mayor}")
# else:
#     print("No hay segundo mayor.")

numeros = [10, 5, 8, 20, 15, 3, 30, 25]

mayor = float('-inf')
segundo_mayor = float('-inf')

for numero in numeros:
    if numero > mayor:
        segundo_mayor = mayor
        mayor = numero
    elif numero > segundo_mayor and numero < mayor:
        segundo_mayor = numero

print(f"El segundo mayor número es: {segundo_mayor}")