cases = int(input(""))

result = []

for i in range (cases):

    x,y = list(map(int,input("").split()))
    a,b = list(map(int,input("").split()))

    dolares = 0

    

    while (x and y > 0):
        x = x - 1
        y = y - 1
        dolares = dolares + b
    while (x > 0 and y == 0):
        a = a - 1
        dolares = dolares + a
    while (y > 0 and x == 0):
        y = y - 1
        dolares = dolares + a 

    result.append(dolares)

for i in result:
    print(i)