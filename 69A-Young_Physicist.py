# accepted

cases = int(input())

matriz= []

# Una matriz es una lista de listas, entonces como ya tenemos la lista, solo la añadimos a la matriz

for i in range(cases):
    lista = list(map(int, input().split(" ")))
    matriz.append(lista)




columna1 = 0 
columna2 = 0
columna3 = 0 


# coge cada fila, y añade la posicion 0, que seria la primera columna, luego la 1 que es la columna 2 , y asi con cada fila, asi sumamos cada columna en cada variables
for fila in matriz:
    columna1 = columna1+ fila[0]
    columna2 = columna2 + fila[1]
    columna3 = columna3 + fila[2]

if(columna1 == 0 and columna2 == 0 and columna3 == 0):
    print("YES")
else:
    print("NO")