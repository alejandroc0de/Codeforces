#accepted

a = int(input())
b = int(input())
c = int(input())



first = 0

first = max((a+b)*c,(a*b)+c,a*(b+c),a*(b*c),a+b+c)

print(first)