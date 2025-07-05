n = int(input())
res = 0
lista = []


def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(0,n+1,1):
    lista.append(fibonacci(i))

print(lista)