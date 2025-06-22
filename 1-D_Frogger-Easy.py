squares,starting,goal = map(int,input().split())
lista = []

lista = list(map(int,input().split()))

numeroActual = lista[starting-1]
contador = 0 
listaPosiciones = []
lenghtLista = len(listaPosiciones)

if (numeroActual == goal):
    print("magic")
    print(0)
    exit(0)

while numeroActual != goal:
    if (numeroActual>=0):
        PosicionActual = lista[starting-1]+starting
        starting = PosicionActual
        numeroActual = lista[starting-1]
        flag = listaPosiciones.__contains__(PosicionActual)
        if (flag==True):
            contador = contador +1 
            print("cycle")
            print(contador)
            exit(0)
        listaPosiciones.append(PosicionActual)
        contador = contador +1

    if(numeroActual<0):
        PosicionActual = starting - abs(lista[starting-1])
        starting = PosicionActual
        numeroActual = lista[starting-1]
        flag = listaPosiciones.__contains__(PosicionActual)
        if (flag == True):
            contador = contador +1
            print("cycle")
            print(contador)
            exit(0)
        listaPosiciones.append(PosicionActual)
        contador = contador + 1
print("magic")
print(contador)


## the logic is good, now we are just missing what happens whne the frog goes left or right
# maybe with a len or idk 