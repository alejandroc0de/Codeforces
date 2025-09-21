n = int(input())
arreglo = (1,2,1,3,4,3,5,6,7,7)
lista = []
contador = 0

for i in range(len(arreglo)-1):
    if(arreglo[i] != arreglo[i+1]):
        contador = contador + 1
        continue
    lista.append(contador)

print(max(lista))