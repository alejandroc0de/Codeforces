# too slow with Python or counters, Manual counter needed or C++
import sys
input = sys.stdin.readline

cases = int(input())
resultados = []

for _ in range(cases):
    n,target = map(int, input().split())
    nums = list(map(int, input().split()))

    freq = [0]*(n+1) #Pues los valores van desde 0 
    present = [False]*(n+1)
    missing = 0

    for i in nums:
        freq[i] +=1
        present[i] = True

    targetIncluded = freq[target]
    for _ in range(target):
        if present[_]==False:
            missing +=1

    resultados.append(max(missing,targetIncluded))

for _ in resultados:
    print(_)