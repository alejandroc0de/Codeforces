# accepted 

cases = int(input())
listafinal = []

for f in range(0,cases,1):
    goal,starting = map(int, input().split(" "))
    lista = list(map(int, input().split(" ")))

    # minimo entre la posicion inicial y el inicio de la lista o el final de la lista, luego de tener eso
    # hay que recorrer si o si toda la lista entonces, ultima posicion menos la primera O(n)
    resultado = min(abs(starting-lista[0]),abs(starting-max(lista)))+max(lista)-lista[0]
    listafinal.append(resultado)

for i in listafinal:
    print(i)