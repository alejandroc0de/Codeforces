# accepted 

import bisect 

numberShops = int(input())
prices = list(map(int,input().split(" ")))
daysToBuy = int(input())
coins = []
for i in range(0,daysToBuy,1):
    coin = int(input())
    coins.append(coin)

prices.sort()

lista = []
for i in coins:
    solucion = bisect.bisect_right(prices,i)
    lista.append(solucion)


for i in lista:
    print(i)