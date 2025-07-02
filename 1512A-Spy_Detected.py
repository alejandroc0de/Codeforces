# accepted 

from collections import Counter

cases = int(input())
lista = []

for z in range(0,cases,1):
    largo = int(input())
    numeros = list(map(int, input().split(" ")))

    count = Counter(numeros)
    goal = count.most_common(1)
    goal = goal[0][0]

    for i in range(0,len(numeros),1):
        if (numeros[i] != goal):
            lista.append(i+1)
            break


for i in lista:
    print(i)