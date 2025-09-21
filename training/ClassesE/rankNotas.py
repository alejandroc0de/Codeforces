n = int(input("Para cuantos estudiantes quieres calcular las notas?\n"))
notas = []

for i in range(n):
    nota = int(input(f"Ingrese la nota {i+1}\n"))
    notas.append(nota)

media = sum(notas)/(len(notas))

print(f"La media es {media}")
notas.sort()

superanMedia = []

for x in notas:
    if x >= media:
        superanMedia.append(x)


print("Las notas que superan la media son: ")
print(superanMedia)