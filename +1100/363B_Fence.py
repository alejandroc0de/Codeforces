# Accepted (HLP)

n,k = map(int, input("").split(" "))
lista = list(map(int, input("").split(" ")))


suma = 0
indice = 0

# We here calculate the first sum, the first numbers, and we will evaluate from them 

for o in range(k-1,-1,-1):
    suma = suma + lista[o]


minima = suma 

# We add the next value and delete the first one, if the current sum is min then we store that index 

for i in range(k,n):
    suma = suma + lista[i] - lista[i-k]
    if suma < minima:
        minima = suma
        indice = i-k +1
    
print(indice+1)
