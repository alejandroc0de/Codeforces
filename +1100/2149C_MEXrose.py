# too slow with Python or counters, Manual counter needed or C++

from collections import Counter
import sys
input = sys.stdin.readline

cases = int(input())
resultados = []
 
for _ in range(cases):
    n,target = map(int, input().split())
    nums = list(map(int, input().split()))
    count = Counter(nums)
    suma1 = 0
    contador = 0


    # We need to check how many are missing that are less than target 
    for _ in range(target):
        if _ not in count:
            contador +=1
    suma1 = count[target]
    resultados.append(max(contador,suma1))



for _ in resultados:
    print(_)
