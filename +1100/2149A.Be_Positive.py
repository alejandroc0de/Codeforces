from collections import Counter
resultados = []

cases = int(input())
for _ in range(cases):
    resultado = 0
    n = int(input())
    numeros = list(map(int, input().split()))
    cuenta = Counter(numeros)

    impares = cuenta[-1]%2
    impares*=2
    ceros = cuenta[0]

    resultado = impares + ceros
    resultados.append(resultado)

for _ in resultados:
    print(_)