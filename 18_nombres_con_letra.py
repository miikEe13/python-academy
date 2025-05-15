names = ["Miguel", "Ana", "Luis", "Sofía", "Carlos", "Marta", "Mario"]
char = str(input("Ingresa una letra: "))

for i, name in enumerate(names):
    if(name.lower().startswith(char.lower())):
        print(f"{i}: {name}")