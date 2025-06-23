# accepted 

cases = int(input(""))

result = []

for b in range(cases):

    x,y = list(map(int,input("").split()))
    a,b = list(map(int,input("").split()))

    dolares = 0

    ambos = min(x,y)
    remaining = max(x,y)-ambos
    precioambos = ambos*min(b, 2*a)
    
    # el minimo entre b o multiplicar el precio 1 dos veces

    preciorestante = remaining * a

    final = precioambos + preciorestante
    result.append(final)

for i in result:
    print(i)
