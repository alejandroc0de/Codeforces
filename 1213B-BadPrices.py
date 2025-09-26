datasets = int(input())
resultados = []

for _ in range(datasets):
    contador = 0 
    price = int(input())
    prices = []
    prices = list(map(int, input().split(" ")))

    prices.sort()

    for i in prices:
        if price > i:
            contador = contador + 1
            continue
        else:
            continue
    resultados.append(contador)

for _ in resultados:
    print(_)