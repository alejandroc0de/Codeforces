lista = list(map(int,input().split()))

lenght = len(lista)

posicionMax = lenght-1
posicionsiguiente = lenght-1-1
print(posicionMax)
contador = 0


for i in range(lenght):
    while(lista[posicionMax-1]>lista[posicionsiguiente]):
        lista[posicionMax-1] = lista[posicionMax-1]//2
        contador = contador + 1
    posicionMax= posicionMax-1

print(lista)
print(contador)