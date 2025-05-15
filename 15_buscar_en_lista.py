numbers = [5, 8, 12, 3, 7]

n1 = int(input("n1: "))

findNumber = False

for i in range(len(numbers)):
    if n1 == numbers[i]:
        findNumber = True
        
if (findNumber):
    print(f"El número {n1} SI está en la lista.")
else:
    print(f"El número {n1} No esta en la lista.")