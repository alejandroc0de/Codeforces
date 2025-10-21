# Account Qualifying 
n = int(input())
numeros = list(map(int, input().split()))

balance = 0
first_index = {0: -1}  # balance 0 visto antes de empezar
r = 0  # longitud máxima del subarreglo balanceado

for i in range(n):
    if numeros[i] > 0:
        balance += 1
    elif numeros[i] < 0:
        balance -= 1

    if balance in first_index:
        r = max(r, i - first_index[balance])
    else:
        first_index[balance] = i

print(r)

# Still cant grasp it 