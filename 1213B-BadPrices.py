#accepted (HLPD)

datasets = int(input())

resultados = []

for _ in range(datasets):
    contador = 0 
    dias = int(input())
    prices = []
    prices = list(map(int, input().split(" ")))
    min_price = float("inf")

    for i in range(dias-1,-1,-1):
        if(min_price<prices[i]):
            contador = contador + 1
        min_price = min(min_price, prices[i])

    resultados.append(contador)


for l in resultados:
    print(l)


