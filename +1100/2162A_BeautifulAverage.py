# accepted

import sys
from collections import Counter

input = sys.stdin.readline

cases = int(input())
res = []

for _ in range(cases):
    n = int(input())
    numeros = list(map(int, input().split()))
    res.append(max(numeros))



for _ in res:
    print(_)