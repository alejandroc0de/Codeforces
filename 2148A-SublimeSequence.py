# accepted 

testCases = int(input())
numeros = []

for i in range(testCases):
    number, length = map(int, input("").split(" "))


    if(length%2!= 0):
        numeros.append(number)
    else:
        numeros.append(0)

for i in numeros:
    print(i)