# ACCEPTED 

lista = []
s,n = map(int,input().split(" "))
contador = 0

for i in range(0,n,1):
    x = list(map(int, input().split(" ")))
    lista.append(x)

lista.sort() # sort by strenght


for j in range(n):
    if(s > lista[j][0]):
        contador = contador + 1
        s = s + lista[j][1]

if (contador == n):
    print("YES")
else:
    print("NO")
