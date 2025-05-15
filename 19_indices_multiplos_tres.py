numeros = [4, 9, 12, 5, 7, 18, 21, 25, 30]

for i, number in enumerate(numeros):
    if(number % 3 == 0):
        print(f"{i}: {number}")