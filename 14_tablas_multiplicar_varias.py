n1 = int(input("n1: "))
n2 = int(input("n2: "))

for i in range(n1, n2+1):
    #print("tabla del", i)
    print(f"tabla del {i}")
    for j in range(1, 11):
        resultado = i * j
        #print(i, "x", j, "=", resultado)
        print(f"{i} x {j} = {resultado}")
    print("----------")
    