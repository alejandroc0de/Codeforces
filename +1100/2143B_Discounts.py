# ACCEPTED 

import sys
from collections import deque
input = sys.stdin.readline
res = []

cases = int(input())

for _ in range(cases):

    numberProducts, vouchers = map(int, input().split())
    prices = list(map(int, input().split()))
    valueVouchers = list(map(int, input().split()))
    ones = valueVouchers.count(1)
    valueVouchers.sort()
    prices.sort()
    suma = 0

    for one in range(ones):
        if not prices:
            break
        prices.pop()
    
    for value in valueVouchers:
        if not prices:
            break
        if value == 1:
            continue
        if value <= len(prices):
            evaluar = prices[-value:]
            for i in range (len(evaluar)):
                prices.pop()
            suma = suma + (sum(evaluar)-evaluar[0])
    res.append(suma+sum(prices))

for _ in res:
    print(_)

