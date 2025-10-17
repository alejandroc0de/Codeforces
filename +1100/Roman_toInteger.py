# MCMXCIV 1994 'I', 'V', 'X', 'L', 'C', 'D', 'M'

import sys
input = sys.stdin.readline

input1 = "III"
values = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
n = len(input1)
current = 0 
flag = True
i = 0

while i<n:
    if i+1 < n and values[input1[i]]< values[input1[i+1]]: # Revisamos si el i+1 entraria en index, si no lo sacamos antes de que bote error
        current = current + (values[input1[i+1]]-values[input1[i]])
        i = i+2
    else:
        current = current + values[input1[i]]
        i = i +1

print(current)