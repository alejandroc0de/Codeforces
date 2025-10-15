#Array of edges (DIRECTED)

n = 8 #Nodes
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

#Convert to adjacency matrix

M = []
for i in range(n):
    M.append([0]*n) #Creates matrix n*n
for origen,destino in A:
    M[origen][destino] = 1 #En cada posicion de A marcamos un 1 

# Convert to adj List
from collections import defaultdict
D = defaultdict(list)
for origen,destino in A:
    D[origen].append(destino) # D[destino].append(origen) UNDIRECTED
print(D) #R: {0: [1, 3], 1: [2], 3: [4, 6, 7], 4: [2, 5], 5: [2]})
print(D[3]) #R: [4, 6, 7] Asi vemos facil conexiones

###################################################################

#DFS RECURSION 
def dfs_recursive(node):
    print(node) #Procesamos nodo
    for nei_node in D[node]: #Revisamos los neighbors
        if nei_node not in seen:
            seen.add(nei_node) #Añadimos de una y luego recursion
            dfs_recursive(nei_node)
source = 0
seen = set() #Sets for O(1)
seen.add(source)
dfs_recursive(source)
#R: 0 1 2 3 4 5 6 7


#DFS STACK
source = 0
seen = set()
seen.add(source)
stack = [source]
while stack:
    node = stack.pop() #Sacamos y procesamos del stack el ultimo
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node) #Append el neighbor to visit 
#R: 0 3 7 6 4 5 2 1


#BFS (QUEUE)
source = 0
from collections import deque
seen = set()
seen.add(source)
q = deque()
q.append(source)
while q:
    node = q.popleft() #First in, first out (index[0])
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node) # Agrega al final
#R: 0 1 3 2 4 6 7 5