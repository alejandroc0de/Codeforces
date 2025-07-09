# accepted

students, amount = map(int, input().split(" "))
lista1 = []
lista = list(map(int, input().split(" ")))

lista.sort()

usar = (amount-students)+1

for i in range(usar):
    grupo1 = lista[i:i+students]
    diferencia = grupo1[students-1]-grupo1[0]
    lista1.append(diferencia)

if lista1:
    print(min(lista1))
else:
    print(0)
