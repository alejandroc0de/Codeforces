cases = int(input())

listaResultados = []

possible = True
contador = 0

for _ in range(cases):
    n = int(input())
    lista = list(map(int,input().split()))
    for i in range(n-2,-1,-1):
        while lista[i]>=lista[i+1]:
            if (lista[i]==0):
                possible = False
                break
            else:
                lista[i]=lista[i]//2
                contador = contador + 1
        if not possible:
            break
    if possible:
        listaResultados.append(contador)
    else:
        listaResultados.append(-1)

for resultado in listaResultados:
    print(resultado)