numbers = [5, 12, 7, 18, 4, 20, 2]

limit =  int(input("ingrese un # como limite: "))

new_list = []

sum_list = 0

for number in numbers:
    if (number > limit):
        new_list.append(number)

if new_list:
    for number in new_list:
        sum_list += number
    print(f"Números mayores a {limit}: {new_list}")
    print(f"la suma de los numeros mas grandes {sum_list}")