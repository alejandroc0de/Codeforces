# Build min heap
# Time O(n), Space: O(1)

#Creamos el minheap con heapify
A = [-4,3,1,0,2,5,10,8,12,9]
import heapq
heapq.heapify(A)
# R : [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9]


# Heap Push (Insert Element) Time O(log n)
heapq.heappush(A,4) # Cual heap? y el valor a agregar y lo agrega en su lugar del heap


# Heap Pop (Extract min) Time O (log n) 
minn = heapq.heappop(A)
print(A,minn)
#R : [0, 2, 1, 3, 4, 5, 10, 8, 12, 9]    -4


# Heap Sort Time O (n log n)
def heapsort(arr):  # Le pasamos un array y le hacemos heapify
    heapq.heapify(arr) 
    n = len(arr)   
    new_list = [0]*n # Una nueva lista llena de 0 con el len del array 

    # Hacemos esto por la cantidad de numeros en el array, le hacemos pop al array y lo agregamos en el mismo index de la
    # lista y luego retornamos la lista cuando termine, esto hace O(n log n)
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list

print(heapsort([1,3,5,7,9,2,4,5,6,4,2,4,4])) #Le pasamos el array a la funcion 
# R: [1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 9]



## Heapify siempre crea un min heap, para crear un MAX = 
B = [-4,3,1,0,2,5,10,8,12,9]
length = len(B)

for i in range(length):
    B[i] = -B[i]   # Convertimos a negativo y ahi si hacemos heapify y ya tenemos max heap
heapq.heapify(B)
# R = [-12, -9, -10, -8, -2, -5, -1, -3, 0, 4]
largest = -heapq.heappop(B)           #Pasarle - para que vuelva a ser positivo 
# R = 12
# Si hacemos push tenemos que igual paserle negativo 



## Tuples of items on heap 

D = [5,4,3,5,4,3,5,5,4]
from collections import Counter
counter = Counter(D)
print(counter)
# R = Counter({5: 4, 4: 3, 3: 2}) Esto saca las ocurrencias de un value (Key = element, Value = Freq.)
heap = []
for key,value in counter.items():
    print(key,value)
    # R = 5 4 / 4 3 / 3 2             Las frecuencias del counter 
    heapq.heappush(heap,(value,key))
print(heap)
# R [(2, 3), (4, 5), (3, 4)]      Hace sort by Value y si hay tie hace sort by the other element