# accepeted 
import sys
import math
input = sys.stdin.readline
resultados = []

cases = int(input())
for _ in range(cases):
    year = int(input())
    square = math.sqrt(year)
    if(square%1 == 0):
        res = str(int(square))+(" ")+("0")
    else:
        res =(-1)
    resultados.append(res)

for _ in resultados:
    print(_)

