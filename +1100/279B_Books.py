# accepeted, slicing window, hlpd

books, freeTime = map(int, input().split(" "))
times = list(map(int, input().split(" ")))

# Inicializamos todo en 0 
maxLibros = float('-inf')
inicio = 0
sumaCurrent = 0


# Mientras que la sumacurrent no sea mayor al tope, le sumamos mas, si es mayor, le vamos restando del inicio
for final in range(books):
    sumaCurrent = sumaCurrent + times[final]
    while sumaCurrent > freeTime:
        sumaCurrent = sumaCurrent - times[inicio]
        inicio = inicio + 1
    maxLibros = max(maxLibros, final-inicio+1)


print(maxLibros)