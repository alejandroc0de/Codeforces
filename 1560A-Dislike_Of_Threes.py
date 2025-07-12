# accepted

cases = int(input())
listafinal = []
lista = []

for i in range(1,2000,1):
    if i % 3 == 0:
        continue
    numero = str(i)
    if (numero.endswith('3')):
        continue
    else:
        lista.append(i)


for i in range (0,cases,1):
    goal = int(input())
    listafinal.append((lista[goal-1]))

for i in listafinal:
    print(i)