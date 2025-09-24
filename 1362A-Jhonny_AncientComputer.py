# accepted 1000 

def powerOfTwo(n):
    return n>0 and (n & (n-1)) == 0
results = []



cases = int(input())
for i in range(cases):
    steps = 0
    a,b = map(int, input().split(" "))
    if(a==b):
        results.append(0)
        continue
    maximun = max(a,b)
    minimun = min(a,b)
    if(maximun%minimun != 0):            #Si no son multiplos por ningun lado llega 
        results.append(-1)
        continue
    ratio = (maximun//minimun)           # cuantas veces multiplicamos para llegar al min 
    if(powerOfTwo(ratio)):               # el ratio pues es el que nos permite saber la cantidad de steps necesarios 
        while ratio > 1 :
            if(ratio%8 == 0):
                ratio = ratio // 8
            elif (ratio%4 == 0):
                ratio = ratio // 4
            elif (ratio%2 == 0):
                ratio = ratio // 2
            steps = steps + 1
        results.append(steps)
        continue
    else:
        results.append(-1)

for i in results:
    print(i)




