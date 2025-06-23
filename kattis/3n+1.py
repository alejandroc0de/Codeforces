lista = [] 


for i in range(4):
    a, b = map(int, input().split())

    ans = 0 

    for i in range(a,b+1):
        contador = 1
        while i != 1:
            if (i == 1):
                break
            if (i % 2 != 0):
                i = 3*i+ 1
            else:
                i = i // 2
            contador = contador + 1
        ans = max(ans,contador)
    lista.append((ans))

for i in range(len(lista)):
    print(a,b,lista[i])