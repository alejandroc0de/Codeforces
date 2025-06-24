cases = int(input())

flag= True
listaResultados = []

for k in range(cases):
    n = input()
    lista = list(map(int,input().split()))
    flag = True
    lenght = len(lista)

    posicionMax = lenght-1
    posicionsiguiente = lenght-1-1
    contador = 0

    if (len(lista)==1):
        listaResultados.append(0)
        continue
    if (lista == sorted(lista, reverse=True)):
        listaResultados.append(-1)
        continue

    while flag:
        for i in range(lenght-1):
            if (lista[i]>=lista[i+1]):
                lista[i]= lista[i]//2
                contador = contador +1
        index = 0

        for i in range(0,lenght):
            if (lista[index]<lista[index+1]):
                index = index+1
                if (index==lenght-1):
                    listaResultados.append(contador)
                    flag=False
                    break

for j in listaResultados:
    print(j)