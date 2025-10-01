# accepted 1000

number = int(input())

lista = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

for i in range(len(lista)):
    if number%lista[i]==0:
        print("YES")
        exit(0)
print("NO")