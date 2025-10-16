# Accepted

cases = int(input())
lista = []
for _ in range(cases):
    n = int(input())
    numeros = list(map(int, input().split()))
    numeros.sort()
    k = 2
    minimo = 0
    minimoGlobal = -999999
    numero1 = numeros[0]
    numero2 = numeros[1]
    minimoGlobal = abs(numero1 - numero2)

    for _ in range(k,n,2):
        numero1 = numeros[_]
        numero2 = numeros[_+1]
        minimo = abs(numero1 - numero2)
        minimoGlobal = max(minimoGlobal,minimo)
    lista.append(minimoGlobal)

for _ in lista:
    print(_)