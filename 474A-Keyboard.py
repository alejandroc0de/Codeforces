#accepted 900

lista = []
listaPalabra = []

letras = "qwertyuiopasdfghjkl;zxcvbnm,./"

for i in letras:
    lista.append(i)

side = input()
palabra = input()


if side == "R":
    for z in palabra:
        index = lista.index(z)
        listaPalabra.append(lista[index-1])
elif side == "L":
    for z in palabra:
        index = lista.index(z)
        listaPalabra.append(lista[index+1])

for x in listaPalabra:
    print(x,end="")