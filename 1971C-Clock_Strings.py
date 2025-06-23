#Accepted

cases = int(input())


listas = []
for i in range (cases):
    contador = 0
    a,b,c,d = map(int, input().split())


    parA = [a,b]
    parB = [c,d]

    lista = []

    parA.sort()
    primero = parA[0]
    segundo = parA[1]
    parB.sort()


    for primero in range(primero,segundo+1):
        lista.append(primero)

    for i in parB:
        if i in lista:
            contador = contador +1
    if (contador==2):
        listas.append("NO")
    if(contador==0):
        listas.append("NO")
    if(contador==1):
        listas.append("YES")


for z in listas:
    print(z)