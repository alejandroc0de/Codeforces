# incorrect answer, dont know why

squares,starting,goal = map(int,input().split())
lista = []

lista = list(map(int,input().split()))

numeroEnLista = lista[starting-1]
numeroEnListaAoperar = lista[starting-1]
posicionEnLista = starting


contador = 0 
listaPosiciones = []
lenghtLista = len(lista)


if (numeroEnLista == goal):
    print("magic")
    print(0)
    exit(0)


    

while numeroEnLista != goal:



    if (numeroEnListaAoperar>=0):
        posicionEnLista = posicionEnLista + numeroEnListaAoperar
        if(posicionEnLista<0):
            print("left")
            print(contador + 1)
            exit(0)
        if (posicionEnLista>lenghtLista):
            print("right")
            print(contador + 1)
            exit(0)
        numeroEnLista = lista[posicionEnLista-1]
        
        flag = listaPosiciones.__contains__(posicionEnLista)
        if (flag==True):
            contador = contador +1 
            print("cycle")
            print(contador)
            exit(0)
        listaPosiciones.append(posicionEnLista)
        contador = contador +1
        numeroEnListaAoperar = numeroEnLista
        continue



    if(numeroEnListaAoperar<0):
        posicionEnLista = posicionEnLista - abs (numeroEnListaAoperar)
        if(posicionEnLista<=0):
            print("left")
            print(contador + 1)
            exit(0)
        if (posicionEnLista>lenghtLista):
            print("right")
            print(contador + 1)
            exit(0)
        numeroEnLista = lista[posicionEnLista-1]
        flag = listaPosiciones.__contains__(posicionEnLista)
        if (flag == True):
            contador = contador +1
            print("cycle")
            print(contador)
            exit(0)
        listaPosiciones.append(posicionEnLista)
        contador = contador + 1
        numeroEnListaAoperar = numeroEnLista
        continue
print("magic")
print(contador)